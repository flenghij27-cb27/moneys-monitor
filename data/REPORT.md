# Moneys Monitor - Report di mercato

Generato: `2026-10-23T00:05:19+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-23T00:04:32+00:00` (478 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.09% | 0.00% | **0.09 pp** |
| 1w | -0.36% | 0.00% | **-0.36 pp** |
| 1m | -2.81% | 0.00% | **-2.81 pp** |
| 3m | 6.96% | 2.72% | **4.24 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.87% | | Petrolio Brent | -8.95% |
| 2 | Nasdaq Composite | 1.05% | | Gas naturale | -3.73% |
| 3 | GBP/USD | 0.76% | | VIX (volatilita) | -3.64% |
| 4 | S&P 500 | 0.58% | | Solana | -0.57% |
| 5 | US 10Y Treasury Yield | 0.20% | | EUR/USD | -0.26% |
| 6 | US 5Y Treasury Yield | 0.20% | | USD/JPY | -0.21% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 4.38% | | Petrolio Brent | -11.91% |
| 2 | USD/JPY | 2.79% | | Nasdaq Composite | -1.84% |
| 3 | Indice dollaro Fed (broad) | 2.70% | | US 30Y Treasury Yield | -1.81% |
| 4 | Dow Jones | 1.32% | | GBP/USD | -1.43% |
| 5 | Petrolio WTI | 0.81% | | US 10Y Treasury Yield | -1.16% |
| 6 | S&P 500 | 0.50% | | VIX (volatilita) | -1.13% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 32.93% | | Solana | -12.23% |
| 2 | Petrolio Brent | 32.51% | | Ethereum | -10.58% |
| 3 | Gas naturale | 13.51% | | Bitcoin | -3.67% |
| 4 | VIX (volatilita) | 8.03% | | EUR/USD | -1.81% |
| 5 | US 10Y Treasury Yield | 3.43% | | Nasdaq Composite | -1.55% |
| 6 | Dow Jones | 2.63% | | GBP/USD | -1.22% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.023 | -0.10% | 8.03% | **-8.13 pp** |
| S&P 500 vs Bitcoin | 0.073 | -0.10% | -3.67% | **3.57 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.097 | 3.43% | 0.00% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | -0.133 | -1.81% | 0.00% | **-1.81 pp** |
| S&P 500 vs Nasdaq Composite | 0.100 | -0.10% | -1.55% | **1.45 pp** |
| Petrolio WTI vs Petrolio Brent | 0.819 | 32.93% | 32.51% | **0.42 pp** |
| S&P 500 vs Oro (spot) | 0.040 | -0.10% | 0.00% | **-0.10 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.81 | 2026-10-21 | 0.02 |
| US 10Y Treasury Rate | 5.13 | 2026-10-21 | 0.01 |
| US 30Y Treasury Rate | 5.42 | 2026-10-21 | 0.00 |
| Spread 10Y-2Y USA | 0.31 | 2026-10-22 | -0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **29.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 115.2200 | 32.51% | 114.17% | -21.50% |
| VIX (volatilita) | 16.6800 | 8.03% | 112.20% | -31.22% |
| Petrolio WTI | 107.8900 | 32.93% | 74.25% | -18.71% |
| Gas naturale | 3.1000 | 13.51% | 58.95% | -18.87% |
| Solana | 103.5582 | -12.23% | 35.59% | -15.47% |
| Ethereum | 2 385.0151 | -10.58% | 35.38% | -13.93% |
| Bitcoin | 81 261.0651 | -3.67% | 24.27% | -6.86% |
| US 5Y Treasury Yield | 4.9500 | 2.48% | 18.09% | -3.93% |
| US 10Y Treasury Yield | 5.1300 | 3.43% | 17.04% | -4.14% |
| US 30Y Treasury Yield | 5.4200 | 2.46% | 14.97% | -4.41% |
| USD/JPY | 158.0000 | -0.88% | 13.75% | -6.19% |
| Nasdaq Composite | 26 702.8600 | -1.55% | 13.11% | -7.00% |
| Dow Jones | 52 867.9800 | 2.63% | 9.22% | -6.34% |
| S&P 500 | 7 757.1700 | -0.10% | 8.93% | -3.42% |
| Indice dollaro Fed (broad) | 121.4048 | n/d | 8.89% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
