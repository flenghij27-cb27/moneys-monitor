#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moneys Monitor - motore PAC (Trade Republic)
=====================================================================
Analizza un Piano di Accumulo a partire dalle transazioni reali.

INPUT
  pac/transactions.csv   le tue operazioni (export TR -> vedi README)
  pac/config.json        pesi target, benchmark, parametri fiscali
  data/prices_daily.csv  serie prezzi (prodotta da scripts/analyze.py)
  data/latest.json       prezzi correnti (prodotto da scripts/collect.py)

OUTPUT
  data/pac_report.json   tutte le metriche
  data/PAC_REPORT.md     report leggibile

COSA CALCOLA (e perche')
  MWR / XIRR    rendimento del TUO capitale, che pesa QUANDO hai versato.
                E' la metrica corretta per un PAC: versamenti irregolari.
  TWR           rendimento dello strumento, neutro rispetto ai versamenti.
                Serve per confrontarti con un indice senza barare.
  Benchmark     stessi identici versamenti, alle stesse date, su un solo ETF.
                Risponde a: "il mio mix ha battuto il World, o no?"
  Drift         scostamento dai pesi target.
  Ribilanciamento senza vendere: come indirizzare i PROSSIMI versamenti per
                riallinearti, evitando la tassazione del 26% su una vendita.
  Fisco IT      simulazione: 26%, asimmetria minus/plus su ETF UCITS, bollo 0,2%.

ATTENZIONE
  La simulazione fiscale e' indicativa. Trade Republic, come sostituto d'imposta
  in regime amministrato (per conti con IBAN italiano), applica il calcolo
  ufficiale: il suo report fiscale prevale sempre su questo script.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from typing import Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
PAC_DIR = os.path.join(ROOT, "pac")

BUY_TYPES = {"BUY", "ACQUISTO", "PAC", "SAVEBACK", "ROUNDUP"}
SELL_TYPES = {"SELL", "VENDITA"}
INCOME_TYPES = {"DIVIDEND", "DIVIDENDO", "INTEREST", "INTERESSI", "CEDOLA"}
CASH_TYPES = {"DEPOSIT", "WITHDRAWAL", "FEE", "TAX", "BOLLO"}

DEFAULT_CONFIG: dict[str, Any] = {
    "base_currency": "EUR",
    "lot_method": "average",              # "average" | "lifo" | "fifo"
    "benchmark": {"ticker": "SWDA.MI", "name": "iShares Core MSCI World"},
    "tax": {
        "capital_gains_pct": 26.0,
        "govies_whitelist_pct": 12.5,
        "crypto_pct": 33.0,               # Italia, realizzi dal 01/01/2026
        "stamp_duty_pct": 0.20,           # imposta di bollo titoli, annua
        "loss_carry_years": 4,
    },
    "positions": [],
}


# ------------------------------------------------------------------ util

def d(x: Any, default: float = 0.0) -> float:
    if x is None:
        return default
    s = str(x).strip().replace(" ", "").replace("€", "").replace("%", "")
    if not s:
        return default
    # accetta sia 1.234,56 sia 1,234.56 sia 1234.56
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") \
            else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return default


def parse_date(x: Any) -> str | None:
    s = str(x).strip()[:19]
    if not s:
        return None
    for f in ("%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y", "%Y-%m-%dT%H:%M:%S", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s[:len(datetime.now().strftime(f))], f).date().isoformat()
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return None


def fmt(v: Any, suf: str = "", dec: int = 2) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/d"
    if isinstance(v, (int, float)):
        return f"{v:,.{dec}f}{suf}".replace(",", " ")
    return f"{v}{suf}"


# ------------------------------------------------------------------ input

def load_config() -> dict[str, Any]:
    p = os.path.join(PAC_DIR, "config.json")
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            user = json.load(f)
        for k, v in user.items():
            if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                cfg[k].update(v)
            else:
                cfg[k] = v
    else:
        print(f"[pac] config assente ({p}), uso i default", file=sys.stderr)
    return cfg


def load_transactions() -> list[dict[str, Any]]:
    p = os.path.join(PAC_DIR, "transactions.csv")
    if not os.path.exists(p):
        print(f"[pac] MANCA {p} — vedi pac/transactions.example.csv", file=sys.stderr)
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        rows = list(csv.DictReader(f, dialect=dialect))

    out = []
    for i, r in enumerate(rows, 2):
        r = { (k or "").strip().lower(): (v or "").strip() for k, v in r.items() }
        dt = parse_date(r.get("date") or r.get("data"))
        if not dt:
            print(f"[pac] riga {i}: data illeggibile, saltata", file=sys.stderr)
            continue
        typ = (r.get("type") or r.get("tipo") or "").upper()
        qty = d(r.get("quantity") or r.get("quantita"))
        px = d(r.get("price") or r.get("prezzo"))
        fee = d(r.get("fees") or r.get("commissioni"))
        amt = d(r.get("amount_eur") or r.get("importo"))
        if not amt and qty and px:
            amt = qty * px + (fee if typ in BUY_TYPES else -fee)
        out.append({
            "row": i, "date": dt, "type": typ,
            "isin": (r.get("isin") or "").upper(),
            "ticker": (r.get("ticker") or "").upper(),
            "name": r.get("name") or r.get("nome") or "",
            "qty": qty, "price": px, "fees": fee, "amount": amt,
            "note": r.get("note", ""),
        })
    out.sort(key=lambda t: (t["date"], t["row"]))
    return out


def load_prices() -> tuple[dict[str, dict[str, float]], dict[str, float]]:
    """(serie storiche per ticker, prezzi correnti)"""
    hist: dict[str, dict[str, float]] = defaultdict(dict)
    p = os.path.join(DATA_DIR, "prices_daily.csv")
    if os.path.exists(p):
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                try:
                    hist[r["ticker"].upper()][r["market_date"]] = float(r["close"])
                except (KeyError, TypeError, ValueError):
                    continue
    cur: dict[str, float] = {}
    lp = os.path.join(DATA_DIR, "latest.json")
    if os.path.exists(lp):
        with open(lp, encoding="utf-8") as f:
            for tk, v in (json.load(f).get("prices") or {}).items():
                if isinstance(v, dict) and v.get("price") is not None:
                    cur[tk.upper()] = float(v["price"])
    for tk, s in hist.items():
        cur.setdefault(tk, s[max(s)])
    return hist, cur


def price_on(hist: dict[str, dict[str, float]], tk: str, day: str) -> float | None:
    s = hist.get(tk.upper())
    if not s:
        return None
    keys = [k for k in s if k <= day]
    return s[max(keys)] if keys else s[min(s)]


# ------------------------------------------------------------------ finanza

def xirr(flows: list[tuple[str, float]], guess: float = 0.1) -> float | None:
    """
    Tasso interno di rendimento con cashflow a date irregolari (MWR).
    flows: [(data ISO, importo)] — negativo = esborso, positivo = incasso.
    Newton-Raphson, con bisezione di sicurezza se Newton diverge.
    """
    if len(flows) < 2:
        return None
    if not (any(f < 0 for _, f in flows) and any(f > 0 for _, f in flows)):
        return None
    t0 = date.fromisoformat(flows[0][0])
    yrs = [(date.fromisoformat(dt) - t0).days / 365.0 for dt, _ in flows]
    amts = [a for _, a in flows]

    def npv(r: float) -> float:
        if r <= -0.999999:
            return float("inf")
        return sum(a / (1.0 + r) ** t for a, t in zip(amts, yrs))

    r = guess
    for _ in range(100):
        f = npv(r)
        if not math.isfinite(f):
            break
        h = 1e-6
        deriv = (npv(r + h) - f) / h
        if abs(deriv) < 1e-12:
            break
        nxt = r - f / deriv
        if not math.isfinite(nxt) or nxt <= -0.9999:
            break
        if abs(nxt - r) < 1e-10:
            return round(nxt * 100, 3)
        r = nxt

    lo, hi = -0.9999, 10.0
    flo = npv(lo)
    if not math.isfinite(flo):
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        fm = npv(mid)
        if not math.isfinite(fm):
            return None
        if abs(fm) < 1e-9:
            return round(mid * 100, 3)
        if (flo < 0) == (fm < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return round(((lo + hi) / 2) * 100, 3)


def twr(values: list[tuple[str, float]], flows: dict[str, float]) -> float | None:
    """
    Time-Weighted Return: concatena i rendimenti dei sotto-periodi tra un
    versamento e l'altro, neutralizzando l'effetto del timing dei versamenti.
    values: [(data, valore portafoglio a fine giornata)]
    flows : {data: cashflow netto entrato quel giorno (positivo = versamento)}
    """
    if len(values) < 2:
        return None
    growth = 1.0
    for (d0, v0), (d1, v1) in zip(values, values[1:]):
        cf = flows.get(d1, 0.0)
        base = v0 + cf
        if base <= 0:
            continue
        growth *= v1 / base
    return round((growth - 1.0) * 100, 3)


def annualize(total_pct: float | None, days: int) -> float | None:
    if total_pct is None or days < 30:
        return None
    yrs = days / 365.0
    base = 1.0 + total_pct / 100.0
    if base <= 0:
        return None
    return round((base ** (1.0 / yrs) - 1.0) * 100, 3)


# ------------------------------------------------------------------ posizioni

def build_positions(tx: list[dict[str, Any]], method: str) -> dict[str, Any]:
    """Costo di carico con metodo medio ponderato, LIFO o FIFO."""
    pos: dict[str, Any] = {}
    for t in tx:
        key = t["ticker"] or t["isin"]
        if not key or t["type"] not in BUY_TYPES | SELL_TYPES:
            continue
        p = pos.setdefault(key, {
            "ticker": t["ticker"], "isin": t["isin"], "name": t["name"],
            "qty": 0.0, "cost": 0.0, "lots": [], "realized_gain": 0.0,
            "realized_loss": 0.0, "fees": 0.0, "n_buy": 0, "n_sell": 0,
            "first_date": t["date"], "last_date": t["date"],
        })
        p["name"] = p["name"] or t["name"]
        p["last_date"] = t["date"]
        p["fees"] += t["fees"]

        if t["type"] in BUY_TYPES:
            if t["qty"] <= 0:
                continue
            unit = (abs(t["amount"]) / t["qty"]) if t["amount"] else t["price"]
            p["qty"] += t["qty"]
            p["cost"] += t["qty"] * unit
            p["lots"].append({"date": t["date"], "qty": t["qty"], "unit": unit})
            p["n_buy"] += 1
        else:
            q = t["qty"] if t["qty"] > 0 else (abs(t["amount"]) / t["price"] if t["price"] else 0)
            if q <= 0:
                continue
            proceeds = abs(t["amount"]) if t["amount"] else q * t["price"] - t["fees"]
            unit_sell = proceeds / q
            remaining, basis = q, 0.0
            if method == "average":
                avg = p["cost"] / p["qty"] if p["qty"] > 0 else 0.0
                take = min(q, p["qty"])
                basis = take * avg
                p["cost"] -= basis
                p["qty"] -= take
                remaining -= take          # <-- senza questo la plus/minus era sempre = -basis
                p["lots"] = [{"date": p["first_date"], "qty": p["qty"], "unit": avg}] if p["qty"] > 0 else []
            else:
                order = reversed(p["lots"]) if method == "lifo" else iter(list(p["lots"]))
                keep = []
                consumed = []
                for lot in order:
                    if remaining <= 1e-12:
                        keep.append(lot)
                        continue
                    take = min(lot["qty"], remaining)
                    basis += take * lot["unit"]
                    remaining -= take
                    lot = {**lot, "qty": lot["qty"] - take}
                    consumed.append(lot)
                    if lot["qty"] > 1e-12:
                        keep.append(lot)
                rest = [l for l in (consumed + keep) if l["qty"] > 1e-12]
                rest.sort(key=lambda l: l["date"])
                p["lots"] = rest
                p["qty"] = sum(l["qty"] for l in rest)
                p["cost"] = sum(l["qty"] * l["unit"] for l in rest)
            pnl = (unit_sell * (q - remaining)) - basis
            if pnl >= 0:
                p["realized_gain"] += pnl
            else:
                p["realized_loss"] += -pnl
            p["n_sell"] += 1
    return pos


# ------------------------------------------------------------------ analisi

def analyze(tx, cfg, hist, cur) -> dict[str, Any]:
    if not tx:
        return {"error": "nessuna transazione: compila pac/transactions.csv"}

    today = datetime.now(timezone.utc).date().isoformat()
    method = cfg.get("lot_method", "average")
    pos = build_positions(tx, method)
    targets = {(p.get("ticker") or p.get("isin", "")).upper(): p
               for p in cfg.get("positions", [])}

    # --- valorizzazione ---
    holdings, tot_val, tot_cost = [], 0.0, 0.0
    missing_px = []
    for key, p in pos.items():
        if p["qty"] <= 1e-9:
            continue
        tk = (p["ticker"] or key).upper()
        px = cur.get(tk)
        if px is None:
            missing_px.append(tk)
        val = p["qty"] * px if px else None
        avg = p["cost"] / p["qty"] if p["qty"] else 0.0
        meta = targets.get(tk, {})
        h = {
            "ticker": tk, "isin": p["isin"],
            "name": meta.get("name") or p["name"] or tk,
            "quantita": round(p["qty"], 6),
            "prezzo_medio_carico": round(avg, 4),
            "prezzo_corrente": px,
            "costo_totale": round(p["cost"], 2),
            "valore_corrente": round(val, 2) if val is not None else None,
            "pl_latente": round(val - p["cost"], 2) if val is not None else None,
            "pl_latente_pct": round((val / p["cost"] - 1) * 100, 2) if val and p["cost"] > 0 else None,
            "plus_realizzate": round(p["realized_gain"], 2),
            "minus_realizzate": round(p["realized_loss"], 2),
            "commissioni": round(p["fees"], 2),
            "n_acquisti": p["n_buy"], "n_vendite": p["n_sell"],
            "primo_acquisto": p["first_date"],
            "target_weight_pct": round(meta.get("target_weight", 0) * 100, 2) if meta.get("target_weight") else None,
            "ter_pct": meta.get("ter_pct"),
            "tipo": meta.get("type", "ETF_UCITS"),
        }
        holdings.append(h)
        tot_cost += p["cost"]
        if val:
            tot_val += val
    holdings.sort(key=lambda x: -(x["valore_corrente"] or 0))

    for h in holdings:
        h["peso_attuale_pct"] = round((h["valore_corrente"] or 0) / tot_val * 100, 2) if tot_val else None

    # --- cashflow per XIRR ---
    flows: list[tuple[str, float]] = []
    by_day: dict[str, float] = defaultdict(float)
    versato = incassato = commissioni = 0.0
    for t in tx:
        if t["type"] in BUY_TYPES:
            a = abs(t["amount"])
            flows.append((t["date"], -a)); by_day[t["date"]] += a
            versato += a
        elif t["type"] in SELL_TYPES:
            a = abs(t["amount"])
            flows.append((t["date"], a)); by_day[t["date"]] -= a
            incassato += a
        elif t["type"] in INCOME_TYPES:
            a = abs(t["amount"])
            flows.append((t["date"], a))
            incassato += a
        elif t["type"] in ("FEE", "TAX", "BOLLO"):
            commissioni += abs(t["amount"])
            flows.append((t["date"], -abs(t["amount"])))
    if tot_val > 0:
        flows.append((today, tot_val))
    flows.sort(key=lambda f: f[0])

    mwr = xirr(flows)
    giorni = (date.fromisoformat(today) - date.fromisoformat(tx[0]["date"])).days
    capitale_netto = versato - incassato
    pl_tot = tot_val - capitale_netto
    pl_pct = (pl_tot / capitale_netto * 100) if capitale_netto > 0 else None

    # --- TWR: serie giornaliera del valore di portafoglio ---
    # I cashflow vanno agganciati al giorno di BORSA in cui la posizione compare
    # nella valorizzazione, non alla data nominale dell'ordine: un PAC eseguito
    # di sabato entra in valorizzazione il lunedi'. Senza questo allineamento il
    # versamento verrebbe letto come rendimento e il TWR risulterebbe gonfiato.
    twr_pct = None
    curve: list[dict[str, Any]] = []
    all_days = sorted({dt for s in hist.values() for dt in s if dt >= tx[0]["date"]})
    if all_days:
        run: dict[str, float] = defaultdict(float)
        ti = 0
        vals: list[tuple[str, float]] = []
        flows_on_valuation_day: dict[str, float] = defaultdict(float)
        for day in all_days:
            while ti < len(tx) and tx[ti]["date"] <= day:
                t = tx[ti]
                k = (t["ticker"] or t["isin"]).upper()
                if t["type"] in BUY_TYPES:
                    run[k] += t["qty"]
                    flows_on_valuation_day[day] += abs(t["amount"])
                elif t["type"] in SELL_TYPES:
                    run[k] -= t["qty"]
                    flows_on_valuation_day[day] -= abs(t["amount"])
                ti += 1
            v = 0.0
            for k, q in run.items():
                px = price_on(hist, k, day)
                if px and q > 0:
                    v += q * px
            if v > 0:
                vals.append((day, round(v, 2)))
        if len(vals) >= 2:
            twr_pct = twr(vals, flows_on_valuation_day)
            step = max(1, len(vals) // 120)
            curve = [{"date": dd, "valore": vv} for dd, vv in vals[::step]]
            if curve and curve[-1]["date"] != vals[-1][0]:
                curve.append({"date": vals[-1][0], "valore": vals[-1][1]})

    # --- benchmark con gli STESSI versamenti ---
    bench = None
    btk = (cfg.get("benchmark", {}).get("ticker") or "").upper()
    if btk and hist.get(btk):
        units, invested = 0.0, 0.0
        for t in tx:
            if t["type"] in BUY_TYPES:
                px = price_on(hist, btk, t["date"])
                if px:
                    units += abs(t["amount"]) / px
                    invested += abs(t["amount"])
        bpx = cur.get(btk) or price_on(hist, btk, today)
        if units > 0 and bpx:
            bval = units * bpx
            bflows = [(t["date"], -abs(t["amount"])) for t in tx if t["type"] in BUY_TYPES]
            bflows.append((today, bval))
            bench = {
                "ticker": btk, "nome": cfg["benchmark"].get("name", btk),
                "quote_teoriche": round(units, 4),
                "capitale_investito": round(invested, 2),
                "valore_teorico": round(bval, 2),
                "pl": round(bval - invested, 2),
                "pl_pct": round((bval / invested - 1) * 100, 2) if invested else None,
                "mwr_pct": xirr(sorted(bflows, key=lambda f: f[0])),
            }
            if bench["pl_pct"] is not None and pl_pct is not None:
                bench["extra_rendimento_pp"] = round(pl_pct - bench["pl_pct"], 2)

    # --- drift e ribilanciamento senza vendere ---
    drift, reb = [], None
    if tot_val > 0 and targets:
        tot_target = sum(m.get("target_weight", 0) for m in targets.values())
        for tk, m in targets.items():
            tw = m.get("target_weight")
            if not tw:
                continue
            tw = tw / tot_target if tot_target > 0 else tw
            h = next((x for x in holdings if x["ticker"] == tk), None)
            cw = (h["valore_corrente"] or 0) / tot_val if h else 0.0
            drift.append({
                "ticker": tk, "nome": m.get("name", tk),
                "peso_target_pct": round(tw * 100, 2),
                "peso_attuale_pct": round(cw * 100, 2),
                "scostamento_pp": round((cw - tw) * 100, 2),
                "delta_eur_per_riallineare": round((tw - cw) * tot_val, 2),
            })
        drift.sort(key=lambda x: x["scostamento_pp"])
        sotto = [x for x in drift if x["scostamento_pp"] < -0.01]
        if sotto:
            need = sum(-x["scostamento_pp"] for x in sotto)
            reb = {
                "logica": ("Nessuna vendita: le vendite in guadagno pagano il 26%. "
                           "Si riallinea indirizzando i prossimi versamenti sui sottopesati."),
                "ripartizione_prossimo_versamento": [
                    {"ticker": x["ticker"], "nome": x["nome"],
                     "quota_pct": round(-x["scostamento_pp"] / need * 100, 1)}
                    for x in sotto],
                "versamento_per_riallineo_completo_eur": round(
                    max((x["peso_target_pct"] / 100 * tot_val - (x["peso_attuale_pct"] / 100 * tot_val))
                        / max(x["peso_target_pct"] / 100, 1e-9) for x in sotto), 2),
            }

    # --- fisco IT (simulazione) ---
    tax_cfg = cfg["tax"]
    plus_lat = sum(h["pl_latente"] for h in holdings if (h["pl_latente"] or 0) > 0)
    minus_lat = sum(-h["pl_latente"] for h in holdings if (h["pl_latente"] or 0) < 0)
    plus_real = sum(h["plus_realizzate"] for h in holdings)
    minus_real = sum(h["minus_realizzate"] for h in holdings)
    is_crypto = lambda h: (h.get("tipo") or "").upper().startswith("CRYPTO")
    plus_crypto = sum(h["pl_latente"] for h in holdings if is_crypto(h) and (h["pl_latente"] or 0) > 0)
    plus_etf = plus_lat - plus_crypto
    imposta_lat = plus_etf * tax_cfg["capital_gains_pct"] / 100 + \
                  plus_crypto * tax_cfg["crypto_pct"] / 100
    bollo = tot_val * tax_cfg["stamp_duty_pct"] / 100
    ter = sum((h["valore_corrente"] or 0) * (h.get("ter_pct") or 0) / 100 for h in holdings)

    fisco = {
        "plusvalenze_latenti": round(plus_lat, 2),
        "minusvalenze_latenti": round(minus_lat, 2),
        "plusvalenze_realizzate": round(plus_real, 2),
        "minusvalenze_realizzate": round(minus_real, 2),
        "imposta_stimata_se_liquidassi_tutto": round(imposta_lat, 2),
        "netto_dopo_imposte": round(tot_val - imposta_lat, 2),
        "bollo_titoli_annuo_stimato": round(bollo, 2),
        "ter_annuo_stimato": round(ter, 2),
        "costo_annuo_totale_stimato": round(bollo + ter, 2),
        "costo_annuo_pct_su_patrimonio": round((bollo + ter) / tot_val * 100, 3) if tot_val else None,
        "avvertenza_asimmetria_etf": (
            "Su ETF UCITS le plusvalenze sono redditi di CAPITALE, le minusvalenze "
            "sono redditi DIVERSI: una minus su ETF NON compensa una plus su ETF. "
            "Le minus da ETF si recuperano solo con plus da azioni singole, ETC/ETN, "
            "obbligazioni, certificati o derivati, entro 4 anni."),
        "metodo_lotti_usato": method,
        "disclaimer": ("Simulazione. In regime amministrato il calcolo ufficiale lo fa "
                       "Trade Republic come sostituto d'imposta: il suo report prevale."),
    }

    # --- ritmo del PAC ---
    buys = [t for t in tx if t["type"] in BUY_TYPES]
    mesi: dict[str, float] = defaultdict(float)
    per_data: dict[str, float] = defaultdict(float)
    for t in buys:
        mesi[t["date"][:7]] += abs(t["amount"])
        per_data[t["date"]] += abs(t["amount"])
    ritmo = {
        "n_ordini": len(buys),
        "n_versamenti": len(per_data),
        "primo": buys[0]["date"] if buys else None,
        "ultimo": buys[-1]["date"] if buys else None,
        "mesi_attivi": len(mesi),
        "versamento_medio": round(versato / len(per_data), 2) if per_data else None,
        "versato_per_mese": {k: round(v, 2) for k, v in sorted(mesi.items())},
        "media_mensile": round(sum(mesi.values()) / len(mesi), 2) if mesi else None,
    }

    return {
        "generato_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "avvertenze": (["prezzo corrente mancante per: " + ", ".join(sorted(set(missing_px)))]
                       if missing_px else []),
        "sintesi": {
            "capitale_versato": round(versato, 2),
            "incassato_da_vendite_e_cedole": round(incassato, 2),
            "capitale_netto_investito": round(capitale_netto, 2),
            "valore_corrente": round(tot_val, 2),
            "pl_totale": round(pl_tot, 2),
            "pl_totale_pct": round(pl_pct, 2) if pl_pct is not None else None,
            "mwr_xirr_annuo_pct": mwr,
            "twr_periodo_pct": twr_pct,
            "twr_annualizzato_pct": annualize(twr_pct, giorni),
            "giorni_investito": giorni,
            "commissioni_totali": round(commissioni + sum(h["commissioni"] for h in holdings), 2),
        },
        "posizioni": holdings,
        "benchmark": bench,
        "drift": drift,
        "ribilanciamento_senza_vendere": reb,
        "fisco": fisco,
        "ritmo_pac": ritmo,
        "curva_valore": curve,
    }


# ------------------------------------------------------------------ report

def to_markdown(a: dict[str, Any]) -> str:
    if "error" in a:
        return f"# Report PAC\n\n**{a['error']}**\n"
    s = a["sintesi"]
    L = ["# Report PAC — Trade Republic\n",
         f"Generato: `{a['generato_utc']}`\n"]
    for w in a.get("avvertenze", []):
        L.append(f"> ATTENZIONE: {w}\n")

    L += ["\n## Sintesi\n",
          "| Voce | Valore |", "|---|--:|",
          f"| Capitale versato | {fmt(s['capitale_versato'],' €')} |",
          f"| Capitale netto investito | {fmt(s['capitale_netto_investito'],' €')} |",
          f"| Valore corrente | **{fmt(s['valore_corrente'],' €')}** |",
          f"| P&L totale | **{fmt(s['pl_totale'],' €')}** ({fmt(s['pl_totale_pct'],'%')}) |",
          f"| MWR / XIRR annuo | **{fmt(s['mwr_xirr_annuo_pct'],'%')}** |",
          f"| TWR di periodo | {fmt(s['twr_periodo_pct'],'%')} |",
          f"| TWR annualizzato | {fmt(s['twr_annualizzato_pct'],'%')} |",
          f"| Giorni investito | {s['giorni_investito']} |",
          f"| Commissioni totali | {fmt(s['commissioni_totali'],' €')} |",
          "\n*MWR pesa **quando** hai versato (il tuo rendimento reale). "
          "TWR ignora il timing e misura **lo strumento** (confrontabile con un indice).*\n"]

    if a["posizioni"]:
        L += ["\n## Posizioni\n",
              "| Strumento | Qta | PMC | Prezzo | Valore | P&L | P&L % | Peso | Target |",
              "|---|--:|--:|--:|--:|--:|--:|--:|--:|"]
        for h in a["posizioni"]:
            L.append(f"| {h['name']} | {fmt(h['quantita'],'',4)} | {fmt(h['prezzo_medio_carico'],'',4)} "
                     f"| {fmt(h['prezzo_corrente'],'',4)} | {fmt(h['valore_corrente'],' €')} "
                     f"| {fmt(h['pl_latente'],' €')} | {fmt(h['pl_latente_pct'],'%')} "
                     f"| {fmt(h['peso_attuale_pct'],'%')} | {fmt(h['target_weight_pct'],'%')} |")

    if a.get("benchmark"):
        b = a["benchmark"]
        L += [f"\n## Confronto con il benchmark ({b['nome']})\n",
              "Stessi importi, stesse date, un solo ETF.\n",
              "| | Il tuo PAC | Benchmark |", "|---|--:|--:|",
              f"| Valore | {fmt(s['valore_corrente'],' €')} | {fmt(b['valore_teorico'],' €')} |",
              f"| P&L % | {fmt(s['pl_totale_pct'],'%')} | {fmt(b['pl_pct'],'%')} |",
              f"| MWR annuo | {fmt(s['mwr_xirr_annuo_pct'],'%')} | {fmt(b['mwr_pct'],'%')} |"]
        e = b.get("extra_rendimento_pp")
        if e is not None:
            verdetto = "il tuo mix BATTE il benchmark" if e > 0 else "il benchmark ti batte"
            L.append(f"\n**Differenza: {fmt(e,' pp')}** — {verdetto}.\n")

    if a.get("drift"):
        L += ["\n## Scostamento dai pesi target\n",
              "| Strumento | Target | Attuale | Scost. | Da spostare |",
              "|---|--:|--:|--:|--:|"]
        for x in a["drift"]:
            L.append(f"| {x['nome']} | {fmt(x['peso_target_pct'],'%')} | {fmt(x['peso_attuale_pct'],'%')} "
                     f"| {fmt(x['scostamento_pp'],' pp')} | {fmt(x['delta_eur_per_riallineare'],' €')} |")
    if a.get("ribilanciamento_senza_vendere"):
        r = a["ribilanciamento_senza_vendere"]
        L += ["\n### Come riallinearti senza vendere\n", f"{r['logica']}\n",
              "| Strumento | Quota del prossimo versamento |", "|---|--:|"]
        for x in r["ripartizione_prossimo_versamento"]:
            L.append(f"| {x['nome']} | **{fmt(x['quota_pct'],'%',1)}** |")

    f = a["fisco"]
    L += ["\n## Fisco e costi (simulazione Italia)\n",
          "| Voce | Importo |", "|---|--:|",
          f"| Plusvalenze latenti | {fmt(f['plusvalenze_latenti'],' €')} |",
          f"| Minusvalenze latenti | {fmt(f['minusvalenze_latenti'],' €')} |",
          f"| Imposta se liquidassi tutto | **{fmt(f['imposta_stimata_se_liquidassi_tutto'],' €')}** |",
          f"| Netto dopo imposte | {fmt(f['netto_dopo_imposte'],' €')} |",
          f"| Bollo titoli annuo (0,2%) | {fmt(f['bollo_titoli_annuo_stimato'],' €')} |",
          f"| TER annuo stimato | {fmt(f['ter_annuo_stimato'],' €')} |",
          f"| **Costo annuo totale** | **{fmt(f['costo_annuo_totale_stimato'],' €')}** "
          f"({fmt(f['costo_annuo_pct_su_patrimonio'],'%',3)}) |",
          f"\n> {f['avvertenza_asimmetria_etf']}\n", f"> {f['disclaimer']}\n"]

    r = a["ritmo_pac"]
    L += ["\n## Ritmo del PAC\n",
          f"- Versamenti: **{r['n_versamenti']}** ({r['n_ordini']} ordini) su **{r['mesi_attivi']}** mesi",
          f"- Versamento medio: **{fmt(r['versamento_medio'],' €')}**",
          f"- Media mensile: **{fmt(r['media_mensile'],' €')}**",
          f"- Periodo: {r['primo']} -> {r['ultimo']}\n"]

    L.append("\n---\n*Strumento di analisi personale. Non e' consulenza finanziaria.*\n")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-only", action="store_true")
    args = ap.parse_args()

    cfg = load_config()
    tx = load_transactions()
    hist, cur = load_prices()
    a = analyze(tx, cfg, hist, cur)

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, "pac_report.json"), "w", encoding="utf-8") as f:
        json.dump(a, f, ensure_ascii=False, indent=2)
    md = to_markdown(a)
    with open(os.path.join(DATA_DIR, "PAC_REPORT.md"), "w", encoding="utf-8") as f:
        f.write(md)

    if "error" in a:
        print(f"[pac] {a['error']}", file=sys.stderr)
        return 1
    s = a["sintesi"]
    print(f"[pac] versato {s['capitale_versato']:.2f} € | valore {s['valore_corrente']:.2f} € | "
          f"P&L {s['pl_totale']:+.2f} € ({s['pl_totale_pct']:+.2f}%) | MWR {s['mwr_xirr_annuo_pct']}%")
    if not args.json_only:
        print("\n" + md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
