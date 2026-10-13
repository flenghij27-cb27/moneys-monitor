# Moneys Monitor - Report di mercato

Generato: `2026-10-13T13:44:24+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-13T13:43:48+00:00` (447 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.17% | 0.00% | **0.17 pp** |
| 1w | 0.05% | 0.00% | **0.05 pp** |
| 1m | -1.61% | 0.00% | **-1.61 pp** |
| 3m | 11.07% | 7.11% | **3.96 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 2.49% | | US 30Y Treasury Yield | -1.23% |
| 3 | Bitcoin | 1.04% | | US 10Y Treasury Yield | -1.14% |
| 4 | Ethereum | 0.98% | | US 5Y Treasury Yield | -0.80% |
| 5 | Indice dollaro Fed (broad) | 0.88% | | Nasdaq Composite | -0.44% |
| 6 | USD/JPY | 0.40% | | EUR/USD | -0.22% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -2.59% |
| 2 | Petrolio WTI | 5.20% | | GBP/USD | -2.37% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -2.00% |
| 4 | Indice dollaro Fed (broad) | 2.22% | | USD/JPY | -1.35% |
| 5 | Bitcoin | 2.02% | | Nasdaq Composite | -0.84% |
| 6 | Ethereum | 1.48% | | US 5Y Treasury Yield | -0.40% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Solana | -9.61% |
| 2 | Petrolio WTI | 15.44% | | Ethereum | -8.76% |
| 3 | Gas naturale | 10.14% | | EUR/USD | -3.55% |
| 4 | US 5Y Treasury Yield | 8.24% | | VIX (volatilita) | -3.24% |
| 5 | US 10Y Treasury Yield | 8.07% | | Bitcoin | -3.20% |
| 6 | US 30Y Treasury Yield | 6.06% | | GBP/USD | -2.02% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.036 | 8.07% | 0.00% | **8.07 pp** |
| S&P 500 vs VIX (volatilita) | 0.119 | 1.96% | -3.24% | **5.20 pp** |
| S&P 500 vs Bitcoin | 0.023 | 1.96% | -3.20% | **5.16 pp** |
| EUR/USD vs Indice dollaro DXY | 0.006 | -3.55% | 0.00% | **-3.55 pp** |
| S&P 500 vs Oro (spot) | 0.285 | 1.96% | 0.00% | **1.96 pp** |
| S&P 500 vs Nasdaq Composite | 0.947 | 1.96% | 3.47% | **-1.51 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.75 | 2026-10-08 | -0.02 |
| US 10Y Treasury Rate | 5.22 | 2026-10-08 | -0.06 |
| US 30Y Treasury Rate | 5.60 | 2026-10-08 | -0.07 |
| Spread 10Y-2Y USA | 0.44 | 2026-10-09 | -0.03 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.2100 | -3.24% | 98.01% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 106.9337 | -9.61% | 36.41% | -13.59% |
| Ethereum | 2 509.4122 | -8.76% | 24.72% | -10.76% |
| US 5Y Treasury Yield | 4.9900 | 8.24% | 18.55% | -1.96% |
| US 10Y Treasury Yield | 5.2200 | 8.07% | 16.70% | -2.70% |
| Bitcoin | 83 368.4388 | -3.20% | 16.29% | -6.86% |
| Nasdaq Composite | 27 245.9000 | 3.47% | 14.33% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 6.06% | 13.60% | -1.49% |
| Dow Jones | 51 850.5500 | -1.37% | 9.86% | -6.34% |
| S&P 500 | 7 807.2400 | 1.96% | 9.73% | -3.42% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
