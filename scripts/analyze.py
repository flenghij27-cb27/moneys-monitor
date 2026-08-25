#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moneys Monitor - analyze
=====================================================================
Legge lo storico (schema v1 E v2) e produce l'analisi di mercato corretta.

Perche' esiste: lo storico v1 contiene change_pct sbagliate (prev_close
congelato ~5 sedute). Questo script IGNORA quel campo e ricalcola tutto
dalla serie dei prezzi osservati, quindi recupera anche i dati gia' raccolti.

OUTPUT
  data/analysis.json   tutte le metriche, machine-readable
  data/REPORT.md       report leggibile
  data/prices.csv      ricostruito dallo storico se assente (backfill una tantum)

USO
  python3 scripts/analyze.py                # analisi completa
  python3 scripts/analyze.py --backfill     # solo ricostruzione prices.csv
  python3 scripts/analyze.py --top 15       # quanti outlier mostrare
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

HORIZONS = [("1d", 1), ("1w", 5), ("1m", 21), ("3m", 63), ("6m", 126), ("1y", 252)]

RISK_ON = {"^GSPC", "^IXIC", "^RUT", "^N225", "^GDAXI", "FTSEMIB.MI",
           "BTC-USD", "ETH-USD", "SOL-USD", "HG=F", "SWDA.MI", "EIMI.MI"}
RISK_OFF = {"GC=F", "SI=F", "^VIX", "AGGH.MI", "XEON.MI"}


# ------------------------------------------------------------------ lettura

def read_history(path: str) -> list[dict[str, Any]]:
    if not os.path.exists(path):
        print(f"[analyze] storico assente: {path}", file=sys.stderr)
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"[analyze] riga {n} illeggibile, saltata: {e}", file=sys.stderr)
    rows.sort(key=lambda r: r.get("collected_at_utc", ""))
    return rows


def build_series(rows: list[dict[str, Any]]) -> tuple[dict[str, list[tuple[str, float]]], dict[str, dict]]:
    """
    Ricostruisce, per ogni ticker, la serie (data_di_mercato, prezzo).
    Un solo punto per data: l'ultima osservazione vince. Cosi' i weekend
    (in cui il feed ripete la chiusura di venerdi') non generano falsi giorni.
    """
    by_date: dict[str, dict[str, float]] = defaultdict(dict)
    meta: dict[str, dict] = {}
    for r in rows:
        collected = r.get("collected_at_utc", "")[:10]
        for tk, p in (r.get("prices") or {}).items():
            if not isinstance(p, dict) or p.get("price") is None or "error" in p:
                continue
            meta.setdefault(tk, {})
            meta[tk]["label"] = p.get("label", tk)
            meta[tk]["asset_class"] = p.get("asset_class", "n/d")
            meta[tk]["currency"] = p.get("currency")
            d = p.get("market_date") or collected          # v1 non ha market_date
            try:
                by_date[tk][d] = float(p["price"])
            except (TypeError, ValueError):
                continue
    return ({tk: sorted(dv.items()) for tk, dv in by_date.items()}, meta)


# ------------------------------------------------------------------ metriche

def pct(a: float | None, b: float | None) -> float | None:
    if a is None or b in (None, 0):
        return None
    return round((a / b - 1.0) * 100.0, 2)


def horizon_returns(series: list[tuple[str, float]]) -> dict[str, float | None]:
    closes = [c for _, c in series]
    if not closes:
        return {}
    cur = closes[-1]
    out: dict[str, float | None] = {}
    for name, n in HORIZONS:
        out[name] = pct(cur, closes[-(n + 1)]) if len(closes) > n else None
    return out


def max_drawdown(series: list[tuple[str, float]]) -> dict[str, Any]:
    peak, mdd, pk_d, tr_d = None, 0.0, None, None
    bp = bt = None
    for d, c in series:
        if peak is None or c > peak:
            peak, pk_d = c, d
        if peak and peak > 0:
            dd = (c / peak - 1.0) * 100.0
            if dd < mdd:
                mdd, bp, bt = dd, pk_d, d
    return {"max_drawdown_pct": round(mdd, 2), "peak_date": bp, "trough_date": bt}


