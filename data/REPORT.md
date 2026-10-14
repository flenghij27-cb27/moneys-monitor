# Moneys Monitor - Report di mercato

Generato: `2026-10-14T16:43:54+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-14T16:43:16+00:00` (451 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.72% | 0.00% | **-0.72 pp** |
| 1w | -0.76% | 0.00% | **-0.76 pp** |
| 1m | -1.48% | 0.00% | **-1.48 pp** |
| 3m | 10.55% | 4.57% | **5.98 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | US 5Y Treasury Yield | 0.60% | | Ethereum | -2.70% |
| 3 | VIX (volatilita) | 0.39% | | Solana | -2.44% |
| 4 | US 10Y Treasury Yield | 0.38% | | Bitcoin | -1.85% |
| 5 | USD/JPY | 0.34% | | Dow Jones | -0.35% |
| 6 | Indice dollaro Fed (broad) | 0.18% | | Nasdaq Composite | -0.15% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -3.97% |
| 2 | Petrolio WTI | 5.20% | | GBP/USD | -2.16% |
| 3 | Gas naturale | 4.48% | | Nasdaq Composite | -1.43% |
| 4 | Indice dollaro Fed (broad) | 2.99% | | Ethereum | -1.42% |
| 5 | VIX (volatilita) | 1.73% | | US 5Y Treasury Yield | -0.79% |
| 6 | USD/JPY | 1.43% | | US 10Y Treasury Yield | -0.76% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Solana | -9.10% |
| 2 | Petrolio WTI | 15.44% | | Ethereum | -9.00% |
| 3 | Gas naturale | 10.14% | | VIX (volatilita) | -7.23% |
| 4 | US 10Y Treasury Yield | 5.86% | | Bitcoin | -3.07% |
| 5 | US 5Y Treasury Yield | 5.68% | | EUR/USD | -2.98% |
| 6 | US 30Y Treasury Yield | 4.28% | | GBP/USD | -2.05% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| S&P 500 vs VIX (volatilita) | 0.119 | 2.43% | -7.23% | **9.66 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.036 | 5.86% | 0.00% | **5.86 pp** |
| S&P 500 vs Bitcoin | 0.024 | 2.43% | -3.07% | **5.50 pp** |
| EUR/USD vs Indice dollaro DXY | 0.054 | -2.98% | 0.00% | **-2.98 pp** |
| S&P 500 vs Oro (spot) | 0.285 | 2.43% | 0.00% | **2.43 pp** |
| S&P 500 vs Nasdaq Composite | 0.947 | 2.43% | 3.89% | **-1.46 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.80 | 2026-10-09 | 0.05 |
| US 10Y Treasury Rate | 5.24 | 2026-10-09 | 0.02 |
| US 30Y Treasury Rate | 5.60 | 2026-10-09 | 0.00 |
| Spread 10Y-2Y USA | 0.42 | 2026-10-13 | -0.02 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **44.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.2700 | -7.23% | 92.67% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 104.4293 | -9.10% | 36.21% | -14.47% |
| Ethereum | 2 441.3531 | -9.00% | 26.02% | -11.90% |
| US 5Y Treasury Yield | 5.0200 | 5.68% | 18.54% | -1.96% |
| Bitcoin | 81 811.4802 | -3.07% | 17.47% | -6.86% |
| US 10Y Treasury Yield | 5.2400 | 5.86% | 16.70% | -2.70% |
| Nasdaq Composite | 27 204.3800 | 3.89% | 13.93% | -7.00% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 4.28% | 13.45% | -1.49% |
| Dow Jones | 51 670.1000 | -1.43% | 9.69% | -6.34% |
| S&P 500 | 7 805.4500 | 2.43% | 9.51% | -3.42% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
