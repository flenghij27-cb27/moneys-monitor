#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moneys Monitor - generatore grafici
=====================================================================
Costruisce una dashboard HTML autonoma con grafici SVG inline.
Zero dipendenze esterne: solo libreria standard. Funziona in GitHub Actions.

INPUT   data/history.jsonl (schema v1 e v2), data/historical_100y.json
OUTPUT  data/dashboard.html   pagina unica, apribile ovunque, tema chiaro/scuro

Grafici prodotti:
  1. Small multiples per classe di asset, serie normalizzate a base 100
  2. Heatmap dei rendimenti (asset x orizzonte), scala divergente
  3. Dispersione rischio/rendimento (volatilita' 20g vs rendimento 1 mese)
  4. Drawdown dal massimo del periodo
  5. Serie lunga S&P 500 e oro dal dataset storico, se presente

USO
  python3 scripts/charts.py
  python3 scripts/charts.py --out data/dashboard.html
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from html import escape
from typing import Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

# Palette categorica validata (ordine fisso, mai ciclato).
SERIES_LIGHT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
                "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
SERIES_DARK = ["#3987e5", "#d95926", "#199e70", "#c98500",
               "#d55181", "#008300", "#9085e9", "#e66767"]

# Divergente blu <-> rosso con midpoint grigio neutro.
DIV_NEG = ["#0d366b", "#184f95", "#256abf", "#3987e5", "#86b6ef", "#cde2fb"]
DIV_POS = ["#f6d0cf", "#efa9a8", "#e8817f", "#e34948", "#b62f2e", "#8a1f1e"]

GRUPPI: list[tuple[str, str, list[str]]] = [
    ("Indici azionari", "equity",
     ["^GSPC", "^IXIC", "FTSEMIB.MI", "^GDAXI", "^N225", "^HSI"]),
    ("ETF/ETC del PAC", "etf",
     ["SWDA.MI", "CSPX.MI", "EIMI.MI", "SGLD.MI", "AGGH.MI"]),
    ("Crypto", "crypto", ["BTC-USD", "ETH-USD", "SOL-USD"]),
    ("Materie prime", "commodity", ["GC=F", "SI=F", "CL=F", "HG=F", "NG=F"]),
    ("Valute e tassi", "fx", ["EURUSD=X", "DX-Y.NYB", "^TNX", "^TYX", "^FVX"]),
]

ALL_HORIZONS = [("1 sett.", 5), ("2 sett.", 10), ("1 mese", 21),
                ("2 mesi", 42), ("3 mesi", 63), ("6 mesi", 126), ("1 anno", 252)]


def usable_horizons(series: dict, min_cover: float = 0.5) -> list[tuple[str, int]]:
    """Tiene solo gli orizzonti coperti da almeno meta' degli strumenti.
    Con una finestra di 2 mesi una colonna '3 mesi' sarebbe tutta n/d."""
    lens = [len(s) for s in series.values() if len(s) > 1]
    if not lens:
        return []
    lens.sort()
    median = lens[len(lens) // 2]
    out = [(n, k) for n, k in ALL_HORIZONS if median > k]
    return out[-4:] if len(out) > 4 else out


# ------------------------------------------------------------------ dati

def read_history() -> list[dict[str, Any]]:
    p = os.path.join(DATA_DIR, "history.jsonl")
    if not os.path.exists(p):
        return []
    rows = []
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    rows.sort(key=lambda r: r.get("collected_at_utc", ""))
    return rows


def build_series(rows) -> tuple[dict[str, list[tuple[str, float]]], dict[str, str]]:
    by: dict[str, dict[str, float]] = defaultdict(dict)
    lab: dict[str, str] = {}
    for r in rows:
        day = r.get("collected_at_utc", "")[:10]
        for tk, p in (r.get("prices") or {}).items():
            if not isinstance(p, dict) or p.get("price") is None or "error" in p:
                continue
            lab[tk] = p.get("label", tk)
            try:
                by[tk][p.get("market_date") or day] = float(p["price"])
            except (TypeError, ValueError):
                continue
    return {t: sorted(v.items()) for t, v in by.items()}, lab


def ret(series, n) -> float | None:
    c = [v for _, v in series]
    if len(c) <= n or c[-(n + 1)] == 0:
        return None
    return (c[-1] / c[-(n + 1)] - 1) * 100


def vol20(series) -> float | None:
    c = [v for _, v in series][-21:]
    if len(c) < 8:
        return None
    r = [b / a - 1 for a, b in zip(c, c[1:]) if a > 0]
    if len(r) < 3:
        return None
    m = sum(r) / len(r)
    return math.sqrt(sum((x - m) ** 2 for x in r) / (len(r) - 1)) * math.sqrt(252) * 100


# ------------------------------------------------------------------ svg

def esc(s: Any) -> str:
    return escape(str(s), quote=True)


def nice_ticks(lo: float, hi: float, n: int = 4) -> list[float]:
    if hi <= lo:
        return [lo]
    raw = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(raw))
    step = min([m * mag for m in (1, 2, 2.5, 5, 10)], key=lambda s: abs(s - raw))
    start = math.ceil(lo / step) * step
    out, v = [], start
    while v <= hi + step * 0.01:
        out.append(round(v, 10))
        v += step
    return out


def sparkline(series, w=300, h=110, pad_l=40, pad_b=20, pad_t=10, pad_r=8,
              color="var(--s1)", base100=True, label="") -> str:
    """Linea singola normalizzata. Niente doppio asse: una sola scala."""
    if len(series) < 2:
        return f'<svg viewBox="0 0 {w} {h}" role="img"><text x="8" y="{h/2}" '\
               f'class="muted" font-size="11">dati insufficienti</text></svg>'
    vals = [v for _, v in series]
    base = vals[0] or 1
    ys = [v / base * 100 for v in vals] if base100 else vals
    lo, hi = min(ys), max(ys)
    if hi == lo:
        lo, hi = lo - 1, hi + 1
    span = hi - lo
    lo -= span * 0.08
    hi += span * 0.08
    iw, ih = w - pad_l - pad_r, h - pad_t - pad_b

    def X(i): return pad_l + (i / (len(ys) - 1)) * iw
    def Y(v): return pad_t + (1 - (v - lo) / (hi - lo)) * ih

    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(ys))
    area = f"{pad_l},{Y(lo)} {pts} {X(len(ys)-1):.1f},{Y(lo)}"
    up = ys[-1] >= 100 if base100 else ys[-1] >= ys[0]
    gid = f"g{abs(hash(label)) % 100000}"

    parts = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">']
    parts.append(f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
                 f'<stop offset="0%" stop-color="{color}" stop-opacity="0.18"/>'
                 f'<stop offset="100%" stop-color="{color}" stop-opacity="0"/>'
                 f'</linearGradient></defs>')
    for t in nice_ticks(lo, hi, 3):
        y = Y(t)
        if pad_t - 2 <= y <= h - pad_b + 2:
            parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{w-pad_r}" y2="{y:.1f}" class="grid"/>')
            parts.append(f'<text x="{pad_l-5}" y="{y+3.5:.1f}" text-anchor="end" class="axis">{t:.0f}</text>')
    if base100 and lo <= 100 <= hi:
        parts.append(f'<line x1="{pad_l}" y1="{Y(100):.1f}" x2="{w-pad_r}" y2="{Y(100):.1f}" class="baseline"/>')
    parts.append(f'<polygon points="{area}" fill="url(#{gid})"/>')
    parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2" '
                 f'stroke-linejoin="round" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{X(len(ys)-1):.1f}" cy="{Y(ys[-1]):.1f}" r="3.5" fill="{color}" '
                 f'stroke="var(--surface)" stroke-width="2"/>')
    delta = ys[-1] - 100 if base100 else (ys[-1] / ys[0] - 1) * 100
    parts.append(f'<text x="{w-pad_r}" y="{pad_t+2}" text-anchor="end" '
                 f'class="{"pos" if up else "neg"}" font-size="12" font-weight="600">'
                 f'{delta:+.1f}%</text>')
    parts.append(f'<text x="{pad_l}" y="{h-4}" class="axis">{esc(series[0][0][5:])}</text>')
    parts.append(f'<text x="{w-pad_r}" y="{h-4}" text-anchor="end" class="axis">{esc(series[-1][0][5:])}</text>')
    parts.append("</svg>")
    return "".join(parts)


