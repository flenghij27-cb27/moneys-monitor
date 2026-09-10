# Moneys Monitor - Report di mercato

Generato: `2026-09-10T15:59:05+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-10T15:58:29+00:00` (341 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.51% | 0.00% | **-0.51 pp** |
| 1w | -0.79% | 0.00% | **-0.79 pp** |
| 1m | 7.23% | 7.01% | **0.22 pp** |
| 3m | 9.41% | 13.53% | **-4.12 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | USD/JPY | -2.41% |
| 2 | Petrolio Brent | 9.44% | | Solana | -1.88% |
| 3 | VIX (volatilita) | 4.71% | | Bitcoin | -1.20% |
| 4 | Gas naturale | 3.83% | | Ethereum | -0.89% |
| 5 | US 5Y Treasury Yield | 0.66% | | Dow Jones | -0.77% |
| 6 | US 10Y Treasury Yield | 0.42% | | Nasdaq Composite | -0.64% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | Solana | -3.67% |
| 2 | Gas naturale | 3.17% | | Bitcoin | -3.25% |
| 3 | US 5Y Treasury Yield | 1.78% | | USD/JPY | -1.78% |
| 4 | Petrolio Brent | 1.73% | | Ethereum | -1.66% |
| 5 | US 10Y Treasury Yield | 1.05% | | GBP/USD | -0.93% |
| 6 | VIX (volatilita) | 0.73% | | Dow Jones | -0.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 29.08% | | Dow Jones | -2.71% |
| 2 | Ethereum | 27.43% | | Shanghai Composite | -2.53% |
| 3 | Petrolio WTI | 21.65% | | Nikkei 225 | -2.38% |
| 4 | Petrolio Brent | 20.57% | | S&P 500 | -2.09% |
| 5 | Bitcoin | 19.44% | | Nasdaq Composite | -2.05% |
| 6 | VIX (volatilita) | 15.35% | | USD/JPY | -1.10% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.006 | -2.09% | 19.44% | **-21.53 pp** |
| S&P 500 vs VIX (volatilita) | -0.066 | -2.09% | 15.35% | **-17.44 pp** |
| S&P 500 vs Oro (spot) | 0.059 | -2.09% | 6.69% | **-8.78 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.136 | 3.43% | 6.69% | **-3.26 pp** |
| EUR/USD vs Indice dollaro DXY | -0.016 | 0.37% | -0.72% | **1.09 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 6.69% | 7.33% | **-0.64 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -2.09% | -2.05% | **-0.04 pp** |

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
| VIX (volatilita) | 16.4600 | 15.35% | 80.09% | -31.03% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 99.5175 | 29.08% | 46.52% | -13.59% |
| Ethereum | 2 438.0728 | 27.43% | 46.02% | -5.78% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 77 164.6444 | 19.44% | 40.26% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| US 5Y Treasury Yield | 4.5700 | n/d | 13.98% | -0.66% |
| Argento (spot) | 68.2900 | 7.33% | 12.06% | -11.21% |
| Nasdaq Composite | 26 253.3400 | -2.05% | 11.76% | -7.00% |
| US 10Y Treasury Yield | 4.8000 | 3.43% | 10.44% | -2.70% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| Dow Jones | 52 380.6600 | -2.71% | 10.23% | -3.62% |
| Hang Seng | 25 511.1000 | 0.16% | 8.68% | -3.43% |
| S&P 500 | 7 636.3600 | -2.09% | 8.16% | -3.42% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
