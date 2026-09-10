# Moneys Monitor - Report di mercato

Generato: `2026-09-10T19:05:17+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-10T19:04:40+00:00` (342 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.37% | 0.00% | **-0.37 pp** |
| 1w | -0.66% | 0.00% | **-0.66 pp** |
| 1m | 7.40% | 7.01% | **0.39 pp** |
| 3m | 9.59% | 13.53% | **-3.93 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | Petrolio WTI | 6.32% | | USD/JPY | -2.41% |
| 3 | VIX (volatilita) | 4.71% | | Solana | -1.62% |
| 4 | US 5Y Treasury Yield | 0.66% | | Bitcoin | -1.20% |
| 5 | US 10Y Treasury Yield | 0.42% | | Dow Jones | -0.77% |
| 6 | Ethereum | 0.21% | | Nasdaq Composite | -0.64% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | Solana | -3.41% |
| 2 | Petrolio WTI | 11.72% | | Bitcoin | -3.24% |
| 3 | US 5Y Treasury Yield | 1.78% | | USD/JPY | -1.78% |
| 4 | US 10Y Treasury Yield | 1.05% | | GBP/USD | -0.93% |
| 5 | VIX (volatilita) | 0.73% | | Dow Jones | -0.73% |
| 6 | Nasdaq Composite | 0.59% | | Ethereum | -0.56% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Dow Jones | -2.71% |
| 2 | Solana | 29.42% | | Shanghai Composite | -2.53% |
| 3 | Ethereum | 28.84% | | Nikkei 225 | -2.38% |
| 4 | Petrolio WTI | 26.39% | | S&P 500 | -2.09% |
| 5 | Bitcoin | 19.44% | | Nasdaq Composite | -2.05% |
| 6 | VIX (volatilita) | 15.35% | | USD/JPY | -1.10% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.006 | -2.09% | 19.44% | **-21.53 pp** |
| S&P 500 vs VIX (volatilita) | -0.066 | -2.09% | 15.35% | **-17.44 pp** |
| S&P 500 vs Oro (spot) | 0.059 | -2.09% | 6.69% | **-8.78 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.136 | 3.43% | 6.69% | **-3.26 pp** |
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
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 99.7816 | 29.42% | 46.32% | -13.59% |
| Ethereum | 2 465.1319 | 28.84% | 45.67% | -5.78% |
| Bitcoin | 77 165.1558 | 19.44% | 40.26% | -5.72% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
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
