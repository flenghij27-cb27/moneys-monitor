# Moneys Monitor - Report di mercato

Generato: `2026-09-16T23:46:10+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-16T23:44:10+00:00` (363 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.14% | 0.00% | **0.14 pp** |
| 1w | -1.15% | 0.00% | **-1.15 pp** |
| 1m | -0.46% | -0.53% | **0.07 pp** |
| 3m | 8.82% | 17.52% | **-8.69 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | USD/JPY | -1.54% |
| 2 | Petrolio WTI | 10.03% | | Dow Jones | -1.21% |
| 3 | Gas naturale | 5.69% | | Nasdaq Composite | -0.78% |
| 4 | Solana | 1.43% | | S&P 500 | -0.45% |
| 5 | Bitcoin | 0.63% | | EUR/USD | -0.02% |
| 6 | US 5Y Treasury Yield | 0.63% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | Ethereum | -3.84% |
| 2 | Petrolio WTI | 25.85% | | Solana | -3.52% |
| 3 | VIX (volatilita) | 9.41% | | USD/JPY | -3.32% |
| 4 | US 5Y Treasury Yield | 5.69% | | Dow Jones | -1.75% |
| 5 | Gas naturale | 5.51% | | Nasdaq Composite | -1.66% |
| 6 | US 10Y Treasury Yield | 4.17% | | Bitcoin | -1.37% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | Dow Jones | -3.53% |
| 2 | Petrolio WTI | 36.89% | | Bitcoin | -3.38% |
| 3 | Gas naturale | 11.57% | | USD/JPY | -2.56% |
| 4 | VIX (volatilita) | 8.65% | | Nasdaq Composite | -2.49% |
| 5 | US 10Y Treasury Yield | 6.25% | | Ethereum | -2.22% |
| 6 | Solana | 2.60% | | S&P 500 | -2.06% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| S&P 500 vs VIX (volatilita) | -0.138 | -2.06% | 8.65% | **-10.71 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.136 | 6.25% | -0.30% | **6.55 pp** |
| S&P 500 vs Oro (spot) | -0.175 | -2.06% | -0.30% | **-1.76 pp** |
| S&P 500 vs Bitcoin | -0.026 | -2.06% | -3.38% | **1.32 pp** |
| EUR/USD vs Indice dollaro DXY | 0.051 | -1.22% | -0.04% | **-1.18 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | -0.30% | -0.76% | **0.46 pp** |
| S&P 500 vs Nasdaq Composite | 0.951 | -2.06% | -2.49% | **0.43 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.67 | 2026-09-15 | 0.02 |
| US 10Y Treasury Rate | 5.00 | 2026-09-15 | 0.03 |
| US 30Y Treasury Rate | 5.36 | 2026-09-15 | 0.02 |
| Spread 10Y-2Y USA | 0.27 | 2026-09-16 | -0.06 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **33.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.2000 | 8.65% | 92.36% | -31.03% |
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Solana | 98.6066 | 2.60% | 46.10% | -13.59% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| Ethereum | 2 416.4974 | -2.22% | 33.91% | -5.78% |
| Bitcoin | 76 109.3217 | -3.38% | 29.21% | -6.86% |
| US 5Y Treasury Yield | 4.8300 | n/d | 15.25% | -0.66% |
| US 10Y Treasury Yield | 5.0000 | 6.25% | 12.12% | -2.70% |
| Nasdaq Composite | 25 981.5700 | -2.49% | 12.03% | -7.00% |
| Dow Jones | 51 461.9000 | -3.53% | 11.75% | -5.31% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| S&P 500 | 7 585.7300 | -2.06% | 8.83% | -3.42% |
| US 30Y Treasury Yield | 5.3600 | n/d | 8.81% | -0.57% |
| GBP/USD | 1.3524 | 0.25% | 3.59% | -1.82% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
