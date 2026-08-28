#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moneys Monitor - collector (schema v2)
=====================================================================
Raccolta dati PASSIVA da fonti pubbliche. Nessun ordine, nessun trading.

OUTPUT
  data/latest.json    snapshot corrente completo (news incluse)
  data/history.jsonl  storico append-only SENZA news    (~3 KB/riga, era 14 KB)
  data/prices.csv     serie tidy long: 1 riga = 1 ticker x 1 raccolta
  data/news.jsonl     news deduplicate: 1 riga = 1 notizia, scritta una volta sola

COSA E' STATO CORRETTO RISPETTO ALLA v1
  1. prev_close.  Yahoo NON popola meta.previousClose su /v8/finance/chart:
     restituisce None. La v1 faceva `chartPreviousClose or previousClose`, quindi
     usava sempre chartPreviousClose = chiusura PRIMA della finestra richiesta,
     cioe' ~5 sedute fa. Verificato: S&P chartPreviousClose=7745.06 contro
     chiusura reale precedente 7674.37 -> tutte le change_pct erano sbagliate.
     Ora la chiusura precedente si ricava dalla serie dei close giornalieri,
     confrontando le date nel fuso orario della borsa.
  2. Rate limiting. Yahoo risponde 429 sotto carico: backoff lungo (30s/90s),
     concorrenza ridotta, e catena di fallback per fx/crypto/tassi.
  3. Carry-forward. Se un ticker fallisce ovunque si riusa l'ultimo valore noto
     marcato `stale_reason`, invece di perdere la riga.
  4. Scritture atomiche, errori contati e visibili in _meta.
  5. News fuori dallo storico e deduplicate (erano riscritte 2,1 volte in media).
