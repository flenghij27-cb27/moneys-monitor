# Moneys Monitor - Report di mercato

Generato: `2026-10-09T01:20:17+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-09T01:19:39+00:00` (434 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.18% | 0.00% | **-0.18 pp** |
| 1w | -1.94% | 0.00% | **-1.94 pp** |
| 1m | -0.27% | 0.00% | **-0.27 pp** |
| 3m | 11.13% | 9.38% | **1.75 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | Indice dollaro Fed (broad) | 0.88% | | Solana | -0.87% |
| 3 | US 30Y Treasury Yield | 0.53% | | S&P 500 | -0.47% |
| 4 | VIX (volatilita) | 0.47% | | Nasdaq Composite | -0.22% |
| 5 | USD/JPY | 0.40% | | Bitcoin | -0.14% |
| 6 | US 10Y Treasury Yield | 0.19% | | GBP/USD | -0.12% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -10.49% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -8.47% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -7.71% |
| 4 | Nasdaq Composite | 2.52% | | Bitcoin | -4.29% |
| 5 | Indice dollaro Fed (broad) | 2.22% | | GBP/USD | -2.37% |
| 6 | S&P 500 | 1.29% | | USD/JPY | -1.35% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Ethereum | -5.49% |
| 2 | Petrolio WTI | 15.44% | | EUR/USD | -4.00% |
| 3 | Gas naturale | 10.14% | | Solana | -3.82% |
| 4 | US 5Y Treasury Yield | 10.07% | | Dow Jones | -2.19% |
| 5 | US 10Y Treasury Yield | 10.00% | | GBP/USD | -2.02% |
| 6 | US 30Y Treasury Yield | 8.00% | | USD/JPY | -0.95% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.028 | 10.00% | 0.00% | **10.00 pp** |
| EUR/USD vs Indice dollaro DXY | -0.072 | -4.00% | 0.00% | **-4.00 pp** |
| S&P 500 vs Nasdaq Composite | 0.128 | 1.69% | 4.23% | **-2.54 pp** |
| S&P 500 vs VIX (volatilita) | -0.047 | 1.69% | -0.79% | **2.48 pp** |
| S&P 500 vs Oro (spot) | -0.156 | 1.69% | 0.00% | **1.69 pp** |
| S&P 500 vs Bitcoin | -0.084 | 1.69% | 0.73% | **0.96 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.77 | 2026-10-07 | -0.02 |
| US 10Y Treasury Rate | 5.28 | 2026-10-07 | 0.01 |
| US 30Y Treasury Rate | 5.67 | 2026-10-07 | 0.03 |
| Spread 10Y-2Y USA | 0.47 | 2026-10-08 | -0.04 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **51.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.0800 | -0.79% | 101.25% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 108.8198 | -3.82% | 43.13% | -13.59% |
| Ethereum | 2 470.9974 | -5.49% | 30.61% | -10.83% |
| Bitcoin | 81 605.4076 | 0.73% | 29.63% | -6.86% |
| US 5Y Treasury Yield | 5.0300 | 10.07% | 20.56% | -1.65% |
| US 10Y Treasury Yield | 5.2800 | 10.00% | 17.58% | -2.70% |
| Nasdaq Composite | 27 538.6900 | 4.23% | 13.93% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6700 | 8.00% | 13.45% | -1.49% |
| S&P 500 | 7 765.3600 | 1.69% | 10.17% | -3.42% |
| Dow Jones | 51 231.6400 | -2.19% | 9.96% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