def heatmap(rows_data, cols, w=760) -> str:
    """Rendimenti asset x orizzonte. Scala divergente, zero = grigio."""
    if not rows_data:
        return "<p class='muted'>dati insufficienti</p>"
    lh, cw = 26, 92
    lw = min(230, w - cw * len(cols) - 8)
    w = lw + cw * len(cols) + 8
    h = 34 + lh * len(rows_data)
    mx = max((abs(v) for _, vs in rows_data for v in vs if v is not None), default=1) or 1

    def col(v):
        if v is None:
            return "var(--surface-2)"
        f = min(abs(v) / mx, 1.0)
        idx = min(int(f * len(DIV_POS)), len(DIV_POS) - 1)
        return (DIV_POS if v > 0 else DIV_NEG)[idx] if abs(v) > 1e-9 else "var(--surface-2)"

    p = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Heatmap rendimenti">']
    for j, c in enumerate(cols):
        p.append(f'<text x="{lw + cw*j + cw/2}" y="18" text-anchor="middle" class="axis">{esc(c)}</text>')
    for i, (name, vs) in enumerate(rows_data):
        y = 30 + lh * i
        p.append(f'<text x="{lw-8}" y="{y+17}" text-anchor="end" class="lbl">{esc(name)}</text>')
        for j, v in enumerate(vs):
            x = lw + cw * j
            fill = col(v)
            # 2px di gap fra celle: il fondo separa i marchi
            p.append(f'<rect x="{x+1}" y="{y+1}" width="{cw-2}" height="{lh-2}" rx="3" fill="{fill}"/>')
            if v is not None:
                strong = abs(v) / mx > 0.55
                p.append(f'<text x="{x+cw/2}" y="{y+17}" text-anchor="middle" font-size="11" '
                         f'font-weight="600" fill="{"#fff" if strong else "var(--ink)"}">{v:+.1f}%</text>')
            else:
                p.append(f'<text x="{x+cw/2}" y="{y+17}" text-anchor="middle" font-size="11" '
                         f'class="muted">n/d</text>')
    p.append("</svg>")
    return "".join(p)