def ann_vol(series: list[tuple[str, float]], window: int = 20) -> float | None:
    closes = [c for _, c in series][-(window + 1):]
    if len(closes) < 5:
        return None
    rets = [b / a - 1.0 for a, b in zip(closes, closes[1:]) if a > 0]
    if len(rets) < 2:
        return None
    mu = sum(rets) / len(rets)
    var = sum((r - mu) ** 2 for r in rets) / (len(rets) - 1)
    return round(math.sqrt(var) * math.sqrt(252) * 100, 2)


def correlation(a: list[float], b: list[float]) -> float | None:
    n = min(len(a), len(b))
    if n < 8:
        return None
    a, b = a[-n:], b[-n:]
    ra = [y / x - 1 for x, y in zip(a, a[1:]) if x > 0]
    rb = [y / x - 1 for x, y in zip(b, b[1:]) if x > 0]
    n = min(len(ra), len(rb))
    if n < 6:
        return None
    ra, rb = ra[-n:], rb[-n:]
    ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = sum((x - ma) ** 2 for x in ra)
    vb = sum((y - mb) ** 2 for y in rb)
    if va <= 0 or vb <= 0:
        return None
    return round(cov / math.sqrt(va * vb), 3)


# ------------------------------------------------------------------ analisi

def analyze(rows: list[dict[str, Any]], top: int) -> dict[str, Any]:
    series, meta = build_series(rows)
    if not series:
        return {"error": "nessuna serie ricostruibile dallo storico"}

    assets: dict[str, Any] = {}
    for tk, s in series.items():
        if len(s) < 2:
            continue
        rets = horizon_returns(s)
        assets[tk] = {
            "label": meta[tk]["label"],
            "asset_class": meta[tk].get("asset_class", "n/d"),
            "currency": meta[tk].get("currency"),
            "last_price": s[-1][1],
            "last_date": s[-1][0],
            "n_osservazioni": len(s),
            "returns_pct": rets,
            "vol20_ann_pct": ann_vol(s),
            **max_drawdown(s),
        }

    def rank(h: str, rev: bool):
        vals = [(tk, a["returns_pct"].get(h)) for tk, a in assets.items()
                if a["returns_pct"].get(h) is not None]
        vals.sort(key=lambda x: x[1], reverse=rev)
        return [{"ticker": tk, "label": assets[tk]["label"],
                 "asset_class": assets[tk]["asset_class"],
                 "chg_pct": v, "price": assets[tk]["last_price"]} for tk, v in vals[:top]]

    outliers = {h: {"migliori": rank(h, True), "peggiori": rank(h, False)}
                for h, _ in HORIZONS if any(a["returns_pct"].get(h) is not None for a in assets.values())}

    # --- risk appetite: media dei rendimenti risk-on meno risk-off ---
    risk: dict[str, Any] = {}
    for h, _ in HORIZONS:
        on = [a["returns_pct"][h] for tk, a in assets.items()
              if tk in RISK_ON and a["returns_pct"].get(h) is not None]
        off = [a["returns_pct"][h] for tk, a in assets.items()
               if tk in RISK_OFF and tk != "^VIX" and a["returns_pct"].get(h) is not None]
        if on and off:
            risk[h] = {"risk_on_medio_pct": round(sum(on) / len(on), 2),
                       "risk_off_medio_pct": round(sum(off) / len(off), 2),
                       "spread_pct": round(sum(on) / len(on) - sum(off) / len(off), 2)}

    # --- divergenze: coppie normalmente correlate che si sono slegate ---
    pairs = [("^GSPC", "^IXIC"), ("^GSPC", "GC=F"), ("^GSPC", "BTC-USD"),
             ("GC=F", "SI=F"), ("CL=F", "BZ=F"), ("^TNX", "GC=F"),
             ("EURUSD=X", "DX-Y.NYB"), ("^GSPC", "^VIX"), ("SWDA.MI", "^GSPC")]
    divs = []
    for a, b in pairs:
        if a not in series or b not in series:
            continue
        c = correlation([x for _, x in series[a]], [x for _, x in series[b]])
        ra = assets.get(a, {}).get("returns_pct", {}).get("1m")
        rb = assets.get(b, {}).get("returns_pct", {}).get("1m")
        if c is None or ra is None or rb is None:
            continue
        divs.append({"coppia": f"{a} vs {b}",
                     "label": f"{assets[a]['label']} vs {assets[b]['label']}",
                     "correlazione_20g": c,
                     "chg_1m_a_pct": ra, "chg_1m_b_pct": rb,
                     "divergenza_pp": round(ra - rb, 2)})
    divs.sort(key=lambda d: -abs(d["divergenza_pp"]))

    # --- qualita' dei dati ---
    last = rows[-1]
    v1 = sum(1 for r in rows if r.get("schema") is None)
    stale = [tk for tk, p in (last.get("prices") or {}).items()
             if isinstance(p, dict) and p.get("stale")]
    carry = [tk for tk, p in (last.get("prices") or {}).items()
             if isinstance(p, dict) and p.get("stale_reason")]

    macro = {}
    for sid, m in (last.get("macro") or {}).items():
        if isinstance(m, dict) and "value" in m:
            macro[sid] = {k: m.get(k) for k in ("label", "value", "date", "delta", "yoy_pct")}

    curva = None
    try:
        y2 = macro.get("DGS2", {}).get("value")
        y10 = macro.get("DGS10", {}).get("value")
        y30 = macro.get("DGS30", {}).get("value")
        if y2 and y10:
            curva = {"spread_10_2_bp": round((y10 - y2) * 100, 1),
                     "spread_30_10_bp": round((y30 - y10) * 100, 1) if y30 else None,
                     "invertita": y10 < y2}
    except Exception:
        curva = None

    return {
        "generato_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "finestra": {"da": rows[0].get("collected_at_utc"), "a": rows[-1].get("collected_at_utc"),
                     "snapshot": len(rows), "righe_schema_v1": v1},
        "qualita_dati": {
            "asset_con_serie": len(assets),
            "prezzi_stale_ultimo_snapshot": stale,
            "carry_forward_ultimo_snapshot": carry,
            "nota": ("Le change_pct salvate nello schema v1 sono errate (prev_close congelato). "
                     "Questo report le ignora e ricalcola tutto dalla serie osservata."),
        },
        "asset": assets,
        "outlier": outliers,
        "risk_appetite": risk,
        "divergenze": divs[:12],
        "macro": macro,
        "curva_tassi": curva,
    }