"""

from __future__ import annotations

import csv
import html
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any

try:
    from zoneinfo import ZoneInfo
except ImportError:                                    # pragma: no cover
    ZoneInfo = None                                     # type: ignore

SCHEMA_VERSION = 2
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
FRED_API_KEY = os.environ.get("FRED_API_KEY", "").strip()

# ------------------------------------------------------------------ config

# cls: equity | etf | crypto | commodity | fx | rate | vol
# fb : provider di fallback se Yahoo fallisce
YAHOO_TICKERS: dict[str, dict[str, Any]] = {
    "^GSPC":      {"label": "S&P 500",                        "cls": "equity"},
    "^DJI":       {"label": "Dow Jones",                      "cls": "equity"},
    "^IXIC":      {"label": "Nasdaq Composite",               "cls": "equity"},
    "^RUT":       {"label": "Russell 2000",                   "cls": "equity"},
    "FTSEMIB.MI": {"label": "FTSE MIB",                       "cls": "equity"},
    "^FTSE":      {"label": "FTSE 100 UK",                    "cls": "equity"},
    "^GDAXI":     {"label": "DAX Germania",                   "cls": "equity"},
    "^FCHI":      {"label": "CAC 40 Francia",                 "cls": "equity"},
    "^STOXX50E":  {"label": "Euro Stoxx 50",                  "cls": "equity"},
    "^N225":      {"label": "Nikkei 225",                     "cls": "equity"},
    "^HSI":       {"label": "Hang Seng",                      "cls": "equity"},
    "000001.SS":  {"label": "Shanghai Composite",             "cls": "equity"},
    "^BVSP":      {"label": "Bovespa Brasile",                "cls": "equity"},
    "^VIX":       {"label": "VIX (volatilita)",               "cls": "vol"},

    # ---------------------------------------------------------------
    # ETF/ETC del PAC su Trade Republic.
    # VERIFICA ogni ticker contro le TUE posizioni (ISIN in app -> cerca il
    # ticker della borsa su cui e' quotato). Un ticker sbagliato non fa
    # crashare nulla: produce una riga di errore in _meta e viene saltato.
    # ---------------------------------------------------------------
    "CSPX.MI":    {"label": "iShares Core S&P 500 (IE00B5BMR087)",   "cls": "etf"},
    "SWDA.MI":    {"label": "iShares Core MSCI World (IE00B4L5Y983)","cls": "etf"},
    "EIMI.MI":    {"label": "iShares Core MSCI EM IMI (IE00BKM4GZ66)","cls": "etf"},
    "SGLD.MI":    {"label": "Invesco Physical Gold ETC (IE00B579F325)","cls": "etf"},
    "4GLD.DE":    {"label": "Xetra-Gold ETC (DE000A0S9GB0)",         "cls": "etf"},
    "AGGH.MI":    {"label": "iShares Core Global Aggregate Bond",    "cls": "etf"},

    "BTC-USD":    {"label": "Bitcoin",   "cls": "crypto", "fb": ("coingecko", "bitcoin")},
    "ETH-USD":    {"label": "Ethereum",  "cls": "crypto", "fb": ("coingecko", "ethereum")},
    "SOL-USD":    {"label": "Solana",    "cls": "crypto", "fb": ("coingecko", "solana")},

    "GC=F":       {"label": "Oro (futures)",           "cls": "commodity"},
    "SI=F":       {"label": "Argento (futures)",       "cls": "commodity"},
    "CL=F":       {"label": "Petrolio WTI (futures)",  "cls": "commodity"},
    "BZ=F":       {"label": "Petrolio Brent (futures)","cls": "commodity"},
    "NG=F":       {"label": "Gas naturale (futures)",  "cls": "commodity"},
    "HG=F":       {"label": "Rame (futures)",          "cls": "commodity"},

    "EURUSD=X":   {"label": "EUR/USD",            "cls": "fx", "fb": ("ecb", "USD")},
    "GBPUSD=X":   {"label": "GBP/USD",            "cls": "fx"},
    "JPY=X":      {"label": "USD/JPY",            "cls": "fx"},
    "DX-Y.NYB":   {"label": "Indice dollaro DXY", "cls": "fx"},

    "^FVX":       {"label": "US 5Y Treasury Yield",  "cls": "rate", "fb": ("fred", "DGS5")},
    "^TNX":       {"label": "US 10Y Treasury Yield", "cls": "rate", "fb": ("fred", "DGS10")},
    "^TYX":       {"label": "US 30Y Treasury Yield", "cls": "rate", "fb": ("fred", "DGS30")},
}

FRED_SERIES = {
    "FEDFUNDS":            "Fed Funds Rate (USA)",
    "CPIAUCSL":            "CPI USA (indice)",
    "CPILFESL":            "CPI Core USA (indice)",
    "UNRATE":              "Disoccupazione USA",
    "PAYEMS":              "Occupati non agricoli USA (000)",
    "DGS2":                "US 2Y Treasury Rate",
    "DGS10":               "US 10Y Treasury Rate",
    "DGS30":               "US 30Y Treasury Rate",
    "T10Y2Y":              "Spread 10Y-2Y USA",
    "IRLTLT01DEM156N":     "Bund Germania 10Y",
    "IRLTLT01ITM156N":     "BTP Italia 10Y",
    "CP0000EZ19M086NEST":  "HICP Eurozona (indice)",
}

RSS_FEEDS = {
    "CNBC Business":    "https://www.cnbc.com/id/10001147/device/rss/rss.html",
    "MarketWatch":      "https://feeds.content.dowjones.io/public/rss/mw_topstories",
    "Investing.com":    "https://www.investing.com/rss/news.rss",
    "Yahoo Finance":    "https://finance.yahoo.com/news/rssindex",
    "ECB Press":        "https://www.ecb.europa.eu/rss/press.html",
    "Google News Mkts": "https://news.google.com/rss/search?q=when:1d+stock+market+OR+bond+yields+OR+ECB&hl=en-US&gl=US&ceid=US:en",
}

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
}
TIMEOUT = 20
MAX_WORKERS = 1                      # sequenziale: la concorrenza e' cio' che fa scattare i 429
BACKOFF_429 = (4, 12, 30)            # backoff corti: il budget globale sotto e' la vera difesa
BACKOFF_NET = (2, 5, 10)

# Budget massimo per l'INTERA fase prezzi. Scaduto il tempo, i ticker rimasti
# usano il carry-forward senza toccare la rete: meglio uno snapshot parziale
# che un job ucciso dal timeout che non scrive niente.
# GitHub uccide il job a timeout-minutes: se collect.py sfora, si perde tutto,
# perche' i file vengono scritti solo alla fine.
PRICE_BUDGET_S = int(os.environ.get("PRICE_BUDGET_S", "420"))   # 7 minuti
_DEADLINE = None                     # impostato in fetch_prices()

PRICES_CSV_HEADER = [
    "collected_at_utc", "ticker", "label", "asset_class", "currency", "source",
    "price", "prev_close", "chg_1d_pct", "chg_5d_pct", "chg_1m_pct", "chg_3m_pct",
    "vol20_ann_pct", "market_date", "stale",
]

_ERRORS: list[str] = []
_LOCK_SLEEP = 0.35


def _err(msg: str) -> None:
    _ERRORS.append(msg)
    print(f"  ! {msg}", file=sys.stderr)


# ------------------------------------------------------------------ http

def _past_deadline() -> bool:
    return _DEADLINE is not None and time.monotonic() > _DEADLINE


def _fetch(url: str, as_json: bool, tries: int = 3) -> Any:
    last: Exception | None = None
    for i in range(tries):
        if _past_deadline():
            raise TimeoutError("budget di raccolta esaurito")
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                raw = r.read()
            return json.loads(raw.decode("utf-8")) if as_json else raw.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (401, 403, 404, 451):
                break                                        # definitivo
            wait = BACKOFF_429[min(i, len(BACKOFF_429) - 1)] if e.code == 429 \
                else BACKOFF_NET[min(i, len(BACKOFF_NET) - 1)]
            if i < tries - 1 and not _past_deadline():
                time.sleep(min(wait + random.uniform(0, 2), 30))
        except Exception as e:
            last = e
            if i < tries - 1 and not _past_deadline():
                time.sleep(BACKOFF_NET[min(i, len(BACKOFF_NET) - 1)] + random.uniform(0, 1))
    raise last if last else RuntimeError("unreachable")


def http_json(url: str, tries: int = 3) -> Any:
    return _fetch(url, True, tries)


def http_text(url: str, tries: int = 2) -> str:
    return _fetch(url, False, tries)


# ------------------------------------------------------------------ helpers

def _local_date(epoch: Any, tzname: str | None) -> str | None:
    if not epoch:
        return None
    tz = timezone.utc
    if tzname and ZoneInfo is not None:
        try:
            tz = ZoneInfo(tzname)
        except Exception:
            pass
    return datetime.fromtimestamp(int(epoch), tz).date().isoformat()


def _today(tzname: str | None) -> str:
    if tzname and ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo(tzname)).date().isoformat()
        except Exception:
            pass
    return datetime.now(timezone.utc).date().isoformat()


def _pct(new: Any, old: Any) -> float | None:
    try:
        if new is None or old is None or float(old) == 0.0:
            return None
        return round((float(new) / float(old) - 1.0) * 100.0, 3)
    except (TypeError, ValueError):
        return None


def _vol20(closes: list[float]) -> float | None:
    if len(closes) < 21:
        return None
    tail = closes[-21:]
    rets = [(b / a - 1.0) for a, b in zip(tail, tail[1:]) if a > 0 and b > 0]
    if len(rets) < 2:
        return None
    mu = sum(rets) / len(rets)
    var = sum((r - mu) ** 2 for r in rets) / (len(rets) - 1)
    return round((var ** 0.5) * (252 ** 0.5) * 100.0, 2)


def _metrics(series: list[tuple[str, float]], price: float | None,
             market_date: str | None) -> dict[str, Any]:
    """series = [(data_locale, close)] ordinata. Ritorna prev_close + rendimenti."""
    prev, src = None, None
    if market_date:
        for d, c in reversed(series):
            if d < market_date:
                prev, src = c, "daily_series"
                break
    if prev is None and len(series) >= 2:
        prev, src = series[-2][1], "series_fallback"

    closes = [c for _, c in series]

    def back(n: int) -> float | None:
        return closes[-(n + 1)] if len(closes) > n else None

    return {
        "prev_close": round(prev, 6) if prev is not None else None,
        "prev_close_source": src,
        "chg_1d_pct": _pct(price, prev),
        "chg_5d_pct": _pct(price, back(5)),
        "chg_1m_pct": _pct(price, back(21)),
        "chg_3m_pct": _pct(price, back(62)),
        "vol20_ann_pct": _vol20(closes),
    }


# ------------------------------------------------------------------ provider: yahoo

def _from_yahoo(ticker: str) -> dict[str, Any]:
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/"
           f"{urllib.parse.quote(ticker)}?interval=1d&range=3mo")
    res = http_json(url)["chart"]["result"][0]
    meta = res["meta"]
    tzname = meta.get("exchangeTimezoneName")

    stamps = res.get("timestamp") or []
    closes = (res.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    series = [(d, float(c)) for ep, c in zip(stamps, closes)
              if c is not None and (d := _local_date(ep, tzname))]
    if not series:
        raise ValueError("serie giornaliera vuota")

    price = meta.get("regularMarketPrice")
    price = float(price) if price is not None else series[-1][1]
    market_date = _local_date(meta.get("regularMarketTime"), tzname) or series[-1][0]

    out = {"source": "yahoo", "price": price, "currency": meta.get("currency"),
           "market_date": market_date, "stale": market_date < _today(tzname),
           "ts": meta.get("regularMarketTime")}
    out.update(_metrics(series, price, market_date))
    return out


# ------------------------------------------------------------------ provider: fallback

def _from_coingecko(coin_id: str) -> dict[str, Any]:
    hist = http_json("https://api.coingecko.com/api/v3/coins/"
                     f"{coin_id}/market_chart?vs_currency=usd&days=90&interval=daily")
    pts = hist.get("prices") or []
    if not pts:
        raise ValueError("coingecko: nessun punto")
    series = [(datetime.fromtimestamp(ms / 1000, timezone.utc).date().isoformat(), float(v))
              for ms, v in pts]
    price = series[-1][1]
    md = series[-1][0]
    out = {"source": "coingecko", "price": price, "currency": "USD",
           "market_date": md, "stale": False, "ts": int(pts[-1][0] / 1000)}
    out.update(_metrics(series, price, md))
    return out


def _from_ecb_fx(quote_ccy: str) -> dict[str, Any]:
    """Tassi ufficiali BCE via frankfurter.app. Base EUR -> ritorna EUR/quote."""
    hist = http_json(f"https://api.frankfurter.app/2000-01-01..?from=EUR&to={quote_ccy}")
    rates = hist.get("rates") or {}
    series = sorted((d, float(v[quote_ccy])) for d, v in rates.items() if quote_ccy in v)
    series = series[-90:]
    if not series:
        raise ValueError("frankfurter: serie vuota")
    price, md = series[-1][1], series[-1][0]
    out = {"source": "ecb", "price": price, "currency": quote_ccy,
           "market_date": md, "stale": md < datetime.now(timezone.utc).date().isoformat(),
           "ts": None}
    out.update(_metrics(series, price, md))
    return out


def _from_fred(series_id: str) -> dict[str, Any]:
    if not FRED_API_KEY:
        raise ValueError("FRED_API_KEY assente")
    d = http_json("https://api.stlouisfed.org/fred/series/observations"
                  f"?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
                  f"&sort_order=desc&limit=120")
    obs = [o for o in d.get("observations", []) if o.get("value") not in (None, ".", "")]
    if not obs:
        raise ValueError("fred: nessuna osservazione")
    series = sorted((o["date"], float(o["value"])) for o in obs)
    price, md = series[-1][1], series[-1][0]
    out = {"source": "fred", "price": price, "currency": "PCT",
           "market_date": md, "stale": md < datetime.now(timezone.utc).date().isoformat(),
           "ts": None}
    out.update(_metrics(series, price, md))
    return out


FALLBACKS = {"coingecko": _from_coingecko, "ecb": _from_ecb_fx, "fred": _from_fred}


# ------------------------------------------------------------------ prezzi

def _load_last_known() -> dict[str, dict[str, Any]]:
    """Ultimo valore noto per ticker, per il carry-forward."""
    path = os.path.join(DATA_DIR, "latest.json")
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return {k: v for k, v in (json.load(f).get("prices") or {}).items()
                    if isinstance(v, dict) and v.get("price") is not None}
    except Exception:
        return {}


def _carry(ticker, base, last_known, reason) -> dict[str, Any] | None:
    prev = last_known.get(ticker)
    if not prev:
        return None
    keep = {k: v for k, v in prev.items() if k not in ("label", "asset_class", "ok")}
    return {**base, "ok": True, **keep, "stale": True, "stale_reason": reason,
            "chg_1d_pct": None, "chg_5d_pct": None,
            "chg_1m_pct": None, "chg_3m_pct": None}


def fetch_one(ticker: str, cfg: dict[str, Any], last_known: dict[str, Any]) -> dict[str, Any]:
    base = {"label": cfg["label"], "asset_class": cfg["cls"]}
    if _past_deadline():
        c = _carry(ticker, base, last_known, "budget_esaurito")
        return c if c else {**base, "ok": False, "error": "budget di raccolta esaurito"}
    time.sleep(random.uniform(0, _LOCK_SLEEP))
    try:
        return {**base, "ok": True, **_from_yahoo(ticker)}
    except Exception as e:
        yerr = f"{type(e).__name__}: {e}"

    fb = cfg.get("fb")
    if fb:
        kind, key = fb
        try:
            r = {**base, "ok": True, **FALLBACKS[kind](key)}
            _err(f"{ticker}: yahoo KO ({yerr}) -> fallback {kind} OK")
            return r
        except Exception as e2:
            _err(f"{ticker}: yahoo KO ({yerr}); fallback {kind} KO ({type(e2).__name__}: {e2})")
    else:
        _err(f"{ticker}: yahoo KO ({yerr}); nessun fallback configurato")

    c = _carry(ticker, base, last_known, "carry_forward_fetch_failed")
    return c if c else {**base, "ok": False, "error": yerr}


def fetch_prices() -> dict[str, Any]:
    global _DEADLINE
    _DEADLINE = time.monotonic() + PRICE_BUDGET_S
    last_known = _load_last_known()
    out: dict[str, Any] = {}
    for tk, cfg in YAHOO_TICKERS.items():
        try:
            out[tk] = fetch_one(tk, cfg, last_known)
        except Exception as e:
            out[tk] = {"label": cfg["label"], "asset_class": cfg["cls"],
                       "ok": False, "error": f"{type(e).__name__}: {e}"}
    if _past_deadline():
        _err(f"budget prezzi ({PRICE_BUDGET_S}s) esaurito: i ticker rimanenti "
             f"usano l'ultimo valore noto")
    _DEADLINE = None
    return out


# ------------------------------------------------------------------ macro

def fetch_macro() -> dict[str, Any]:
    if not FRED_API_KEY:
        _err("FRED_API_KEY assente: sezione macro vuota")
        return {"_error": "FRED_API_KEY non configurata"}
    out: dict[str, Any] = {}
    for sid, label in FRED_SERIES.items():
        try:
            d = http_json("https://api.stlouisfed.org/fred/series/observations"
                          f"?series_id={sid}&api_key={FRED_API_KEY}&file_type=json"
                          f"&sort_order=desc&limit=14")
            obs = [o for o in d.get("observations", []) if o.get("value") not in (None, ".", "")]
            if not obs:
                raise ValueError("nessuna osservazione valida")
            cur = obs[0]
            val = float(cur["value"])
            prev = float(obs[1]["value"]) if len(obs) > 1 else None
            yoy = None
            if len(obs) >= 13:
                try:
                    yoy = _pct(val, float(obs[12]["value"]))
                except Exception:
                    yoy = None
            out[sid] = {"label": label, "value": val, "date": cur["date"],
                        "prev_value": prev,
                        "delta": round(val - prev, 4) if prev is not None else None,
                        "yoy_pct": yoy}
        except Exception as e:
            _err(f"fred {sid}: {type(e).__name__}: {e}")
            out[sid] = {"label": label, "error": f"{type(e).__name__}: {e}"}
        time.sleep(0.2)
    return out


# ------------------------------------------------------------------ news

_ITEM = re.compile(r"<item[^>]*>(.*?)</item>", re.DOTALL | re.I)
_ENTRY = re.compile(r"<entry[^>]*>(.*?)</entry>", re.DOTALL | re.I)


def _tag(block: str, name: str) -> str | None:
    m = re.search(rf"<{name}[^>]*>(.*?)</{name}>", block, re.DOTALL | re.I)
    if m:
        t = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", m.group(1), flags=re.DOTALL)
        t = re.sub(r"<[^>]+>", "", t)
        t = html.unescape(t).strip()
        if t:
            return t
    m = re.search(rf'<{name}[^>]*href="([^"]+)"', block, re.I)     # atom
    return html.unescape(m.group(1)).strip() if m else None


def parse_feed(xml: str, limit: int = 12) -> list[dict[str, Any]]:
    blocks = _ITEM.findall(xml) or _ENTRY.findall(xml)
    out = []
    for b in blocks[:limit]:
        t = _tag(b, "title")
        if t:
            out.append({"title": t, "link": _tag(b, "link"),
                        "pub_date": _tag(b, "pubDate") or _tag(b, "published") or _tag(b, "updated")})
    return out


def fetch_news() -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    with ThreadPoolExecutor(max_workers=3) as pool:
        futs = {pool.submit(http_text, u): s for s, u in RSS_FEEDS.items()}
        for fut, src in futs.items():
            try:
                out[src] = parse_feed(fut.result())
            except Exception as e:
                _err(f"rss {src}: {type(e).__name__}: {e}")
                out[src] = []
    return {k: out.get(k, []) for k in RSS_FEEDS}


# ------------------------------------------------------------------ io

def atomic_write(path: str, text: str) -> None:
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def append_prices_csv(path: str, stamp: str, prices: dict[str, Any]) -> None:
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(PRICES_CSV_HEADER)
        for tk, p in prices.items():
            if not p.get("ok"):
                continue
            w.writerow([stamp, tk, p.get("label"), p.get("asset_class"), p.get("currency"),
                        p.get("source", "carry"), p.get("price"), p.get("prev_close"),
                        p.get("chg_1d_pct"), p.get("chg_5d_pct"), p.get("chg_1m_pct"),
                        p.get("chg_3m_pct"), p.get("vol20_ann_pct"), p.get("market_date"),
                        int(bool(p.get("stale")))])


def append_news_dedup(path: str, stamp: str, news: dict[str, list[dict[str, Any]]]) -> int:
    seen: set[str] = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    seen.add(json.loads(line)["k"])
                except Exception:
                    pass
    added = 0
    with open(path, "a", encoding="utf-8") as f:
        for src, items in news.items():
            for it in items:
                k = f"{src}|{it['title']}"
                if k in seen:
                    continue
                seen.add(k)
                f.write(json.dumps({"k": k, "first_seen_utc": stamp, "source": src,
                                    "title": it["title"], "link": it.get("link"),
                                    "pub_date": it.get("pub_date")}, ensure_ascii=False) + "\n")
                added += 1
    return added


# ------------------------------------------------------------------ main

def main() -> int:
    t0 = time.time()
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    os.makedirs(DATA_DIR, exist_ok=True)
    print(f"[collect] {stamp}")

    prices = fetch_prices()
    ok = sum(1 for p in prices.values() if p.get("ok"))
    live = sum(1 for p in prices.values() if p.get("ok") and not p.get("stale_reason"))
    carry = sum(1 for p in prices.values() if p.get("stale_reason"))
    print(f"  prezzi : {live} dal vivo, {carry} carry-forward, "
          f"{len(YAHOO_TICKERS) - ok} persi  (in {time.time() - t0:.0f}s)")

    macro = fetch_macro()
    print(f"  macro  : {sum(1 for v in macro.values() if isinstance(v, dict) and 'value' in v)}/{len(FRED_SERIES)}")

    news = fetch_news()
    print(f"  news   : {sum(len(v) for v in news.values())} titoli, "
          f"{sum(1 for v in news.values() if v)}/{len(RSS_FEEDS)} feed vivi")

    core = {
        "schema": SCHEMA_VERSION,
        "collected_at_utc": stamp,
        "prices": prices,
        "macro": macro,
        "_meta": {"elapsed_s": round(time.time() - t0, 1),
                  "tickers_ok": ok, "tickers_total": len(YAHOO_TICKERS),
                  "carry_forward": carry,
                  "error_count": len(_ERRORS), "errors": _ERRORS[:40]},
    }

    with open(os.path.join(DATA_DIR, "history.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(core, ensure_ascii=False) + "\n")
    append_prices_csv(os.path.join(DATA_DIR, "prices.csv"), stamp, prices)
    n_new = append_news_dedup(os.path.join(DATA_DIR, "news.jsonl"), stamp, news)

    atomic_write(os.path.join(DATA_DIR, "latest.json"),
                 json.dumps({**core, "news": news}, ensure_ascii=False, indent=2))

    print(f"[collect] fatto in {core['_meta']['elapsed_s']}s | news nuove {n_new} | errori {len(_ERRORS)}")
    if ok == 0:
        print("[collect] FATAL: nessun prezzo raccolto", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