def scatter(points, w=760, h=380) -> str:
    """Rischio (x) vs rendimento (y). Massimo 3 colori: cap all-pairs della palette."""
    pts = [p for p in points if p[1] is not None and p[2] is not None]
    if len(pts) < 2:
        return "<p class='muted'>dati insufficienti</p>"
    pl, pr, pt, pb = 56, 16, 16, 44
    xs = [p[1] for p in pts]
    ys = [p[2] for p in pts]
    x0, x1 = 0, max(xs) * 1.15
    y0, y1 = min(min(ys) * 1.2, -1), max(max(ys) * 1.2, 1)
    iw, ih = w - pl - pr, h - pt - pb

    def X(v): return pl + (v - x0) / (x1 - x0) * iw
    def Y(v): return pt + (1 - (v - y0) / (y1 - y0)) * ih

    classes = list(dict.fromkeys(p[3] for p in pts))[:3]
    cmap = {c: f"var(--s{i+1})" for i, c in enumerate(classes)}

    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Rischio rendimento">']
    for t in nice_ticks(y0, y1, 4):
        o.append(f'<line x1="{pl}" y1="{Y(t):.1f}" x2="{w-pr}" y2="{Y(t):.1f}" class="grid"/>')
        o.append(f'<text x="{pl-8}" y="{Y(t)+4:.1f}" text-anchor="end" class="axis">{t:+.0f}%</text>')
    for t in nice_ticks(x0, x1, 4):
        o.append(f'<text x="{X(t):.1f}" y="{h-pb+18}" text-anchor="middle" class="axis">{t:.0f}%</text>')
    o.append(f'<line x1="{pl}" y1="{Y(0):.1f}" x2="{w-pr}" y2="{Y(0):.1f}" class="baseline"/>')
    # Etichette selettive: in un grappolo denso non si etichetta tutto.
    # Chi non entra resta leggibile via tooltip e nella tabella sotto.
    placed: list[tuple[float, float]] = []
    dots = [(X(px), Y(py)) for _, px, py, _ in pts]        # le etichette evitano anche i punti
    for name, x, y, cls in sorted(pts, key=lambda p: -p[2]):
        c = cmap.get(cls, "var(--s1)")
        cx, cy = X(x), Y(y)
        o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{c}" '
                 f'stroke="var(--surface)" stroke-width="2"><title>{esc(name)}: '
                 f'vol {x:.1f}%, rend. {y:+.1f}%</title></circle>')
        lx, ly, fits = cx + 11, cy + 4, False
        for _ in range(4):
            tw = len(name) * 6.6 + 6                                 # larghezza stimata a 10px
            if all(abs(ly - py) > 12 or abs(lx - px) > 130 for px, py in placed) \
               and all(abs(ly - 4 - dy) > 9 or not (lx - 4 < dx < lx + tw + 4)
                       for dx, dy in dots) \
               and pt + 6 < ly < h - pb - 6 and lx + tw < w - pr:
                fits = True
                break
            ly += 13
        if not fits:
            continue
        placed.append((lx, ly))
        if ly - (cy + 4) > 6:
            o.append(f'<line x1="{cx+6:.1f}" y1="{cy+2:.1f}" x2="{lx-3:.1f}" y2="{ly-3:.1f}" '
                     f'stroke="var(--line)" stroke-width="1"/>')
        o.append(f'<text x="{lx:.1f}" y="{ly:.1f}" class="lbl" font-size="10">{esc(name)}</text>')
    o.append(f'<text x="{pl+iw/2}" y="{h-6}" text-anchor="middle" class="axis">'
             f'volatilita annualizzata 20 giorni</text>')
    o.append(f'<text x="14" y="{pt+ih/2}" transform="rotate(-90 14 {pt+ih/2})" '
             f'text-anchor="middle" class="axis">rendimento 1 mese</text>')
    o.append("</svg>")
    legend = " ".join(
        f'<span class="key"><i style="background:{cmap[c]}"></i>{esc(c)}</span>' for c in classes)
    return f'<div class="legend">{legend}</div>' + "".join(o)


