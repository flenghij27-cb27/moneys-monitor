# Moneys Monitor - Report di mercato

Generato: `2026-09-29T12:18:45+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-29T12:18:17+00:00` (404 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.32% | 0.00% | **0.32 pp** |
| 1w | 0.25% | 0.00% | **0.25 pp** |
| 1m | 3.44% | 0.00% | **3.44 pp** |
| 3m | 15.31% | 15.61% | **-0.29 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Ethereum | 2.10% | | Petrolio Brent | -12.16% |
| 2 | Solana | 1.68% | | Petrolio WTI | -9.91% |
| 3 | Bitcoin | 1.09% | | VIX (volatilita) | -4.44% |
| 4 | Indice dollaro Fed (broad) | 0.68% | | Gas naturale | -2.36% |
| 5 | US 30Y Treasury Yield | 0.37% | | US 5Y Treasury Yield | -0.99% |
| 6 | USD/JPY | 0.20% | | Nasdaq Composite | -0.92% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -17.38% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 7.41% | | USD/JPY | -1.28% |
| 4 | US 10Y Treasury Yield | 3.19% | | Nasdaq Composite | -1.11% |
| 5 | US 30Y Treasury Yield | 2.81% | | Dow Jones | -1.09% |
| 6 | Solana | 2.79% | | S&P 500 | -1.04% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | VIX (volatilita) | -6.08% |
| 2 | Petrolio WTI | 23.32% | | Dow Jones | -3.90% |
| 3 | Solana | 16.30% | | EUR/USD | -2.28% |
| 4 | US 5Y Treasury Yield | 13.96% | | GBP/USD | -1.82% |
| 5 | US 10Y Treasury Yield | 10.94% | | S&P 500 | -0.61% |
| 6 | Ethereum | 10.17% | | USD/JPY | -0.40% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.098 | 10.94% | 0.00% | **10.94 pp** |
| S&P 500 vs Bitcoin | 0.001 | -0.61% | 7.51% | **-8.12 pp** |
| S&P 500 vs VIX (volatilita) | -0.033 | -0.61% | -6.08% | **5.47 pp** |
| EUR/USD vs Indice dollaro DXY | 0.023 | -2.28% | 0.00% | **-2.28 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | -0.61% | 1.05% | **-1.66 pp** |
| S&P 500 vs Oro (spot) | 0.067 | -0.61% | 0.00% | **-0.61 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.81 | 2026-09-25 | -0.06 |
| US 10Y Treasury Rate | 5.17 | 2026-09-25 | -0.01 |
| US 30Y Treasury Rate | 5.49 | 2026-09-25 | 0.02 |
| Spread 10Y-2Y USA | 0.32 | 2026-09-28 | -0.04 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **36.0 bp**, 30Y-10Y **32.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| VIX (volatilita) | 14.2100 | -6.08% | 100.28% | -31.22% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 120.2726 | 16.30% | 60.78% | -13.59% |
| Ethereum | 2 737.0982 | 10.17% | 39.60% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 84 343.3953 | 7.51% | 37.64% | -6.86% |
| US 5Y Treasury Yield | 4.9800 | 13.96% | 19.71% | -1.65% |
| US 10Y Treasury Yield | 5.1700 | 10.94% | 16.57% | -2.70% |
| Nasdaq Composite | 26 820.3800 | 1.05% | 14.86% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.4900 | 5.98% | 12.70% | -1.49% |
| Dow Jones | 51 481.5100 | -3.90% | 11.78% | -5.52% |
| S&P 500 | 7 683.6900 | -0.61% | 11.14% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