# ------------------------------------------------------------------ output

def fmt(v: Any, suf: str = "", dec: int = 2) -> str:
    if v is None:
        return "n/d"
    if isinstance(v, float):
        return f"{v:,.{dec}f}{suf}".replace(",", " ")
    return f"{v}{suf}"


def to_markdown(a: dict[str, Any]) -> str:
    if "error" in a:
        return f"# Report\n\nErrore: {a['error']}\n"
    L: list[str] = []
    w = a["finestra"]
    L.append("# Moneys Monitor - Report di mercato\n")
    L.append(f"Generato: `{a['generato_utc']}`  \n"
             f"Finestra: `{w['da']}` -> `{w['a']}` ({w['snapshot']} snapshot, "
             f"{a['qualita_dati']['asset_con_serie']} asset)\n")
    L.append(f"> {a['qualita_dati']['nota']}\n")

    if a.get("risk_appetite"):
        L.append("\n## Appetito al rischio\n")
        L.append("| Orizzonte | Risk-on medio | Risk-off medio | Spread |")
        L.append("|---|---:|---:|---:|")
        for h, r in a["risk_appetite"].items():
            L.append(f"| {h} | {fmt(r['risk_on_medio_pct'],'%')} | "
                     f"{fmt(r['risk_off_medio_pct'],'%')} | **{fmt(r['spread_pct'],' pp')}** |")

    for h in ("1d", "1w", "1m"):
        o = a["outlier"].get(h)
        if not o:
            continue
        L.append(f"\n## Outlier {h}\n")
        L.append("| # | Migliori | % | | Peggiori | % |")
        L.append("|--:|---|--:|---|---|--:|")
        for i in range(min(6, max(len(o["migliori"]), len(o["peggiori"])))):
            g = o["migliori"][i] if i < len(o["migliori"]) else None
            b = o["peggiori"][i] if i < len(o["peggiori"]) else None
            L.append(f"| {i+1} | {g['label'] if g else ''} | {fmt(g['chg_pct'],'%') if g else ''} "
                     f"| | {b['label'] if b else ''} | {fmt(b['chg_pct'],'%') if b else ''} |")

    if a.get("divergenze"):
        L.append("\n## Divergenze principali (1 mese)\n")
        L.append("| Coppia | Corr. 20g | A | B | Divergenza |")
        L.append("|---|--:|--:|--:|--:|")
        for d in a["divergenze"][:8]:
            L.append(f"| {d['label']} | {fmt(d['correlazione_20g'],'',3)} | {fmt(d['chg_1m_a_pct'],'%')} "
                     f"| {fmt(d['chg_1m_b_pct'],'%')} | **{fmt(d['divergenza_pp'],' pp')}** |")

    if a.get("macro"):
        L.append("\n## Macro\n")
        L.append("| Indicatore | Valore | Data | Var. |")
        L.append("|---|--:|---|--:|")
        for m in a["macro"].values():
            L.append(f"| {m['label']} | {fmt(m['value'])} | {m['date']} | {fmt(m.get('delta'))} |")
        if a.get("curva_tassi"):
            c = a["curva_tassi"]
            L.append(f"\nCurva USA: 10Y-2Y **{fmt(c['spread_10_2_bp'],' bp',1)}**, "
                     f"30Y-10Y **{fmt(c.get('spread_30_10_bp'),' bp',1)}**, "
                     f"invertita: **{'si' if c['invertita'] else 'no'}**\n")

    L.append("\n## Volatilita' e drawdown (dalla finestra osservata)\n")
    L.append("| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |")
    L.append("|---|--:|--:|--:|--:|")
    for tk, x in sorted(a["asset"].items(), key=lambda kv: -(kv[1].get("vol20_ann_pct") or 0))[:15]:
        L.append(f"| {x['label']} | {fmt(x['last_price'],'',4)} | {fmt(x['returns_pct'].get('1m'),'%')} "
                 f"| {fmt(x.get('vol20_ann_pct'),'%')} | {fmt(x.get('max_drawdown_pct'),'%')} |")

    L.append("\n---\n*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*\n")
    return "\n".join(L)


