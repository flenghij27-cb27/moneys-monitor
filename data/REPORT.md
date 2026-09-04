# Moneys Monitor - Report di mercato

Generato: `2026-09-04T15:54:41+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-04T15:54:09+00:00` (320 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.36% | 0.00% | **-0.36 pp** |
| 1w | 0.46% | 0.00% | **0.46 pp** |
| 1m | 8.43% | 4.71% | **3.73 pp** |
| 3m | 12.93% | 15.30% | **-2.37 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | VIX (volatilita) | -5.79% |
| 2 | Petrolio Brent | 9.44% | | Solana | -2.25% |
| 3 | Gas naturale | 3.83% | | Bitcoin | -2.11% |
| 4 | Nasdaq Composite | 1.40% | | Ethereum | -1.68% |
| 5 | Dow Jones | 1.18% | | GBP/USD | -0.62% |
| 6 | S&P 500 | 1.06% | | US 5Y Treasury Yield | -0.22% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | VIX (volatilita) | -1.31% |
| 2 | US 5Y Treasury Yield | 3.89% | | GBP/USD | -0.65% |
| 3 | Gas naturale | 3.17% | | EUR/USD | -0.18% |
| 4 | US 10Y Treasury Yield | 2.79% | | Solana | -0.05% |
| 5 | Bitcoin | 2.55% | | FTSE MIB | 0.00% |
| 6 | US 30Y Treasury Yield | 1.74% | | Euro Stoxx 50 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 33.79% | | VIX (volatilita) | -6.28% |
| 2 | Ethereum | 30.25% | | CAC 40 Francia | -2.57% |
| 3 | Bitcoin | 25.20% | | Nikkei 225 | -2.47% |
| 4 | Petrolio WTI | 21.65% | | FTSE MIB | -1.80% |
| 5 | Petrolio Brent | 20.57% | | Shanghai Composite | -1.45% |
| 6 | Gas naturale | 7.77% | | Russell 2000 | -1.26% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.019 | -0.07% | 25.20% | **-25.27 pp** |
| S&P 500 vs VIX (volatilita) | -0.033 | -0.07% | -6.28% | **6.21 pp** |
| S&P 500 vs Oro (spot) | 0.085 | -0.07% | 5.05% | **-5.12 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.075 | 1.94% | 5.05% | **-3.11 pp** |
| EUR/USD vs Indice dollaro DXY | -0.115 | 0.67% | -1.04% | **1.71 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.05% | 4.36% | **0.69 pp** |
| S&P 500 vs Nasdaq Composite | 0.954 | -0.07% | -0.08% | **0.01 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.39 | 2026-09-02 | 0.00 |
| US 10Y Treasury Rate | 4.79 | 2026-09-02 | 0.00 |
| US 30Y Treasury Rate | 5.27 | 2026-09-02 | 0.00 |
| Spread 10Y-2Y USA | 0.43 | 2026-09-03 | 0.03 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **40.0 bp**, 30Y-10Y **48.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.3200 | -6.28% | 75.32% | -31.03% |
| Ethereum | 2 455.1016 | 30.25% | 55.98% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 101.5572 | 33.79% | 47.78% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 79 486.6854 | 25.20% | 43.39% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 4.36% | 24.41% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.05% | 16.75% | -4.96% |
| US 5Y Treasury Yield | 4.5400 | n/d | 16.23% | -0.22% |
| Nikkei 225 | 65 856.4300 | -2.47% | 16.07% | -12.83% |
| Nasdaq Composite | 26 584.0600 | -0.08% | 12.07% | -7.00% |
| US 10Y Treasury Yield | 4.7900 | 1.94% | 11.51% | -2.70% |
| Hang Seng | 25 511.1000 | 0.28% | 10.74% | -3.43% |
| Rame | 6.6680 | 0.92% | 10.54% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