def bars(items, w=760, unit="%", pos_is_good=True) -> str:
    """
    Barre orizzontali divergenti. Estremita' arrotondate 4px ancorate alla
    linea dello zero. Il valore sta sempre in un corridoio riservato, mai
    sopra l'etichetta: con barre tutte dello stesso segno le due scritte
    finirebbero altrimenti nello stesso punto.
    """
    if not items:
        return "<p class='muted'>dati insufficienti</p>"
    bh, gap, lw, gut = 24, 6, 150, 62
    h = len(items) * (bh + gap) + 20
    vals = [v for _, v in items]
    vmin, vmax = min(vals + [0.0]), max(vals + [0.0])
    span = (vmax - vmin) or 1.0
    x_lo, x_hi = lw + gut, w - gut
    plot = x_hi - x_lo

    def X(v): return x_lo + (v - vmin) / span * plot
    zero = X(0.0)

    o = [f'<svg viewBox="0 0 {w} {h}" role="img">']
    o.append(f'<line x1="{zero:.1f}" y1="4" x2="{zero:.1f}" y2="{h-8}" class="baseline"/>')
    for i, (name, v) in enumerate(items):
        y = 6 + i * (bh + gap)
        xv = X(v)
        x, bw = (zero, xv - zero) if v >= 0 else (xv, zero - xv)
        bw = max(bw, 2.0)
        c = "var(--s3)" if (v >= 0) == pos_is_good else "var(--s8)"
        o.append(f'<text x="{lw-8}" y="{y+16}" text-anchor="end" class="lbl">{esc(name)}</text>')
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{bh}" rx="4" fill="{c}"/>')
        if v >= 0:
            o.append(f'<text x="{x+bw+8:.1f}" y="{y+16}" text-anchor="start" class="val">{v:+.1f}{unit}</text>')
        else:
            o.append(f'<text x="{x-8:.1f}" y="{y+16}" text-anchor="end" class="val">{v:+.1f}{unit}</text>')
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ pagina

