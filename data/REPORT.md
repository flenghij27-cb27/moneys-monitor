# Moneys Monitor - Report di mercato

Generato: `2026-09-09T16:06:25+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-09T16:04:27+00:00` (338 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.06% | 0.00% | **-0.06 pp** |
| 1w | 0.17% | 0.00% | **0.17 pp** |
| 1m | 8.07% | 4.20% | **3.87 pp** |
| 3m | 9.18% | 10.40% | **-1.22 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | USD/JPY | -2.41% |
| 2 | Petrolio Brent | 9.44% | | Dow Jones | -1.18% |
| 3 | Gas naturale | 3.83% | | S&P 500 | -0.58% |
| 4 | VIX (volatilita) | 2.75% | | Indice dollaro Fed (broad) | -0.57% |
| 5 | US 5Y Treasury Yield | 0.44% | | Nasdaq Composite | -0.32% |
| 6 | EUR/USD | 0.33% | | Solana | -0.25% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 5.36% | | USD/JPY | -1.78% |
| 2 | Petrolio WTI | 5.08% | | Bitcoin | -1.29% |
| 3 | Gas naturale | 3.17% | | GBP/USD | -0.93% |
| 4 | Petrolio Brent | 1.73% | | Dow Jones | -0.75% |
| 5 | Ethereum | 1.66% | | S&P 500 | -0.16% |
| 6 | US 5Y Treasury Yield | 1.34% | | FTSE MIB | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 36.48% | | Nikkei 225 | -4.86% |
| 2 | Ethereum | 30.92% | | Shanghai Composite | -2.34% |
| 3 | Bitcoin | 22.37% | | Dow Jones | -1.83% |
| 4 | Petrolio WTI | 21.65% | | Russell 2000 | -1.65% |
| 5 | Petrolio Brent | 20.57% | | FTSE MIB | -1.59% |
| 6 | Gas naturale | 7.77% | | CAC 40 Francia | -1.48% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.011 | -0.97% | 22.37% | **-23.34 pp** |
| S&P 500 vs VIX (volatilita) | -0.055 | -0.97% | 7.45% | **-8.42 pp** |
| S&P 500 vs Oro (spot) | 0.057 | -0.97% | 4.91% | **-5.88 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.137 | 2.09% | 4.91% | **-2.82 pp** |
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
| US 2Y Treasury Rate | 4.37 | 2026-09-04 | 0.03 |
| US 10Y Treasury Rate | 4.78 | 2026-09-04 | 0.01 |
| US 30Y Treasury Rate | 5.24 | 2026-09-04 | -0.01 |
| Spread 10Y-2Y USA | 0.41 | 2026-09-08 | 0.00 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **41.0 bp**, 30Y-10Y **46.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.7200 | 7.45% | 78.83% | -31.03% |
| Ethereum | 2 492.1367 | 30.92% | 56.25% | -5.78% |
| Solana | 103.1540 | 36.48% | 48.34% | -13.59% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 78 629.7441 | 22.37% | 43.93% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 3.49% | 19.64% | -11.21% |
| Oro (spot) | 4 693.0000 | 4.91% | 15.16% | -4.96% |
| US 5Y Treasury Yield | 4.5400 | n/d | 15.08% | -0.66% |
| Nikkei 225 | 65 856.4300 | -4.86% | 12.87% | -12.83% |
| Nasdaq Composite | 26 421.4100 | -0.63% | 11.60% | -7.00% |
| US 10Y Treasury Yield | 4.7800 | 2.09% | 11.07% | -2.70% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| Dow Jones | 52 786.0700 | -1.83% | 9.95% | -2.93% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
