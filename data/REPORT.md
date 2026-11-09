# Moneys Monitor - Report di mercato

Generato: `2026-11-09T15:28:02+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-09T15:27:30+00:00` (532 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.08% | 0.00% | **-1.08 pp** |
| 1w | -3.71% | 0.00% | **-3.71 pp** |
| 1m | -5.20% | 0.00% | **-5.20 pp** |
| 3m | -4.72% | 0.00% | **-4.72 pp** |
| 6m | 6.02% | 10.40% | **-4.38 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 69.66% | | Petrolio Brent | -13.05% |
| 2 | Nasdaq Composite | 1.09% | | Gas naturale | -4.71% |
| 3 | USD/JPY | 0.38% | | S&P 500 | -4.36% |
| 4 | Indice dollaro Fed (broad) | 0.28% | | Ethereum | -4.26% |
| 5 | EUR/USD | 0.25% | | Petrolio WTI | -3.61% |
| 6 | GBP/USD | 0.17% | | Solana | -2.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 63.84% | | Gas naturale | -17.30% |
| 2 | Petrolio WTI | 3.62% | | Ethereum | -11.87% |
| 3 | GBP/USD | 1.12% | | Solana | -7.64% |
| 4 | Indice dollaro Fed (broad) | 1.11% | | Bitcoin | -6.39% |
| 5 | USD/JPY | 0.18% | | Nasdaq Composite | -6.13% |
| 6 | FTSE MIB | 0.00% | | Petrolio Brent | -6.08% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 86.87% | | Solana | -16.26% |
| 2 | Petrolio WTI | 20.92% | | Ethereum | -11.05% |
| 3 | Petrolio Brent | 20.91% | | Nasdaq Composite | -10.94% |
| 4 | Dow Jones | 0.11% | | US 5Y Treasury Yield | -8.75% |
| 5 | FTSE MIB | 0.00% | | Bitcoin | -8.38% |
| 6 | Euro Stoxx 50 | 0.00% | | US 10Y Treasury Yield | -8.16% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.674 | -5.41% | 86.87% | **-92.28 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.085 | -8.16% | 0.00% | **-8.16 pp** |
| S&P 500 vs Nasdaq Composite | -0.055 | -5.41% | -10.94% | **5.53 pp** |
| S&P 500 vs Oro (spot) | 0.046 | -5.41% | 0.00% | **-5.41 pp** |
| S&P 500 vs Bitcoin | 0.052 | -5.41% | -8.38% | **2.97 pp** |
| EUR/USD vs Indice dollaro DXY | -0.132 | -0.12% | 0.00% | **-0.12 pp** |
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
| Ethereum | 2 131.5546 | -11.05% | 46.85% | -23.08% |
| Solana | 87.3817 | -16.26% | 34.62% | -28.43% |
| Bitcoin | 75 026.5107 | -8.38% | 31.95% | -13.48% |
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
