# Moneys Monitor - Report di mercato

Generato: `2026-10-09T20:36:30+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-09T20:35:55+00:00` (436 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.18% | 0.00% | **-0.18 pp** |
| 1w | -1.98% | 0.00% | **-1.98 pp** |
| 1m | -0.23% | 0.00% | **-0.23 pp** |
| 3m | 11.36% | 9.38% | **1.97 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 2.19% | | Nasdaq Composite | -1.25% |
| 3 | Indice dollaro Fed (broad) | 0.88% | | US 30Y Treasury Yield | -1.23% |
| 4 | Bitcoin | 0.72% | | US 10Y Treasury Yield | -1.14% |
| 5 | USD/JPY | 0.40% | | Solana | -0.94% |
| 6 | EUR/USD | 0.18% | | US 5Y Treasury Yield | -0.80% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -10.55% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -8.27% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -5.98% |
| 4 | Indice dollaro Fed (broad) | 2.22% | | Bitcoin | -3.46% |
| 5 | S&P 500 | 1.29% | | GBP/USD | -2.37% |
| 6 | Nasdaq Composite | 1.20% | | USD/JPY | -1.35% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Ethereum | -5.28% |
| 2 | Petrolio WTI | 15.44% | | Solana | -3.88% |
| 3 | Gas naturale | 10.14% | | EUR/USD | -3.53% |
| 4 | US 5Y Treasury Yield | 8.24% | | Dow Jones | -2.19% |
| 5 | US 10Y Treasury Yield | 8.07% | | GBP/USD | -2.02% |
| 6 | VIX (volatilita) | 7.61% | | USD/JPY | -0.95% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.068 | 8.07% | 0.00% | **8.07 pp** |
| S&P 500 vs VIX (volatilita) | 0.128 | 1.69% | 7.61% | **-5.92 pp** |
| EUR/USD vs Indice dollaro DXY | 0.089 | -3.53% | 0.00% | **-3.53 pp** |
| S&P 500 vs Nasdaq Composite | 0.948 | 1.69% | 3.58% | **-1.89 pp** |
| S&P 500 vs Oro (spot) | -0.156 | 1.69% | 0.00% | **1.69 pp** |
| S&P 500 vs Bitcoin | -0.088 | 1.69% | 1.60% | **0.09 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.75 | 2026-10-08 | -0.02 |
| US 10Y Treasury Rate | 5.22 | 2026-10-08 | -0.06 |
| US 30Y Treasury Rate | 5.60 | 2026-10-08 | -0.07 |
| Spread 10Y-2Y USA | 0.47 | 2026-10-08 | -0.04 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.4100 | 7.61% | 98.66% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 108.7433 | -3.88% | 43.15% | -13.59% |
| Ethereum | 2 476.4967 | -5.28% | 30.65% | -10.76% |
| Bitcoin | 82 309.6635 | 1.60% | 29.72% | -6.86% |
| US 5Y Treasury Yield | 4.9900 | 8.24% | 18.55% | -1.96% |
| US 10Y Treasury Yield | 5.2200 | 8.07% | 16.70% | -2.70% |
| Nasdaq Composite | 27 193.3400 | 3.58% | 14.59% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 6.06% | 13.60% | -1.49% |
| S&P 500 | 7 765.3600 | 1.69% | 10.17% | -3.42% |
| Dow Jones | 51 231.6400 | -2.19% | 9.96% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
