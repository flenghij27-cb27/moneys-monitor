# Moneys Monitor - Report di mercato

Generato: `2026-10-22T11:19:10+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-22T11:18:38+00:00` (476 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.97% | 0.00% | **-0.97 pp** |
| 1w | 0.09% | 0.00% | **0.09 pp** |
| 1m | -2.72% | 0.00% | **-2.72 pp** |
| 3m | 9.71% | 7.01% | **2.70 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.87% | | Petrolio Brent | -8.95% |
| 2 | Nasdaq Composite | 1.05% | | VIX (volatilita) | -6.13% |
| 3 | GBP/USD | 0.76% | | Ethereum | -4.47% |
| 4 | Dow Jones | 0.69% | | Gas naturale | -3.73% |
| 5 | S&P 500 | 0.58% | | Solana | -3.67% |
| 6 | EUR/USD | 0.17% | | Bitcoin | -3.21% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 13.36% | | Petrolio Brent | -11.91% |
| 2 | Gas naturale | 4.38% | | US 30Y Treasury Yield | -2.52% |
| 3 | USD/JPY | 2.79% | | Nasdaq Composite | -1.84% |
| 4 | Indice dollaro Fed (broad) | 2.70% | | US 10Y Treasury Yield | -1.73% |
| 5 | Dow Jones | 2.39% | | GBP/USD | -1.43% |
| 6 | Solana | 1.22% | | US 5Y Treasury Yield | -1.20% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 32.93% | | Solana | -11.50% |
| 2 | Petrolio Brent | 32.51% | | Ethereum | -10.92% |
| 3 | Gas naturale | 13.51% | | Bitcoin | -3.17% |
| 4 | US 10Y Treasury Yield | 2.20% | | VIX (volatilita) | -2.26% |
| 5 | Dow Jones | 1.91% | | EUR/USD | -2.00% |
| 6 | US 5Y Treasury Yield | 1.65% | | Nasdaq Composite | -1.55% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.139 | -0.10% | -3.17% | **3.07 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.097 | 2.20% | 0.00% | **2.20 pp** |
| S&P 500 vs VIX (volatilita) | -0.013 | -0.10% | -2.26% | **2.16 pp** |
| EUR/USD vs Indice dollaro DXY | -0.132 | -2.00% | 0.00% | **-2.00 pp** |
| S&P 500 vs Nasdaq Composite | 0.100 | -0.10% | -1.55% | **1.45 pp** |
| Petrolio WTI vs Petrolio Brent | 0.819 | 32.93% | 32.51% | **0.42 pp** |
| S&P 500 vs Oro (spot) | 0.012 | -0.10% | 0.00% | **-0.10 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.79 | 2026-10-20 | 0.02 |
| US 10Y Treasury Rate | 5.12 | 2026-10-20 | -0.03 |
| US 30Y Treasury Rate | 5.42 | 2026-10-20 | -0.06 |
| Spread 10Y-2Y USA | 0.32 | 2026-10-21 | -0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **33.0 bp**, 30Y-10Y **30.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 115.2200 | 32.51% | 114.17% | -21.50% |
| VIX (volatilita) | 17.3100 | -2.26% | 112.44% | -31.22% |
| Petrolio WTI | 107.8900 | 32.93% | 74.25% | -18.71% |
| Gas naturale | 3.1000 | 13.51% | 58.95% | -18.87% |
| Solana | 104.4593 | -11.50% | 36.04% | -15.47% |
| Ethereum | 2 401.9544 | -10.92% | 34.54% | -13.58% |
| Bitcoin | 81 897.1233 | -3.17% | 23.27% | -6.86% |
| US 5Y Treasury Yield | 4.9400 | 1.65% | 18.09% | -3.93% |
| US 10Y Treasury Yield | 5.1200 | 2.20% | 17.05% | -4.14% |
| US 30Y Treasury Yield | 5.4200 | 1.50% | 14.97% | -4.41% |
| USD/JPY | 158.0000 | -0.88% | 13.75% | -6.19% |
| Nasdaq Composite | 26 702.8600 | -1.55% | 13.11% | -7.00% |
| Dow Jones | 52 856.0900 | 1.91% | 9.36% | -6.34% |
| S&P 500 | 7 757.1700 | -0.10% | 8.93% | -3.42% |
| Indice dollaro Fed (broad) | 121.4048 | n/d | 8.89% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
