# Moneys Monitor - Report di mercato

Generato: `2026-09-16T10:59:39+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-16T10:58:51+00:00` (361 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.11% | 0.00% | **-0.11 pp** |
| 1w | -1.39% | 0.00% | **-1.39 pp** |
| 1m | -0.71% | -0.53% | **-0.18 pp** |
| 3m | 8.51% | 17.52% | **-9.01 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | VIX (volatilita) | 7.95% | | USD/JPY | -1.54% |
| 3 | Petrolio WTI | 6.32% | | Nasdaq Composite | -0.78% |
| 4 | US 5Y Treasury Yield | 0.42% | | Dow Jones | -0.63% |
| 5 | Bitcoin | 0.29% | | S&P 500 | -0.45% |
| 6 | US 10Y Treasury Yield | 0.20% | | US 30Y Treasury Yield | -0.19% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | Solana | -4.98% |
| 2 | VIX (volatilita) | 11.76% | | Ethereum | -4.44% |
| 3 | Petrolio WTI | 11.72% | | USD/JPY | -3.32% |
| 4 | US 5Y Treasury Yield | 5.73% | | Bitcoin | -1.70% |
| 5 | US 10Y Treasury Yield | 3.97% | | Nasdaq Composite | -1.66% |
| 6 | US 30Y Treasury Yield | 1.91% | | Dow Jones | -1.31% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Bitcoin | -3.70% |
| 2 | Petrolio WTI | 26.39% | | Ethereum | -2.83% |
| 3 | VIX (volatilita) | 12.50% | | Dow Jones | -2.56% |
| 4 | US 10Y Treasury Yield | 5.21% | | USD/JPY | -2.56% |
| 5 | Gas naturale | 5.20% | | Nasdaq Composite | -2.49% |
| 6 | Solana | 1.04% | | S&P 500 | -2.06% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.597 | -2.06% | 12.50% | **-14.56 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.114 | 5.21% | -0.30% | **5.51 pp** |
| S&P 500 vs Oro (spot) | -0.175 | -2.06% | -0.30% | **-1.76 pp** |
| S&P 500 vs Bitcoin | -0.024 | -2.06% | -3.70% | **1.64 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | -0.30% | -0.76% | **0.46 pp** |
| S&P 500 vs Nasdaq Composite | 0.951 | -2.06% | -2.49% | **0.43 pp** |
| EUR/USD vs Indice dollaro DXY | -0.015 | -0.31% | -0.04% | **-0.27 pp** |

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
| VIX (volatilita) | 17.1000 | 12.50% | 95.61% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 97.1121 | 1.04% | 45.81% | -13.59% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 401.3596 | -2.83% | 33.81% | -5.78% |
| Bitcoin | 75 854.5358 | -3.70% | 29.10% | -6.86% |
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
