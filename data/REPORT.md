# Moneys Monitor - Report di mercato

Generato: `2026-09-16T16:19:24+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-16T16:18:52+00:00` (362 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.14% | 0.00% | **-0.14 pp** |
| 1w | -1.43% | 0.00% | **-1.43 pp** |
| 1m | -0.74% | -0.53% | **-0.21 pp** |
| 3m | 8.46% | 17.52% | **-9.05 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | Petrolio WTI | 6.32% | | USD/JPY | -1.54% |
| 3 | VIX (volatilita) | 0.58% | | Nasdaq Composite | -0.78% |
| 4 | US 5Y Treasury Yield | 0.42% | | Dow Jones | -0.63% |
| 5 | US 10Y Treasury Yield | 0.20% | | S&P 500 | -0.45% |
| 6 | Bitcoin | 0.15% | | Ethereum | -0.35% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | Solana | -4.88% |
| 2 | Petrolio WTI | 11.72% | | Ethereum | -4.77% |
| 3 | VIX (volatilita) | 9.41% | | USD/JPY | -3.32% |
| 4 | US 5Y Treasury Yield | 5.73% | | Bitcoin | -1.84% |
| 5 | US 10Y Treasury Yield | 3.97% | | Nasdaq Composite | -1.66% |
| 6 | US 30Y Treasury Yield | 1.91% | | Dow Jones | -1.31% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Bitcoin | -3.84% |
| 2 | Petrolio WTI | 26.39% | | Ethereum | -3.16% |
| 3 | VIX (volatilita) | 8.65% | | Dow Jones | -2.56% |
| 4 | US 10Y Treasury Yield | 5.21% | | USD/JPY | -2.56% |
| 5 | Gas naturale | 5.20% | | Nasdaq Composite | -2.49% |
| 6 | Solana | 1.16% | | S&P 500 | -2.06% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.138 | -2.06% | 8.65% | **-10.71 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.114 | 5.21% | -0.30% | **5.51 pp** |
| S&P 500 vs Bitcoin | -0.023 | -2.06% | -3.84% | **1.78 pp** |
| S&P 500 vs Oro (spot) | -0.175 | -2.06% | -0.30% | **-1.76 pp** |
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
| US 2Y Treasury Rate | 4.65 | 2026-09-14 | 0.02 |
| US 10Y Treasury Rate | 4.97 | 2026-09-14 | 0.01 |
| US 30Y Treasury Rate | 5.34 | 2026-09-14 | -0.01 |
| Spread 10Y-2Y USA | 0.33 | 2026-09-15 | 0.01 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.2000 | 8.65% | 92.36% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 97.2207 | 1.16% | 45.81% | -13.59% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 393.2081 | -3.16% | 33.81% | -5.78% |
| Bitcoin | 75 748.7507 | -3.84% | 29.08% | -6.86% |
| US 5Y Treasury Yield | 4.8000 | n/d | 15.91% | -0.66% |
| US 10Y Treasury Yield | 4.9700 | 5.21% | 13.17% | -2.70% |
| Nasdaq Composite | 25 981.5700 | -2.49% | 12.03% | -7.00% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| Dow Jones | 52 093.1100 | -2.56% | 11.18% | -4.20% |
| US 30Y Treasury Yield | 5.3400 | n/d | 9.19% | -0.57% |
| S&P 500 | 7 585.7300 | -2.06% | 8.83% | -3.42% |
| GBP/USD | 1.3524 | 0.25% | 3.59% | -1.82% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
