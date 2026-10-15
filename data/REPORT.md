# Moneys Monitor - Report di mercato

Generato: `2026-10-15T00:02:06+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-15T00:00:22+00:00` (452 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.86% | 0.00% | **-0.86 pp** |
| 1w | -0.90% | 0.00% | **-0.90 pp** |
| 1m | -1.62% | 0.00% | **-1.62 pp** |
| 3m | 10.31% | 5.61% | **4.70 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 0.39% | | Ethereum | -3.59% |
| 3 | USD/JPY | 0.34% | | Solana | -2.70% |
| 4 | Indice dollaro Fed (broad) | 0.18% | | Bitcoin | -2.11% |
| 5 | Petrolio WTI | 0.08% | | US 30Y Treasury Yield | -0.71% |
| 6 | EUR/USD | 0.06% | | US 10Y Treasury Yield | -0.57% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -4.22% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -2.32% |
| 3 | Gas naturale | 4.48% | | GBP/USD | -2.16% |
| 4 | Indice dollaro Fed (broad) | 2.99% | | US 10Y Treasury Yield | -1.88% |
| 5 | VIX (volatilita) | 1.73% | | US 30Y Treasury Yield | -1.77% |
| 6 | USD/JPY | 1.43% | | Nasdaq Composite | -1.43% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Ethereum | -9.84% |
| 2 | Petrolio WTI | 15.44% | | Solana | -9.34% |
| 3 | Gas naturale | 10.14% | | VIX (volatilita) | -7.23% |
| 4 | US 10Y Treasury Yield | 5.04% | | Bitcoin | -3.33% |
| 5 | US 5Y Treasury Yield | 4.60% | | EUR/USD | -2.98% |
| 6 | US 30Y Treasury Yield | 3.93% | | GBP/USD | -2.05% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| S&P 500 vs VIX (volatilita) | 0.119 | 2.43% | -7.23% | **9.66 pp** |
| S&P 500 vs Bitcoin | 0.025 | 2.43% | -3.33% | **5.76 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.034 | 5.04% | 0.00% | **5.04 pp** |
| EUR/USD vs Indice dollaro DXY | 0.007 | -2.98% | 0.00% | **-2.98 pp** |
| S&P 500 vs Oro (spot) | 0.036 | 2.43% | 0.00% | **2.43 pp** |
| S&P 500 vs Nasdaq Composite | 0.947 | 2.43% | 3.89% | **-1.46 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.79 | 2026-10-13 | -0.01 |
| US 10Y Treasury Rate | 5.21 | 2026-10-13 | -0.03 |
| US 30Y Treasury Rate | 5.56 | 2026-10-13 | -0.04 |
| Spread 10Y-2Y USA | 0.37 | 2026-10-14 | -0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **42.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.2700 | -7.23% | 92.67% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 104.1521 | -9.34% | 36.40% | -14.70% |
| Ethereum | 2 418.9888 | -9.84% | 27.20% | -12.70% |
| US 5Y Treasury Yield | 5.0000 | 4.60% | 18.67% | -1.96% |
| Bitcoin | 81 591.4135 | -3.33% | 17.83% | -6.86% |
| US 10Y Treasury Yield | 5.2100 | 5.04% | 16.98% | -2.70% |
| Nasdaq Composite | 27 204.3800 | 3.89% | 13.93% | -7.00% |
| US 30Y Treasury Yield | 5.5600 | 3.93% | 13.79% | -1.94% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| S&P 500 | 7 805.4500 | 2.43% | 9.51% | -3.42% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |
| Dow Jones | 51 621.4800 | -0.91% | 8.66% | -6.34% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
