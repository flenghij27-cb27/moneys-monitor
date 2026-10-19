# Moneys Monitor - Report di mercato

Generato: `2026-10-19T20:55:02+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-19T20:54:17+00:00` (468 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.13% | 0.00% | **-0.13 pp** |
| 1w | -0.41% | 0.00% | **-0.41 pp** |
| 1m | -2.11% | 0.00% | **-2.11 pp** |
| 3m | 10.04% | 5.32% | **4.71 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 21.45% | | S&P 500 | -1.09% |
| 2 | Gas naturale | 6.27% | | Ethereum | -0.41% |
| 3 | Petrolio WTI | 5.89% | | US 5Y Treasury Yield | -0.41% |
| 4 | Petrolio Brent | 0.88% | | Dow Jones | -0.34% |
| 5 | GBP/USD | 0.76% | | EUR/USD | -0.25% |
| 6 | Solana | 0.28% | | USD/JPY | -0.21% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 34.70% | | US 30Y Treasury Yield | -3.04% |
| 2 | Petrolio Brent | 15.56% | | US 10Y Treasury Yield | -2.49% |
| 3 | Gas naturale | 14.59% | | US 5Y Treasury Yield | -2.00% |
| 4 | Petrolio WTI | 4.78% | | S&P 500 | -1.95% |
| 5 | USD/JPY | 2.79% | | Nasdaq Composite | -1.77% |
| 6 | Indice dollaro Fed (broad) | 2.70% | | GBP/USD | -1.43% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -11.78% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -10.61% |
| 3 | VIX (volatilita) | 16.90% | | EUR/USD | -2.05% |
| 4 | Gas naturale | 15.16% | | Bitcoin | -1.85% |
| 5 | Nasdaq Composite | 2.83% | | GBP/USD | -1.22% |
| 6 | US 10Y Treasury Yield | 1.60% | | USD/JPY | -0.88% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs VIX (volatilita) | -0.005 | 0.28% | 16.90% | **-16.62 pp** |
| S&P 500 vs Nasdaq Composite | 0.100 | 0.28% | 2.83% | **-2.55 pp** |
| S&P 500 vs Bitcoin | 0.154 | 0.28% | -1.85% | **2.13 pp** |
| EUR/USD vs Indice dollaro DXY | -0.179 | -2.05% | 0.00% | **-2.05 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.024 | 1.60% | 0.00% | **1.60 pp** |
| S&P 500 vs Oro (spot) | 0.016 | 0.28% | 0.00% | **0.28 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.74 | 2026-10-16 | -0.03 |
| US 10Y Treasury Rate | 5.09 | 2026-10-16 | -0.01 |
| US 30Y Treasury Rate | 5.43 | 2026-10-16 | 0.00 |
| Spread 10Y-2Y USA | 0.35 | 2026-10-16 | 0.02 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **35.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.9900 | 16.90% | 116.39% | -31.22% |
| Petrolio Brent | 126.5500 | 42.82% | 107.21% | -21.50% |
| Petrolio WTI | 101.9100 | 22.98% | 72.41% | -18.71% |
| Gas naturale | 3.2200 | 15.16% | 56.78% | -18.87% |
| Solana | 104.3486 | -11.78% | 31.55% | -15.47% |
| Ethereum | 2 396.2857 | -10.61% | 27.49% | -13.58% |
| US 5Y Treasury Yield | 4.8900 | 0.62% | 18.86% | -3.93% |
| Bitcoin | 81 887.9308 | -1.85% | 17.96% | -6.86% |
| US 10Y Treasury Yield | 5.0900 | 1.60% | 17.56% | -4.14% |
| US 30Y Treasury Yield | 5.4300 | 1.50% | 14.83% | -4.23% |
| Nasdaq Composite | 26 713.0300 | 2.83% | 14.71% | -7.00% |
| USD/JPY | 158.0000 | -0.88% | 13.75% | -6.19% |
| S&P 500 | 7 659.4400 | 0.28% | 10.46% | -3.42% |
| Dow Jones | 52 002.4100 | 0.43% | 9.28% | -6.34% |
| Indice dollaro Fed (broad) | 121.4048 | n/d | 8.89% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
