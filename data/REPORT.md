# Moneys Monitor - Report di mercato

Generato: `2026-09-13T11:15:50+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-13T11:15:18+00:00` (351 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.33% | 0.00% | **-0.33 pp** |
| 1w | -0.88% | 0.00% | **-0.88 pp** |
| 1m | 0.78% | -0.57% | **1.34 pp** |
| 3m | 9.87% | 13.62% | **-3.75 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | VIX (volatilita) | 8.38% | | USD/JPY | -2.41% |
| 3 | Petrolio WTI | 6.32% | | Ethereum | -2.10% |
| 4 | US 5Y Treasury Yield | 3.04% | | Solana | -2.04% |
| 5 | US 10Y Treasury Yield | 2.48% | | Bitcoin | -0.93% |
| 6 | US 30Y Treasury Yield | 1.70% | | Indice dollaro Fed (broad) | -0.57% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 17.37% | | Solana | -3.69% |
| 2 | Petrolio Brent | 16.02% | | Bitcoin | -2.44% |
| 3 | Petrolio WTI | 11.72% | | Dow Jones | -2.07% |
| 4 | US 5Y Treasury Yield | 4.63% | | USD/JPY | -1.78% |
| 5 | US 10Y Treasury Yield | 3.34% | | S&P 500 | -1.17% |
| 6 | US 30Y Treasury Yield | 1.90% | | Nasdaq Composite | -0.94% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Dow Jones | -2.16% |
| 2 | Petrolio WTI | 26.39% | | Hang Seng | -1.92% |
| 3 | VIX (volatilita) | 25.19% | | S&P 500 | -1.65% |
| 4 | Solana | 8.89% | | Argento (spot) | -1.54% |
| 5 | US 10Y Treasury Yield | 5.41% | | Nasdaq Composite | -1.48% |
| 6 | Gas naturale | 5.20% | | Bitcoin | -1.16% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.639 | -1.65% | 25.19% | **-26.84 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.135 | 5.41% | 0.41% | **5.00 pp** |
| S&P 500 vs Oro (spot) | 0.181 | -1.65% | 0.41% | **-2.06 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 0.41% | -1.54% | **1.95 pp** |
| S&P 500 vs Bitcoin | 0.105 | -1.65% | -1.16% | **-0.49 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -1.65% | -1.48% | **-0.17 pp** |
| EUR/USD vs Indice dollaro DXY | 0.056 | 0.16% | 0.13% | **0.03 pp** |

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
| Solana | 99.6043 | 8.89% | 41.03% | -13.59% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 470.5540 | 1.71% | 29.29% | -5.78% |
| Bitcoin | 76 534.9111 | -1.16% | 27.00% | -5.75% |
| US 5Y Treasury Yield | 4.7500 | n/d | 17.44% | -0.66% |
| US 10Y Treasury Yield | 4.9500 | 5.41% | 13.43% | -2.70% |
| Nasdaq Composite | 26 333.0400 | -1.48% | 12.52% | -7.00% |
| Dow Jones | 52 573.2900 | -2.16% | 11.11% | -4.20% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| US 30Y Treasury Yield | 5.3700 | n/d | 9.14% | -0.57% |
| S&P 500 | 7 656.9800 | -1.65% | 9.03% | -3.42% |
| Hang Seng | 25 511.1000 | -1.92% | 6.71% | -3.43% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
