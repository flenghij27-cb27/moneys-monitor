# Moneys Monitor - Report di mercato

Generato: `2026-11-05T01:40:32+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-05T01:39:59+00:00` (519 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.30% | 0.00% | **0.30 pp** |
| 1w | 0.68% | 0.00% | **0.68 pp** |
| 1m | -1.85% | 0.00% | **-1.85 pp** |
| 3m | -1.91% | 0.00% | **-1.91 pp** |
| 6m | 16.28% | 16.18% | **0.11 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Dow Jones | 3.03% | | Petrolio Brent | -13.05% |
| 2 | Solana | 1.24% | | Gas naturale | -4.71% |
| 3 | US 5Y Treasury Yield | 0.85% | | Petrolio WTI | -3.61% |
| 4 | Nasdaq Composite | 0.83% | | VIX (volatilita) | -1.51% |
| 5 | US 10Y Treasury Yield | 0.81% | | FTSE MIB | 0.00% |
| 6 | EUR/USD | 0.79% | | Euro Stoxx 50 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 18.89% | | Gas naturale | -17.30% |
| 2 | Ethereum | 7.59% | | Petrolio Brent | -6.08% |
| 3 | Bitcoin | 3.82% | | Nasdaq Composite | -3.05% |
| 4 | Petrolio WTI | 3.62% | | US 5Y Treasury Yield | -1.66% |
| 5 | Dow Jones | 1.68% | | S&P 500 | -1.40% |
| 6 | EUR/USD | 1.20% | | US 10Y Treasury Yield | -0.80% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 34.21% | | Solana | -9.03% |
| 2 | Petrolio WTI | 20.92% | | US 5Y Treasury Yield | -6.32% |
| 3 | Petrolio Brent | 20.91% | | US 10Y Treasury Yield | -6.25% |
| 4 | Dow Jones | 3.56% | | Nasdaq Composite | -5.58% |
| 5 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -5.51% |
| 6 | Euro Stoxx 50 | 0.00% | | Gas naturale | -3.77% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.458 | -1.27% | 34.21% | **-35.48 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.010 | -6.25% | 0.00% | **-6.25 pp** |
| S&P 500 vs Nasdaq Composite | 0.815 | -1.27% | -5.58% | **4.31 pp** |
| S&P 500 vs Oro (spot) | -0.015 | -1.27% | 0.00% | **-1.27 pp** |
| S&P 500 vs Bitcoin | 0.111 | -1.27% | -1.98% | **0.71 pp** |
| EUR/USD vs Indice dollaro DXY | -0.128 | -0.02% | 0.00% | **-0.02 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.61 | 2026-11-03 | 0.02 |
| US 10Y Treasury Rate | 4.95 | 2026-11-03 | 0.04 |
| US 30Y Treasury Rate | 5.32 | 2026-11-03 | 0.04 |
| Spread 10Y-2Y USA | 0.32 | 2026-11-04 | -0.02 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **34.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| VIX (volatilita) | 20.8300 | 34.21% | 123.84% | -31.22% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 421.4636 | -0.69% | 36.39% | -19.23% |
| Solana | 95.7765 | -9.03% | 32.46% | -24.92% |
| Bitcoin | 80 486.1844 | -1.98% | 26.45% | -11.51% |
| Nasdaq Composite | 25 372.0100 | -5.58% | 21.15% | -8.82% |
| US 5Y Treasury Yield | 4.7400 | -6.32% | 17.15% | -7.66% |
| US 10Y Treasury Yield | 4.9500 | -6.25% | 16.95% | -7.53% |
| US 30Y Treasury Yield | 5.3200 | -5.51% | 14.50% | -6.88% |
| Dow Jones | 53 356.1200 | 3.56% | 14.22% | -6.34% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| S&P 500 | 7 568.9200 | -1.27% | 13.17% | -3.55% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