CSS = """
/* Neutri con leggera deriva fredda: scelti, non ereditati dal grigio puro. */
:root{color-scheme:light;
--surface:#f7f8fa;--surface-2:#eaecf1;--card:#ffffff;
--ink:#101319;--ink-2:#4b5364;--muted:#828b9c;--line:#dfe3ea;
--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--s5:#e87ba4;--s6:#008300;--s7:#4a3aa7;--s8:#e34948;
--pos:#0f7a55;--neg:#b62f2e;--accent:#2a78d6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
--surface:#0e1116;--surface-2:#1c212b;--card:#151a22;
--ink:#f2f5fa;--ink-2:#aeb7c6;--muted:#7a8496;--line:#252c38;
--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;
--pos:#4ec49a;--neg:#e66767;--accent:#3987e5}}
:root[data-theme="dark"]{color-scheme:dark;
--surface:#0e1116;--surface-2:#1c212b;--card:#151a22;
--ink:#f2f5fa;--ink-2:#aeb7c6;--muted:#7a8496;--line:#252c38;
--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;
--pos:#4ec49a;--neg:#e66767;--accent:#3987e5}
*{box-sizing:border-box}
body{margin:0;background:var(--surface);color:var(--ink);
font:15px/1.55 "IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.wrap{max-width:1120px;margin:0 auto;padding:34px 20px 72px}
h1{font-family:Archivo,"IBM Plex Sans",system-ui,sans-serif;font-size:30px;font-weight:700;
margin:0 0 6px;letter-spacing:-.025em;text-wrap:balance}
h2{font-family:Archivo,"IBM Plex Sans",system-ui,sans-serif;font-size:18px;font-weight:600;
margin:42px 0 6px;letter-spacing:-.012em;text-wrap:balance}
p.sub{color:var(--ink-2);margin:0 0 4px;font-size:13.5px}
p.note{color:var(--muted);font-size:12.5px;margin:0 0 14px;max-width:74ch}
code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.92em}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;overflow-x:auto}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(268px,1fr))}
.tile{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 12px 6px;
display:flex;flex-direction:column;gap:2px}
.tile h3{font-family:Archivo,sans-serif;font-size:13px;margin:0;font-weight:600;letter-spacing:-.005em}
.tile .tk{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--muted);margin:0 0 4px;
font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.tile svg{width:100%;height:auto;display:block}
.card svg{width:100%;height:auto;display:block;min-width:620px}
/* strip di sintesi: il riassunto viene prima del dettaglio */
.kpis{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));margin:18px 0 4px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;
display:flex;flex-direction:column;gap:3px}
.kpi .k{font-size:10.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);font-weight:600}
.kpi .v{font-family:Archivo,sans-serif;font-size:23px;font-weight:700;letter-spacing:-.03em;
font-variant-numeric:tabular-nums;line-height:1.15}
.kpi .d{font-size:11.5px;color:var(--ink-2)}
.chip{display:inline-flex;align-items:center;gap:5px;align-self:flex-start;
font-size:10.5px;font-weight:600;padding:2px 7px;border-radius:999px;
background:var(--surface-2);color:var(--ink-2);letter-spacing:.02em}
.chip.up,.chip.risk{background:color-mix(in srgb,var(--pos) 15%,transparent);color:var(--pos)}
.chip.down,.chip.safe{background:color-mix(in srgb,var(--neg) 15%,transparent);color:var(--neg)}
text.axis{fill:var(--muted);font-size:10px;font-family:"IBM Plex Mono",monospace}
text.lbl{fill:var(--ink-2);font-size:11px}
text.val{fill:var(--ink);font-size:11px;font-weight:600;font-variant-numeric:tabular-nums;
font-family:"IBM Plex Mono",monospace}
text.muted{fill:var(--muted)}
.pos{fill:var(--pos)}.neg{fill:var(--neg)}
line.grid{stroke:var(--line);stroke-width:1}
line.baseline{stroke:var(--muted);stroke-width:1;stroke-dasharray:3 3}
.legend{display:flex;gap:14px;flex-wrap:wrap;margin:0 0 10px;font-size:12px;color:var(--ink-2)}
.key{display:inline-flex;align-items:center;gap:6px}
.key i{width:10px;height:10px;border-radius:3px;display:inline-block}
table{border-collapse:collapse;width:100%;font-size:12.5px;font-variant-numeric:tabular-nums}
th,td{padding:7px 10px;border-bottom:1px solid var(--line);text-align:right}
td:not(:first-child){font-family:"IBM Plex Mono",monospace;letter-spacing:-.02em}
th:first-child,td:first-child{text-align:left}
th{color:var(--muted);font-weight:600;font-size:10.5px;text-transform:uppercase;letter-spacing:.06em}
tbody tr:hover{background:var(--surface-2)}
footer{margin-top:52px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);
font-size:12px;max-width:74ch}
@media (prefers-reduced-motion:no-preference){.tile,.kpi{transition:border-color .15s ease}}
.tile:hover,.kpi:hover{border-color:var(--muted)}
"""


