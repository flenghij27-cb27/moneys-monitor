#!/usr/bin/env python3
"""
Moneys Monitor — raccolta dati passiva (NO trading, NO ordini, solo lettura)
Gira via GitHub Actions ogni 5 ore. Salva snapshot in data/latest.json
e accoda storico in data/history.jsonl.
"""

import json
import os
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

# ---------- CONFIG ----------

FRED_API_KEY = os.environ.get("FRED_API_KEY", "")

# Yahoo Finance: ticker -> nome leggibile
YAHOO_TICKERS = {
    "^GSPC": "S&P 500",
    "^DJI": "Dow Jones",
    "^IXIC": "Nasdaq Composite",
    "FTSEMIB.MI": "FTSE MIB",
    "^STOXX50E": "Euro Stoxx 50",
    "^N225": "Nikkei 225",
    "GC=F": "Oro (futures)",
    "CL=F": "Petrolio WTI (futures)",
    "EURUSD=X": "EUR/USD",
    "BTC-USD": "Bitcoin",
    "^TNX": "US 10Y Treasury Yield",
}

# FRED: series_id -> nome leggibile
FRED_SERIES = {
    "FEDFUNDS": "Fed Funds Rate (USA)",
    "CPIAUCSL": "Inflazione USA (CPI)",
    "UNRATE": "Disoccupazione USA",
    "DGS10": "US 10Y Treasury Rate",
}

# News RSS — fonti pubbliche, ampio spettro
RSS_FEEDS = {
    "CNBC Business": "https://www.cnbc.com/id/10001147/device/rss/rss.html",
    "MarketWatch": "https://feeds.content.dowjones.io/public/rss/mw_topstories",
    "Investing.com": "https://www.investing.com/rss/news.rss",
    "Yahoo Finance": "https://finance.yahoo.com/news/rssindex",
    "ECB Press": "https://www.ecb.europa.eu/rss/press.html",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; MoneysMonitor/1.0; personal use)"}
TIMEOUT = 15


def http_get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_get_text(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


# ---------- PREZZI (Yahoo Finance, no key richiesta) ----------

def fetch_yahoo_quotes():
    results = {}
    for ticker, label in YAHOO_TICKERS.items():
        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
            f"?interval=1d&range=5d"
        )
        try:
            data = http_get_json(url)
            result = data["chart"]["result"][0]
            meta = result["meta"]
            price = meta.get("regularMarketPrice")
            prev_close = meta.get("chartPreviousClose") or meta.get("previousClose")
            change_pct = None
            if price is not None and prev_close:
                change_pct = round((price - prev_close) / prev_close * 100, 2)
            results[ticker] = {
                "label": label,
                "price": price,
                "prev_close": prev_close,
                "change_pct": change_pct,
                "currency": meta.get("currency"),
                "ts": meta.get("regularMarketTime"),
            }
        except Exception as e:
            results[ticker] = {"label": label, "error": str(e)}
        time.sleep(0.5)  # rispetto rate limit non ufficiale
    return results


# ---------- MACRO (FRED, richiede key gratuita) ----------

def fetch_fred_series():
    if not FRED_API_KEY:
        return {"_error": "FRED_API_KEY non configurata (vedi README setup)"}

    results = {}
    for series_id, label in FRED_SERIES.items():
        url = (
            f"https://api.stlouisfed.org/fred/series/observations"
            f"?series_id={series_id}&api_key={FRED_API_KEY}"
            f"&file_type=json&sort_order=desc&limit=1"
        )
        try:
            data = http_get_json(url)
            obs = data["observations"][0]
            results[series_id] = {
                "label": label,
                "value": obs["value"],
                "date": obs["date"],
            }
        except Exception as e:
            results[series_id] = {"label": label, "error": str(e)}
        time.sleep(0.3)
    return results


# ---------- NEWS (RSS, parsing minimale senza dipendenze esterne) ----------

def parse_rss_titles(xml_text, max_items=8):
    import re
    import html
    items = re.findall(r"<item>(.*?)</item>", xml_text, re.DOTALL)
    out = []
    for item in items[:max_items]:
        title_match = re.search(r"<title>(.*?)</title>", item, re.DOTALL)
        link_match = re.search(r"<link>(.*?)</link>", item, re.DOTALL)
        pub_match = re.search(r"<pubDate>(.*?)</pubDate>", item, re.DOTALL)
        if title_match:
            title = title_match.group(1)
            title = title.replace("<![CDATA[", "").replace("]]>", "").strip()
            title = html.unescape(title)
            out.append({
                "title": title,
                "link": html.unescape(link_match.group(1).strip()) if link_match else None,
                "pub_date": pub_match.group(1).strip() if pub_match else None,
            })
    return out


def fetch_news():
    results = {}
    for source, url in RSS_FEEDS.items():
        try:
            xml_text = http_get_text(url)
            results[source] = parse_rss_titles(xml_text)
        except Exception as e:
            results[source] = [{"error": str(e)}]
        time.sleep(0.3)
    return results


# ---------- MAIN ----------

def main():
    snapshot = {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "prices": fetch_yahoo_quotes(),
        "macro": fetch_fred_series(),
        "news": fetch_news(),
    }

    os.makedirs("data", exist_ok=True)

    # Ultimo snapshot (la dashboard legge questo)
    with open("data/latest.json", "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)

    # Storico append-only (per analisi future, 1 riga = 1 raccolta)
    with open("data/history.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(snapshot, ensure_ascii=False) + "\n")

    print(f"OK — snapshot salvato: {snapshot['collected_at_utc']}")


if __name__ == "__main__":
    main()
