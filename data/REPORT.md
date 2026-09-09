# Moneys Monitor - Report di mercato

Generato: `2026-09-09T23:26:20+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-09T23:25:47+00:00` (339 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.43% | 0.00% | **-0.43 pp** |
| 1w | -0.20% | 0.00% | **-0.20 pp** |
| 1m | 7.60% | 4.20% | **3.40 pp** |
| 3m | 8.71% | 10.40% | **-1.69 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | USD/JPY | -2.41% |
| 2 | Petrolio Brent | 9.44% | | Solana | -1.92% |
| 3 | Gas naturale | 3.83% | | Ethereum | -0.99% |
| 4 | VIX (volatilita) | 2.75% | | Dow Jones | -0.77% |
| 5 | US 5Y Treasury Yield | 0.66% | | S&P 500 | -0.58% |
| 6 | US 10Y Treasury Yield | 0.42% | | Indice dollaro Fed (broad) | -0.57% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 5.36% | | Bitcoin | -1.96% |
| 2 | Petrolio WTI | 5.08% | | USD/JPY | -1.78% |
| 3 | Gas naturale | 3.17% | | GBP/USD | -0.93% |
| 4 | US 5Y Treasury Yield | 1.78% | | Dow Jones | -0.73% |
| 5 | Petrolio Brent | 1.73% | | Solana | -0.38% |
| 6 | US 10Y Treasury Yield | 1.05% | | S&P 500 | -0.16% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 34.20% | | Nikkei 225 | -4.86% |
| 2 | Ethereum | 29.23% | | Dow Jones | -2.71% |
| 3 | Petrolio WTI | 21.65% | | Shanghai Composite | -2.34% |
| 4 | Bitcoin | 21.54% | | Russell 2000 | -1.65% |
| 5 | Petrolio Brent | 20.57% | | FTSE MIB | -1.59% |
| 6 | Gas naturale | 7.77% | | CAC 40 Francia | -1.48% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.005 | -0.97% | 21.54% | **-22.51 pp** |
| S&P 500 vs VIX (volatilita) | -0.055 | -0.97% | 7.45% | **-8.42 pp** |
| S&P 500 vs Oro (spot) | 0.057 | -0.97% | 4.91% | **-5.88 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.008 | 3.43% | 4.91% | **-1.48 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 4.91% | 3.49% | **1.42 pp** |
| EUR/USD vs Indice dollaro DXY | -0.013 | 0.70% | -0.63% | **1.33 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -0.97% | -0.63% | **-0.34 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.39 | 2026-09-08 | 0.02 |
| US 10Y Treasury Rate | 4.80 | 2026-09-08 | 0.02 |
| US 30Y Treasury Rate | 5.25 | 2026-09-08 | 0.01 |
| Spread 10Y-2Y USA | 0.40 | 2026-09-09 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **41.0 bp**, 30Y-10Y **45.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.7200 | 7.45% | 78.83% | -31.03% |
| Ethereum | 2 459.9117 | 29.23% | 56.77% | -5.78% |
| Solana | 101.4278 | 34.20% | 49.49% | -13.59% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 78 100.9553 | 21.54% | 44.16% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 3.49% | 19.64% | -11.21% |
| Oro (spot) | 4 693.0000 | 4.91% | 15.16% | -4.96% |
| US 5Y Treasury Yield | 4.5700 | n/d | 13.98% | -0.66% |
| Nikkei 225 | 65 856.4300 | -4.86% | 12.87% | -12.83% |
| Nasdaq Composite | 26 421.4100 | -0.63% | 11.60% | -7.00% |
| US 10Y Treasury Yield | 4.8000 | 3.43% | 10.44% | -2.70% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| Dow Jones | 52 380.6600 | -2.71% | 10.23% | -3.62% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