def kpi_strip(series, lab) -> str:
    """Il riassunto prima del dettaglio: cosa e' successo, in quattro numeri."""
    # Universo confrontabile: fuori VIX, valute e tassi. Un indice di
    # volatilita' o un cambio non sono "il peggior investimento del mese".
    RANK = {t for _, cls, ts in GRUPPI if cls in ("equity", "etf", "crypto", "commodity")
            for t in ts}
    R = {t: ret(s, 21) for t, s in series.items() if len(s) > 21 and t in RANK}
    if not R:
        return ""
    best = max(R.items(), key=lambda kv: kv[1])
    worst = min(R.items(), key=lambda kv: kv[1])
    on = [R[t] for t in ("^GSPC", "^IXIC", "^N225", "^GDAXI", "FTSEMIB.MI") if t in R]
    off = [R[t] for t in ("GC=F", "SI=F") if t in R]
    spread = (sum(on) / len(on) - sum(off) / len(off)) if on and off else None
    vols = {t: vol20(s) for t, s in series.items() if t in RANK and vol20(s)}
    calm = min(vols.items(), key=lambda kv: kv[1]) if vols else None

    CHIP = {"up": "in salita", "down": "in calo",
            "risk": "propensione al rischio", "safe": "domanda di rifugio"}

    def card(k, v, d, cls=""):
        c = f' <span class="chip {cls}">{CHIP[cls]}</span>' if cls else ""
        return (f'<div class="kpi"><span class="k">{esc(k)}</span>'
                f'<span class="v">{esc(v)}</span><span class="d">{esc(d)}{c}</span></div>')

    parts = [
        card("Migliore sul mese", f"{best[1]:+.1f}%", lab.get(best[0], best[0]), "up"),
        card("Peggiore sul mese", f"{worst[1]:+.1f}%", lab.get(worst[0], worst[0]), "down"),
    ]
    if spread is not None:
        parts.append(card("Azioni meno oro", f"{spread:+.1f} pp",
                          "quanto le azioni battono i rifugi, sul mese",
                          "risk" if spread > 0 else "safe"))
    if calm:
        parts.append(card("Il piu' tranquillo", f"{calm[1]:.1f}%",
                          f"{lab.get(calm[0], calm[0])} - volatilita 20g"))
    return f'<div class="kpis">{"".join(parts)}</div>'


