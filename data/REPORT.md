# Moneys Monitor - Report di mercato

Generato: `2026-10-11T19:58:12+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-11T19:57:40+00:00` (442 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.35% | 0.00% | **0.35 pp** |
| 1w | -1.47% | 0.00% | **-1.47 pp** |
| 1m | 0.73% | 0.00% | **0.73 pp** |
| 3m | 12.56% | 6.97% | **5.59 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 2.19% | | US 30Y Treasury Yield | -1.23% |
| 3 | Indice dollaro Fed (broad) | 0.88% | | US 10Y Treasury Yield | -1.14% |
| 4 | Dow Jones | 0.83% | | US 5Y Treasury Yield | -0.80% |
| 5 | Ethereum | 0.80% | | GBP/USD | -0.12% |
| 6 | Solana | 0.78% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -8.05% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -6.08% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -5.98% |
| 4 | Indice dollaro Fed (broad) | 2.22% | | Bitcoin | -2.39% |
| 5 | S&P 500 | 1.15% | | GBP/USD | -2.37% |
| 6 | Dow Jones | 0.93% | | USD/JPY | -1.35% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Ethereum | -3.96% |
| 2 | Petrolio WTI | 15.44% | | EUR/USD | -3.53% |
| 3 | Gas naturale | 10.14% | | GBP/USD | -2.02% |
| 4 | US 5Y Treasury Yield | 8.24% | | USD/JPY | -0.95% |
| 5 | US 10Y Treasury Yield | 8.07% | | Dow Jones | -0.79% |
| 6 | VIX (volatilita) | 7.61% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.113 | 8.07% | 0.00% | **8.07 pp** |
| S&P 500 vs VIX (volatilita) | -0.043 | 2.90% | 7.61% | **-4.71 pp** |
| EUR/USD vs Indice dollaro DXY | 0.054 | -3.53% | 0.00% | **-3.53 pp** |
| S&P 500 vs Oro (spot) | -0.195 | 2.90% | 0.00% | **2.90 pp** |
| S&P 500 vs Nasdaq Composite | 0.948 | 2.90% | 4.92% | **-2.02 pp** |
| S&P 500 vs Bitcoin | -0.023 | 2.90% | 2.96% | **-0.06 pp** |
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
| VIX (volatilita) | 15.4100 | 7.61% | 98.66% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 111.2636 | 0.48% | 35.04% | -13.59% |
| Ethereum | 2 533.6915 | -3.96% | 24.77% | -10.76% |
| US 5Y Treasury Yield | 4.9900 | 8.24% | 18.55% | -1.96% |
| Bitcoin | 83 600.2321 | 2.96% | 16.75% | -6.86% |
| US 10Y Treasury Yield | 5.2200 | 8.07% | 16.70% | -2.70% |
| Nasdaq Composite | 27 366.1700 | 4.92% | 14.41% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 6.06% | 13.60% | -1.49% |
| S&P 500 | 7 811.5400 | 2.90% | 9.95% | -3.42% |
| Dow Jones | 51 654.9500 | -0.79% | 9.76% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