def backfill_prices_csv(rows: list[dict[str, Any]], path: str) -> int:
    series, meta = build_series(rows)
    n = 0
    with open(path, "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["market_date", "ticker", "label", "asset_class", "currency", "close"])
        for tk, s in sorted(series.items()):
            for d, c in s:
                wr.writerow([d, tk, meta[tk]["label"], meta[tk].get("asset_class", "n/d"),
                             meta[tk].get("currency"), c])
                n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--backfill", action="store_true",
                    help="ricostruisce data/prices_daily.csv dallo storico ed esce")
    args = ap.parse_args()

    rows = read_history(os.path.join(DATA_DIR, "history.jsonl"))
    if not rows:
        print("[analyze] nessun dato", file=sys.stderr)
        return 1

    if args.backfill:
        p = os.path.join(DATA_DIR, "prices_daily.csv")
        n = backfill_prices_csv(rows, p)
        print(f"[analyze] backfill: {n} righe -> {p}")
        return 0

    a = analyze(rows, args.top)
    with open(os.path.join(DATA_DIR, "analysis.json"), "w", encoding="utf-8") as f:
        json.dump(a, f, ensure_ascii=False, indent=2)
    with open(os.path.join(DATA_DIR, "REPORT.md"), "w", encoding="utf-8") as f:
        f.write(to_markdown(a))
    backfill_prices_csv(rows, os.path.join(DATA_DIR, "prices_daily.csv"))

    print(f"[analyze] {a['finestra']['snapshot']} snapshot, "
          f"{a['qualita_dati']['asset_con_serie']} asset -> data/REPORT.md, data/analysis.json")
    if a["qualita_dati"]["prezzi_stale_ultimo_snapshot"]:
        print(f"[analyze] mercati chiusi/stale: "
              f"{', '.join(a['qualita_dati']['prezzi_stale_ultimo_snapshot'][:8])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