def page(series, lab) -> str:
    gen = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    days = sorted({d for s in series.values() for d, _ in s})
    o = ['<title>Moneys Monitor</title>',
         '<link rel="preconnect" href="https://fonts.googleapis.com">',
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Archivo:wght@600;700&family=IBM+Plex+Mono:wght@400;600&'
         'family=IBM+Plex+Sans:wght@400;600&display=swap">',
         f"<style>{CSS}</style>", '<div class="wrap">']
    o.append("<h1>Moneys Monitor</h1>")
    o.append(f'<p class="sub">Finestra osservata: {days[0]} &rarr; {days[-1]} '
             f'({len(days)} giornate di mercato, {len(series)} strumenti)</p>')
    o.append(f'<p class="note">Generato {gen}. Serie ricostruite dalle osservazioni raccolte, '
             f'non dal campo <code>change_pct</code> dello storico v1.</p>')
    o.append(kpi_strip(series, lab))

    # 1. small multiples
    for title, cls, tickers in GRUPPI:
        avail = [t for t in tickers if len(series.get(t, [])) >= 2]
        if not avail:
            continue
        o.append(f"<h2>{esc(title)}</h2>")
        o.append('<p class="note">Ogni riquadro parte da 100 il primo giorno: '
                 'confronta l&rsquo;andamento, non il prezzo.</p>')
        o.append('<div class="grid">')
        for i, t in enumerate(avail):
            c = f"var(--s{(i % 8) + 1})"
            o.append('<div class="tile">'
                     f'<h3>{esc(lab.get(t, t))}</h3><p class="tk">{esc(t)} &middot; '
                     f'{series[t][-1][1]:,.2f}</p>'.replace(",", " ")
                     + sparkline(series[t], color=c, label=lab.get(t, t)) + "</div>")
        o.append("</div>")

    # 2. heatmap
    HZ = usable_horizons(series)
    watch = [t for _, _, ts in GRUPPI for t in ts if len(series.get(t, [])) > 5]
    hm = [(lab.get(t, t), [ret(series[t], n) for _, n in HZ]) for t in watch]
    si = min(1, len(HZ) - 1) if HZ else 0
    hm.sort(key=lambda r: -(r[1][si] if r[1] and r[1][si] is not None else -999))
    o.append("<h2>Rendimenti per orizzonte</h2>")
    o.append('<p class="note">Blu = negativo, rosso = positivo, grigio = fermo. '
             f'Ordinato su &laquo;{esc(HZ[si][0]) if HZ else ""}&raquo;.</p>')
    o.append(f'<div class="card">{heatmap(hm, [h for h, _ in HZ])}</div>')

    # 3. scatter
    CLS = {"^GSPC": "azionario", "^IXIC": "azionario", "FTSEMIB.MI": "azionario",
           "^GDAXI": "azionario", "^N225": "azionario", "^HSI": "azionario",
           "SWDA.MI": "azionario", "CSPX.MI": "azionario", "EIMI.MI": "azionario",
           "BTC-USD": "crypto", "ETH-USD": "crypto", "SOL-USD": "crypto",
           "GC=F": "materie prime", "SI=F": "materie prime", "CL=F": "materie prime",
           "HG=F": "materie prime", "NG=F": "materie prime"}
    pts = [(lab.get(t, t), vol20(series[t]), ret(series[t], 21), CLS[t])
           for t in CLS if len(series.get(t, [])) > 8]
    o.append("<h2>Quanto rischio per quanto rendimento</h2>")
    o.append('<p class="note">Piu&rsquo; a destra = oscilla di piu&rsquo;. Piu&rsquo; in alto = ha reso di piu&rsquo; '
             'nell&rsquo;ultimo mese. In alto a sinistra sta il posto migliore. '
             'Dove i punti si accavallano l&rsquo;etichetta e&rsquo; omessa: '
             'passa il mouse sul punto o guarda la tabella.</p>')
    o.append(f'<div class="card">{scatter(pts)}</div>')

    # 4. drawdown
    dd = []
    for t in watch:
        s = [v for _, v in series[t]]
        pk = mx = s[0]
        for v in s:
            pk = max(pk, v)
            mx = min(mx, (v / pk - 1) * 100) if pk else mx
        dd.append((lab.get(t, t), round(min(mx, 0), 2)))
    dd.sort(key=lambda x: x[1])
    o.append("<h2>Massima perdita dal picco (nel periodo osservato)</h2>")
    o.append('<p class="note">Quanto avresti perso comprando nel momento peggiore '
             'e vendendo nel punto piu&rsquo; basso successivo.</p>')
    o.append(f'<div class="card">{bars(dd[:12], pos_is_good=True)}</div>')

    # 5. tabella (identita' mai affidata al solo colore)
    o.append("<h2>Tabella</h2><div class='card'><table><thead><tr><th>Strumento</th>"
             "<th>Ultimo</th>" + "".join(f"<th>{esc(h)}</th>" for h, _ in HZ) +
             "<th>Vol. 20g</th></tr></thead><tbody>")
    for t in watch:
        s = series[t]
        cells = "".join(
            f'<td class="{"pos" if (v or 0) >= 0 else "neg"}" style="color:var(--{"pos" if (v or 0)>=0 else "neg"})">'
            f'{v:+.2f}%</td>' if v is not None else "<td>n/d</td>"
            for v in (ret(s, n) for _, n in HZ))
        vv = vol20(s)
        o.append(f"<tr><td>{esc(lab.get(t,t))}</td><td>{s[-1][1]:,.2f}</td>{cells}"
                 f"<td>{vv:.1f}%</td></tr>".replace(",", " ") if vv is not None
                 else f"<tr><td>{esc(lab.get(t,t))}</td><td>{s[-1][1]:,.2f}</td>{cells}<td>n/d</td></tr>".replace(",", " "))
    o.append("</tbody></table></div>")

    # 6. storico lungo
    hp = os.path.join(DATA_DIR, "historical_100y.json")
    if os.path.exists(hp):
        try:
            with open(hp, encoding="utf-8") as f:
                H = json.load(f)
            sp = H.get("sp500_annual_returns_pct", {})
            yrs = sorted(k for k in sp if k.isdigit())
            if yrs:
                worst = sorted(((y, sp[y]) for y in yrs), key=lambda x: x[1])[:10]
                neg = sum(1 for y in yrs if sp[y] < 0)
                o.append("<h2>Un secolo di S&amp;P 500</h2>")
                o.append(f'<p class="note">{len(yrs)} anni ({yrs[0]}&ndash;{yrs[-1]}): '
                         f'<strong>{neg}</strong> chiusi in perdita, '
                         f'<strong>{len(yrs)-neg}</strong> in guadagno. '
                         f'I dieci anni peggiori:</p>')
                o.append(f'<div class="card">{bars([(y, v) for y, v in worst], pos_is_good=True)}</div>')
        except Exception as e:
            print(f"[charts] historical_100y.json non leggibile: {e}", file=sys.stderr)

    o.append("<footer>Dati pubblici a scopo informativo. Non e&rsquo; consulenza finanziaria. "
             "La finestra osservata e&rsquo; breve: i numeri di volatilita&rsquo; e drawdown "
             "descrivono questo periodo, non il rischio strutturale di un asset.</footer>")
    o.append("</div>")
    return "\n".join(o)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA_DIR, "dashboard.html"))
    args = ap.parse_args()

    rows = read_history()
    if not rows:
        print("[charts] nessuno storico in data/history.jsonl", file=sys.stderr)
        return 1
    series, lab = build_series(rows)
    if not series:
        print("[charts] nessuna serie ricostruibile", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(page(series, lab))
    print(f"[charts] {len(series)} strumenti -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
