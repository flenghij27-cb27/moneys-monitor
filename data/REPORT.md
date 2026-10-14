# Moneys Monitor - Report di mercato

Generato: `2026-10-14T00:29:33+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-14T00:28:58+00:00` (449 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.03% | 0.00% | **-0.03 pp** |
| 1w | 0.02% | 0.00% | **0.02 pp** |
| 1m | -0.85% | 0.00% | **-0.85 pp** |
| 3m | 11.54% | 4.57% | **6.97 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 2.49% | | Nasdaq Composite | -0.44% |
| 3 | US 5Y Treasury Yield | 0.60% | | Dow Jones | -0.35% |
| 4 | US 10Y Treasury Yield | 0.38% | | Ethereum | -0.08% |
| 5 | USD/JPY | 0.34% | | GBP/USD | -0.04% |
| 6 | Solana | 0.25% | | S&P 500 | -0.02% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | GBP/USD | -2.16% |
| 2 | Petrolio WTI | 5.20% | | VIX (volatilita) | -2.00% |
| 3 | Gas naturale | 4.48% | | Solana | -1.32% |
| 4 | Indice dollaro Fed (broad) | 2.99% | | Nasdaq Composite | -0.84% |
| 5 | USD/JPY | 1.43% | | US 5Y Treasury Yield | -0.79% |
| 6 | Bitcoin | 1.28% | | US 10Y Treasury Yield | -0.76% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Solana | -6.59% |
| 2 | Petrolio WTI | 15.44% | | Ethereum | -6.55% |
| 3 | Gas naturale | 10.14% | | VIX (volatilita) | -3.24% |
| 4 | US 10Y Treasury Yield | 5.86% | | EUR/USD | -3.14% |
| 5 | US 5Y Treasury Yield | 5.68% | | GBP/USD | -2.05% |
| 6 | US 30Y Treasury Yield | 4.28% | | Dow Jones | -1.43% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.036 | 5.86% | 0.00% | **5.86 pp** |
| S&P 500 vs VIX (volatilita) | -0.042 | 2.43% | -3.24% | **5.67 pp** |
| S&P 500 vs Bitcoin | 0.023 | 2.43% | -1.23% | **3.66 pp** |
| EUR/USD vs Indice dollaro DXY | 0.007 | -3.14% | 0.00% | **-3.14 pp** |
| S&P 500 vs Oro (spot) | 0.285 | 2.43% | 0.00% | **2.43 pp** |
| S&P 500 vs Nasdaq Composite | 0.111 | 2.43% | 3.47% | **-1.04 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.80 | 2026-10-09 | 0.05 |
| US 10Y Treasury Rate | 5.24 | 2026-10-09 | 0.02 |
| US 30Y Treasury Rate | 5.60 | 2026-10-09 | 0.00 |
| Spread 10Y-2Y USA | 0.42 | 2026-10-13 | -0.02 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **44.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.2100 | -3.24% | 98.01% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 107.3080 | -6.59% | 35.59% | -13.59% |
| Ethereum | 2 507.1740 | -6.55% | 24.66% | -10.76% |
| US 5Y Treasury Yield | 5.0200 | 5.68% | 18.54% | -1.96% |
| US 10Y Treasury Yield | 5.2400 | 5.86% | 16.70% | -2.70% |
| Bitcoin | 83 361.8498 | -1.23% | 16.27% | -6.86% |
| Nasdaq Composite | 27 245.9000 | 3.47% | 14.33% | -7.00% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 4.28% | 13.45% | -1.49% |
| Dow Jones | 51 670.1000 | -1.43% | 9.69% | -6.34% |
| S&P 500 | 7 805.4500 | 2.43% | 9.51% | -3.42% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
