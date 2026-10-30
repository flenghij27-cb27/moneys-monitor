# Moneys Monitor - Report di mercato

Generato: `2026-10-30T01:16:09+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-30T01:15:33+00:00` (501 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.54% | 0.00% | **-0.54 pp** |
| 1w | -1.53% | 0.00% | **-1.53 pp** |
| 1m | -2.97% | 0.00% | **-2.97 pp** |
| 3m | -1.76% | 0.00% | **-1.76 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 6.84% | | Gas naturale | -10.97% |
| 2 | US 30Y Treasury Yield | 1.32% | | Petrolio WTI | -4.19% |
| 3 | US 10Y Treasury Yield | 1.20% | | VIX (volatilita) | -3.48% |
| 4 | US 5Y Treasury Yield | 0.62% | | Bitcoin | -2.29% |
| 5 | GBP/USD | 0.34% | | Solana | -1.98% |
| 6 | S&P 500 | 0.28% | | Ethereum | -1.72% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 7.22% | | Solana | -6.61% |
| 2 | Petrolio Brent | 7.15% | | Gas naturale | -4.83% |
| 3 | Indice dollaro Fed (broad) | 1.51% | | Ethereum | -4.75% |
| 4 | VIX (volatilita) | 1.38% | | Bitcoin | -3.74% |
| 5 | S&P 500 | 0.41% | | US 5Y Treasury Yield | -2.02% |
| 6 | GBP/USD | 0.02% | | US 10Y Treasury Yield | -1.56% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -12.94% |
| 2 | Petrolio WTI | 25.40% | | Ethereum | -10.31% |
| 3 | VIX (volatilita) | 5.42% | | Bitcoin | -6.22% |
| 4 | Dow Jones | 2.82% | | US 5Y Treasury Yield | -4.15% |
| 5 | Gas naturale | 1.55% | | US 10Y Treasury Yield | -3.63% |
| 6 | S&P 500 | 0.78% | | US 30Y Treasury Yield | -3.42% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| S&P 500 vs Bitcoin | -0.011 | 0.78% | -6.22% | **7.00 pp** |
| S&P 500 vs VIX (volatilita) | 0.081 | 0.78% | 5.42% | **-4.64 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.052 | -3.63% | 0.00% | **-3.63 pp** |
| EUR/USD vs Indice dollaro DXY | 0.074 | -1.98% | 0.00% | **-1.98 pp** |
| S&P 500 vs Nasdaq Composite | 0.854 | 0.78% | -1.01% | **1.79 pp** |
| S&P 500 vs Oro (spot) | -0.059 | 0.78% | 0.00% | **0.78 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.67 | 2026-10-28 | -0.03 |
| US 10Y Treasury Rate | 5.05 | 2026-10-28 | 0.06 |
| US 30Y Treasury Rate | 5.37 | 2026-10-28 | 0.07 |
| Spread 10Y-2Y USA | 0.37 | 2026-10-29 | -0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **38.0 bp**, 30Y-10Y **32.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.9100 | 5.42% | 116.99% | -31.22% |
| Petrolio Brent | 123.1000 | 38.92% | 115.48% | -21.50% |
| Petrolio WTI | 103.3700 | 25.40% | 76.78% | -18.71% |
| Gas naturale | 2.7600 | 1.55% | 72.11% | -18.87% |
| Ethereum | 2 221.2775 | -10.31% | 32.65% | -19.84% |
| Solana | 94.6741 | -12.94% | 32.65% | -22.46% |
| Bitcoin | 77 189.1509 | -6.22% | 23.91% | -10.99% |
| US 5Y Treasury Yield | 4.8500 | -4.15% | 17.16% | -6.09% |
| US 10Y Treasury Yield | 5.0500 | -3.63% | 17.00% | -6.59% |
| Nasdaq Composite | 26 549.8500 | -1.01% | 16.16% | -7.00% |
| US 30Y Treasury Yield | 5.3700 | -3.42% | 14.85% | -6.70% |
| USD/JPY | 156.8700 | -1.68% | 13.95% | -6.19% |
| S&P 500 | 7 743.9800 | 0.78% | 10.91% | -3.42% |
| Dow Jones | 52 342.5600 | 2.82% | 8.94% | -6.34% |
| Indice dollaro Fed (broad) | 121.3202 | n/d | 8.60% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
