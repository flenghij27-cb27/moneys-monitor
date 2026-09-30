# Moneys Monitor - Report di mercato

Generato: `2026-09-30T12:05:28+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-30T12:03:54+00:00` (407 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.04% | 0.00% | **0.04 pp** |
| 1w | -0.47% | 0.00% | **-0.47 pp** |
| 1m | 3.58% | 0.00% | **3.58 pp** |
| 3m | 14.35% | 15.71% | **-1.35 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 13.09% | | Petrolio Brent | -12.16% |
| 2 | US 5Y Treasury Yield | 1.61% | | Petrolio WTI | -9.91% |
| 3 | US 10Y Treasury Yield | 1.35% | | Gas naturale | -2.36% |
| 4 | US 30Y Treasury Yield | 1.28% | | GBP/USD | -0.91% |
| 5 | Indice dollaro Fed (broad) | 0.68% | | Dow Jones | -0.26% |
| 6 | Bitcoin | 0.29% | | EUR/USD | -0.20% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -9.26% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 7.41% | | Solana | -1.79% |
| 4 | US 10Y Treasury Yield | 5.65% | | Nasdaq Composite | -1.64% |
| 5 | US 30Y Treasury Yield | 5.10% | | USD/JPY | -1.28% |
| 6 | US 5Y Treasury Yield | 4.76% | | S&P 500 | -1.21% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | Dow Jones | -4.13% |
| 2 | Petrolio WTI | 23.32% | | EUR/USD | -2.08% |
| 3 | Solana | 17.81% | | GBP/USD | -1.82% |
| 4 | US 5Y Treasury Yield | 15.53% | | S&P 500 | -0.53% |
| 5 | US 10Y Treasury Yield | 12.21% | | USD/JPY | -0.40% |
| 6 | Ethereum | 9.60% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.099 | 12.21% | 0.00% | **12.21 pp** |
| S&P 500 vs Bitcoin | 0.008 | -0.53% | 7.37% | **-7.90 pp** |
| EUR/USD vs Indice dollaro DXY | 0.021 | -2.08% | 0.00% | **-2.08 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | -0.53% | 1.50% | **-2.03 pp** |
| S&P 500 vs VIX (volatilita) | -0.041 | -0.53% | 1.45% | **-1.98 pp** |
| S&P 500 vs Oro (spot) | 0.067 | -0.53% | 0.00% | **-0.53 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.92 | 2026-09-28 | 0.11 |
| US 10Y Treasury Rate | 5.24 | 2026-09-28 | 0.07 |
| US 30Y Treasury Rate | 5.56 | 2026-09-28 | 0.07 |
| Spread 10Y-2Y USA | 0.37 | 2026-09-29 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **32.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.0700 | 1.45% | 110.92% | -31.22% |
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 119.4881 | 17.81% | 59.50% | -13.59% |
| Ethereum | 2 696.0014 | 9.60% | 38.90% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 83 857.5352 | 7.37% | 36.65% | -6.86% |
| US 5Y Treasury Yield | 5.0600 | 15.53% | 19.10% | -1.65% |
| US 10Y Treasury Yield | 5.2400 | 12.21% | 16.61% | -2.70% |
| Nasdaq Composite | 26 797.5400 | 1.50% | 14.85% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.5600 | 7.13% | 13.14% | -1.49% |
| Dow Jones | 51 349.9200 | -4.13% | 11.63% | -5.52% |
| S&P 500 | 7 670.8400 | -0.53% | 11.09% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
