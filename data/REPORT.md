# Moneys Monitor - Report di mercato

Generato: `2026-11-05T21:48:11+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-05T21:47:39+00:00` (521 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.49% | 0.00% | **-1.49 pp** |
| 1w | -1.23% | 0.00% | **-1.23 pp** |
| 1m | -3.64% | 0.00% | **-3.64 pp** |
| 3m | -3.50% | 0.00% | **-3.50 pp** |
| 6m | 12.80% | 16.18% | **-3.37 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Dow Jones | 3.03% | | VIX (volatilita) | -20.26% |
| 2 | S&P 500 | 1.58% | | Petrolio Brent | -13.05% |
| 3 | Nasdaq Composite | 1.44% | | Ethereum | -7.69% |
| 4 | USD/JPY | 0.38% | | Bitcoin | -5.33% |
| 5 | Indice dollaro Fed (broad) | 0.28% | | Solana | -4.88% |
| 6 | GBP/USD | 0.17% | | Gas naturale | -4.71% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 3.62% | | Gas naturale | -17.30% |
| 2 | Dow Jones | 1.68% | | Solana | -6.18% |
| 3 | GBP/USD | 1.12% | | Petrolio Brent | -6.08% |
| 4 | Indice dollaro Fed (broad) | 1.11% | | US 5Y Treasury Yield | -3.30% |
| 5 | EUR/USD | 0.84% | | US 10Y Treasury Yield | -2.97% |
| 6 | USD/JPY | 0.18% | | Nasdaq Composite | -2.80% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 20.92% | | Solana | -14.53% |
| 2 | Petrolio Brent | 20.91% | | Ethereum | -8.44% |
| 3 | VIX (volatilita) | 10.66% | | US 10Y Treasury Yield | -7.72% |
| 4 | Dow Jones | 3.56% | | Bitcoin | -7.59% |
| 5 | EUR/USD | 0.42% | | US 5Y Treasury Yield | -7.31% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -6.71% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.494 | -0.44% | 10.66% | **-11.10 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.020 | -7.72% | 0.00% | **-7.72 pp** |
| S&P 500 vs Bitcoin | -0.155 | -0.44% | -7.59% | **7.15 pp** |
| S&P 500 vs Nasdaq Composite | 0.817 | -0.44% | -5.35% | **4.91 pp** |
| S&P 500 vs Oro (spot) | -0.109 | -0.44% | 0.00% | **-0.44 pp** |
| EUR/USD vs Indice dollaro DXY | 0.031 | 0.42% | 0.00% | **0.42 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.58 | 2026-11-04 | -0.03 |
| US 10Y Treasury Rate | 4.90 | 2026-11-04 | -0.05 |
| US 30Y Treasury Rate | 5.28 | 2026-11-04 | -0.04 |
| Spread 10Y-2Y USA | 0.32 | 2026-11-04 | -0.02 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.6100 | 10.66% | 146.80% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 232.5702 | -8.44% | 45.54% | -19.43% |
| Solana | 89.9913 | -14.53% | 35.47% | -26.30% |
| Bitcoin | 75 876.0295 | -7.59% | 32.33% | -12.50% |
| Nasdaq Composite | 25 736.5100 | -5.35% | 21.53% | -8.82% |
| US 5Y Treasury Yield | 4.6900 | -7.31% | 17.32% | -7.86% |
| US 10Y Treasury Yield | 4.9000 | -7.72% | 17.06% | -7.72% |
| US 30Y Treasury Yield | 5.2800 | -6.71% | 14.58% | -6.88% |
| S&P 500 | 7 688.6200 | -0.44% | 14.23% | -3.55% |
| Dow Jones | 53 356.1200 | 3.56% | 14.22% | -6.34% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
