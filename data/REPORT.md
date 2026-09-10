# Moneys Monitor - Report di mercato

Generato: `2026-09-10T23:20:24+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-10T23:19:48+00:00` (343 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.62% | 0.00% | **-0.62 pp** |
| 1w | -0.90% | 0.00% | **-0.90 pp** |
| 1m | 7.08% | 7.01% | **0.07 pp** |
| 3m | 9.27% | 13.53% | **-4.26 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | Petrolio WTI | 6.32% | | Solana | -2.44% |
| 3 | VIX (volatilita) | 4.71% | | USD/JPY | -2.41% |
| 4 | US 5Y Treasury Yield | 0.88% | | Bitcoin | -1.85% |
| 5 | US 10Y Treasury Yield | 0.63% | | Ethereum | -0.83% |
| 6 | US 30Y Treasury Yield | 0.57% | | Nasdaq Composite | -0.64% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | Solana | -4.22% |
| 2 | Petrolio WTI | 11.72% | | Bitcoin | -3.88% |
| 3 | US 5Y Treasury Yield | 1.32% | | Dow Jones | -1.88% |
| 4 | US 10Y Treasury Yield | 0.84% | | USD/JPY | -1.78% |
| 5 | VIX (volatilita) | 0.73% | | Ethereum | -1.60% |
| 6 | Nasdaq Composite | 0.59% | | GBP/USD | -0.93% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Dow Jones | -3.10% |
| 2 | Solana | 28.34% | | Shanghai Composite | -2.53% |
| 3 | Ethereum | 27.50% | | Nikkei 225 | -2.38% |
| 4 | Petrolio WTI | 26.39% | | S&P 500 | -2.09% |
| 5 | Bitcoin | 18.65% | | Nasdaq Composite | -2.05% |
| 6 | VIX (volatilita) | 15.35% | | USD/JPY | -1.10% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.011 | -2.09% | 18.65% | **-20.74 pp** |
| S&P 500 vs VIX (volatilita) | -0.066 | -2.09% | 15.35% | **-17.44 pp** |
| S&P 500 vs Oro (spot) | 0.059 | -2.09% | 6.69% | **-8.78 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.010 | 2.85% | 6.69% | **-3.84 pp** |
| EUR/USD vs Indice dollaro DXY | -0.016 | 0.37% | -0.72% | **1.09 pp** |
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
| US 2Y Treasury Rate | 4.43 | 2026-09-09 | 0.04 |
| US 10Y Treasury Rate | 4.83 | 2026-09-09 | 0.03 |
| US 30Y Treasury Rate | 5.28 | 2026-09-09 | 0.03 |
| Spread 10Y-2Y USA | 0.39 | 2026-09-10 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **40.0 bp**, 30Y-10Y **45.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.4600 | 15.35% | 80.09% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 98.9485 | 28.34% | 47.02% | -13.59% |
| Ethereum | 2 439.5148 | 27.50% | 46.00% | -5.78% |
| Bitcoin | 76 658.2843 | 18.65% | 40.71% | -5.72% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| US 5Y Treasury Yield | 4.6100 | n/d | 13.18% | -0.66% |
| Argento (spot) | 68.2900 | 7.33% | 12.06% | -11.21% |
| Nasdaq Composite | 26 253.3400 | -2.05% | 11.76% | -7.00% |
| US 10Y Treasury Yield | 4.8300 | 2.85% | 10.58% | -2.70% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| Dow Jones | 52 064.1000 | -3.10% | 10.36% | -4.20% |
| Hang Seng | 25 511.1000 | 0.16% | 8.68% | -3.43% |
| S&P 500 | 7 636.3600 | -2.09% | 8.16% | -3.42% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
