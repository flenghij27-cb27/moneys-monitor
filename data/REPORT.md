# Moneys Monitor - Report di mercato

Generato: `2026-09-11T23:29:30+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-11T23:28:56+00:00` (346 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.57% | 0.00% | **0.57 pp** |
| 1w | -0.85% | 0.00% | **-0.85 pp** |
| 1m | 5.44% | 2.72% | **2.72 pp** |
| 3m | 12.09% | 15.60% | **-3.51 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | VIX (volatilita) | 8.38% | | USD/JPY | -2.41% |
| 3 | Petrolio WTI | 6.32% | | Nasdaq Composite | -0.65% |
| 4 | Solana | 3.29% | | S&P 500 | -0.58% |
| 5 | US 5Y Treasury Yield | 3.04% | | Indice dollaro Fed (broad) | -0.57% |
| 6 | Ethereum | 3.01% | | GBP/USD | -0.25% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 17.37% | | Bitcoin | -3.60% |
| 2 | Petrolio Brent | 16.02% | | Solana | -3.53% |
| 3 | Petrolio WTI | 11.72% | | Dow Jones | -2.07% |
| 4 | US 5Y Treasury Yield | 4.63% | | USD/JPY | -1.78% |
| 5 | US 10Y Treasury Yield | 3.34% | | S&P 500 | -0.98% |
| 6 | US 30Y Treasury Yield | 1.90% | | GBP/USD | -0.93% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | S&P 500 | -2.49% |
| 2 | Petrolio WTI | 26.39% | | Nasdaq Composite | -2.42% |
| 3 | VIX (volatilita) | 25.19% | | Dow Jones | -2.16% |
| 4 | Solana | 24.14% | | USD/JPY | -1.10% |
| 5 | Ethereum | 19.01% | | Russell 2000 | -0.85% |
| 6 | Bitcoin | 12.50% | | CAC 40 Francia | -0.58% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.088 | -2.49% | 25.19% | **-27.68 pp** |
| S&P 500 vs Bitcoin | 0.008 | -2.49% | 12.50% | **-14.99 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| S&P 500 vs Oro (spot) | 0.061 | -2.49% | 2.74% | **-5.23 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.018 | 5.41% | 2.74% | **2.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -2.49% | -2.42% | **-0.07 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 2.74% | 2.70% | **0.04 pp** |
| EUR/USD vs Indice dollaro DXY | -0.018 | 0.16% | 0.16% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.56 | 2026-09-10 | 0.13 |
| US 10Y Treasury Rate | 4.95 | 2026-09-10 | 0.12 |
| US 30Y Treasury Rate | 5.37 | 2026-09-10 | 0.09 |
| Spread 10Y-2Y USA | 0.33 | 2026-09-11 | -0.06 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **39.0 bp**, 30Y-10Y **42.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.8400 | 25.19% | 84.34% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 102.2066 | 24.14% | 44.01% | -13.59% |
| Bitcoin | 77 168.2584 | 12.50% | 35.41% | -5.72% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 513.0431 | 19.01% | 32.33% | -5.78% |
| US 5Y Treasury Yield | 4.7500 | n/d | 17.44% | -0.66% |
| US 10Y Treasury Yield | 4.9500 | 5.41% | 13.43% | -2.70% |
| Nasdaq Composite | 26 081.7200 | -2.42% | 11.92% | -7.00% |
| Dow Jones | 52 573.2900 | -2.16% | 11.11% | -4.20% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| US 30Y Treasury Yield | 5.3700 | n/d | 9.14% | -0.57% |
| S&P 500 | 7 591.7000 | -2.49% | 8.33% | -3.42% |
| Hang Seng | 25 511.1000 | 0.06% | 8.16% | -3.43% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
