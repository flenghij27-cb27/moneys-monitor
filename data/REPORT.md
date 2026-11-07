# Moneys Monitor - Report di mercato

Generato: `2026-11-07T12:37:04+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-07T12:36:33+00:00` (526 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.27% | 0.00% | **-0.27 pp** |
| 1w | -1.46% | 0.00% | **-1.46 pp** |
| 1m | -4.23% | 0.00% | **-4.23 pp** |
| 3m | -3.96% | 0.00% | **-3.96 pp** |
| 6m | 9.19% | 12.43% | **-3.24 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 69.66% | | Petrolio Brent | -13.05% |
| 2 | Nasdaq Composite | 1.09% | | Gas naturale | -4.71% |
| 3 | Ethereum | 0.59% | | S&P 500 | -4.36% |
| 4 | USD/JPY | 0.38% | | Petrolio WTI | -3.61% |
| 5 | Indice dollaro Fed (broad) | 0.28% | | US 5Y Treasury Yield | -2.13% |
| 6 | GBP/USD | 0.17% | | US 10Y Treasury Yield | -1.22% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 63.84% | | Gas naturale | -17.30% |
| 2 | Petrolio WTI | 3.62% | | Nasdaq Composite | -6.13% |
| 3 | GBP/USD | 1.12% | | Petrolio Brent | -6.08% |
| 4 | Indice dollaro Fed (broad) | 1.11% | | S&P 500 | -5.04% |
| 5 | USD/JPY | 0.18% | | US 5Y Treasury Yield | -3.97% |
| 6 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -2.81% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 86.87% | | Solana | -12.92% |
| 2 | Petrolio WTI | 20.92% | | Nasdaq Composite | -10.94% |
| 3 | Petrolio Brent | 20.91% | | US 5Y Treasury Yield | -8.75% |
| 4 | Dow Jones | 0.11% | | US 10Y Treasury Yield | -8.16% |
| 5 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -6.91% |
| 6 | Euro Stoxx 50 | 0.00% | | Bitcoin | -6.63% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.674 | -5.41% | 86.87% | **-92.28 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.014 | -8.16% | 0.00% | **-8.16 pp** |
| S&P 500 vs Nasdaq Composite | -0.055 | -5.41% | -10.94% | **5.53 pp** |
| S&P 500 vs Oro (spot) | -0.006 | -5.41% | 0.00% | **-5.41 pp** |
| S&P 500 vs Bitcoin | 0.075 | -5.41% | -6.63% | **1.22 pp** |
| EUR/USD vs Indice dollaro DXY | -0.128 | -0.19% | 0.00% | **-0.19 pp** |
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
| US 2Y Treasury Rate | 4.46 | 2026-11-05 | -0.12 |
| US 10Y Treasury Rate | 4.84 | 2026-11-05 | -0.06 |
| US 30Y Treasury Rate | 5.25 | 2026-11-05 | -0.03 |
| Spread 10Y-2Y USA | 0.35 | 2026-11-06 | -0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **38.0 bp**, 30Y-10Y **41.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 28.1800 | 86.87% | 285.02% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 241.8793 | -6.38% | 45.48% | -19.57% |
| Solana | 89.8714 | -12.92% | 35.17% | -26.40% |
| Bitcoin | 75 904.6630 | -6.63% | 32.07% | -12.57% |
| Nasdaq Composite | 24 579.4200 | -10.94% | 28.75% | -11.90% |
| S&P 500 | 7 353.7300 | -5.41% | 20.66% | -5.95% |
| Dow Jones | 51 285.7300 | 0.11% | 19.08% | -6.34% |
| US 5Y Treasury Yield | 4.5900 | -8.75% | 18.38% | -9.82% |
| US 10Y Treasury Yield | 4.8400 | -8.16% | 17.19% | -8.85% |
| US 30Y Treasury Yield | 5.2500 | -6.91% | 14.24% | -7.41% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
