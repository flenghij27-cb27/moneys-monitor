# Moneys Monitor - Report di mercato

Generato: `2026-10-12T22:46:16+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-12T22:45:39+00:00` (445 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.60% | 0.00% | **-0.60 pp** |
| 1w | -1.08% | 0.00% | **-1.08 pp** |
| 1m | -1.72% | 0.00% | **-1.72 pp** |
| 3m | 11.04% | 7.11% | **3.93 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | Indice dollaro Fed (broad) | 0.88% | | Solana | -4.04% |
| 3 | Nasdaq Composite | 0.64% | | VIX (volatilita) | -3.70% |
| 4 | S&P 500 | 0.59% | | Ethereum | -1.92% |
| 5 | USD/JPY | 0.40% | | Bitcoin | -1.30% |
| 6 | Dow Jones | 0.38% | | US 30Y Treasury Yield | -1.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -8.08% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -3.43% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -3.07% |
| 4 | Indice dollaro Fed (broad) | 2.22% | | GBP/USD | -2.37% |
| 5 | S&P 500 | 1.15% | | USD/JPY | -1.35% |
| 6 | Dow Jones | 1.14% | | Bitcoin | -1.05% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Ethereum | -10.32% |
| 2 | Petrolio WTI | 15.44% | | Solana | -9.89% |
| 3 | Gas naturale | 10.14% | | Bitcoin | -4.85% |
| 4 | US 5Y Treasury Yield | 8.24% | | EUR/USD | -3.55% |
| 5 | US 10Y Treasury Yield | 8.07% | | VIX (volatilita) | -3.01% |
| 6 | US 30Y Treasury Yield | 6.06% | | GBP/USD | -2.02% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.104 | 8.07% | 0.00% | **8.07 pp** |
| S&P 500 vs Bitcoin | 0.024 | 2.90% | -4.85% | **7.75 pp** |
| S&P 500 vs VIX (volatilita) | 0.120 | 2.90% | -3.01% | **5.91 pp** |
| EUR/USD vs Indice dollaro DXY | 0.053 | -3.55% | 0.00% | **-3.55 pp** |
| S&P 500 vs Oro (spot) | 0.285 | 2.90% | 0.00% | **2.90 pp** |
| S&P 500 vs Nasdaq Composite | 0.948 | 2.90% | 4.92% | **-2.02 pp** |
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
| VIX (volatilita) | 14.8400 | -3.01% | 99.13% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 106.7701 | -9.89% | 37.47% | -13.59% |
| Ethereum | 2 485.0289 | -10.32% | 25.31% | -10.76% |
| US 5Y Treasury Yield | 4.9900 | 8.24% | 18.55% | -1.96% |
| Bitcoin | 82 511.2606 | -4.85% | 17.14% | -6.86% |
| US 10Y Treasury Yield | 5.2200 | 8.07% | 16.70% | -2.70% |
| Nasdaq Composite | 27 366.1700 | 4.92% | 14.41% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 6.06% | 13.60% | -1.49% |
| S&P 500 | 7 811.5400 | 2.90% | 9.95% | -3.42% |
| Dow Jones | 51 850.5500 | -1.37% | 9.86% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
