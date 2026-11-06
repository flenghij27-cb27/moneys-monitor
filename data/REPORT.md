# Moneys Monitor - Report di mercato

Generato: `2026-11-06T21:20:59+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-06T21:20:24+00:00` (524 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.01% | 0.00% | **-1.01 pp** |
| 1w | -2.11% | 0.00% | **-2.11 pp** |
| 1m | -4.56% | 0.00% | **-4.56 pp** |
| 3m | -3.93% | 0.00% | **-3.93 pp** |
| 6m | 10.91% | 15.30% | **-4.39 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 69.66% | | Petrolio Brent | -13.05% |
| 2 | USD/JPY | 0.38% | | Nasdaq Composite | -5.52% |
| 3 | Indice dollaro Fed (broad) | 0.28% | | Gas naturale | -4.71% |
| 4 | GBP/USD | 0.17% | | S&P 500 | -4.36% |
| 5 | FTSE MIB | 0.00% | | Petrolio WTI | -3.61% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -3.44% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 63.84% | | Gas naturale | -17.30% |
| 2 | Petrolio WTI | 3.62% | | Nasdaq Composite | -8.42% |
| 3 | GBP/USD | 1.12% | | Petrolio Brent | -6.08% |
| 4 | Indice dollaro Fed (broad) | 1.11% | | S&P 500 | -5.04% |
| 5 | USD/JPY | 0.18% | | Solana | -4.03% |
| 6 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -3.30% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 86.87% | | Solana | -13.72% |
| 2 | Petrolio WTI | 20.92% | | Nasdaq Composite | -11.51% |
| 3 | Petrolio Brent | 20.91% | | Ethereum | -7.96% |
| 4 | Dow Jones | 0.67% | | US 10Y Treasury Yield | -7.72% |
| 5 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -7.31% |
| 6 | Euro Stoxx 50 | 0.00% | | Bitcoin | -7.03% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.674 | -5.41% | 86.87% | **-92.28 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.012 | -7.72% | 0.00% | **-7.72 pp** |
| S&P 500 vs Nasdaq Composite | 0.858 | -5.41% | -11.51% | **6.10 pp** |
| S&P 500 vs Oro (spot) | -0.082 | -5.41% | 0.00% | **-5.41 pp** |
| S&P 500 vs Bitcoin | -0.125 | -5.41% | -7.03% | **1.62 pp** |
| EUR/USD vs Indice dollaro DXY | 0.029 | -0.19% | 0.00% | **-0.19 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.58 | 2026-11-04 | -0.03 |
| US 10Y Treasury Rate | 4.90 | 2026-11-04 | -0.05 |
| US 30Y Treasury Rate | 5.28 | 2026-11-04 | -0.04 |
| Spread 10Y-2Y USA | 0.38 | 2026-11-05 | 0.06 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 28.1800 | 86.87% | 285.02% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 228.7346 | -7.96% | 45.46% | -19.57% |
| Solana | 89.9805 | -13.72% | 35.53% | -26.31% |
| Bitcoin | 75 817.0960 | -7.03% | 32.34% | -12.57% |
| Nasdaq Composite | 24 315.0000 | -11.51% | 28.13% | -11.90% |
| S&P 500 | 7 353.7300 | -5.41% | 20.66% | -5.95% |
| Dow Jones | 51 523.0600 | 0.67% | 19.24% | -6.34% |
| US 5Y Treasury Yield | 4.6900 | -7.31% | 17.32% | -7.86% |
| US 10Y Treasury Yield | 4.9000 | -7.72% | 17.06% | -7.72% |
| US 30Y Treasury Yield | 5.2800 | -6.71% | 14.58% | -6.88% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
