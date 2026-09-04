# Moneys Monitor - Report di mercato

Generato: `2026-09-04T23:10:54+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-04T23:10:18+00:00` (322 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.33% | 0.00% | **-0.33 pp** |
| 1w | 0.49% | 0.00% | **0.49 pp** |
| 1m | 8.48% | 4.71% | **3.77 pp** |
| 3m | 12.97% | 15.30% | **-2.33 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | VIX (volatilita) | -5.79% |
| 2 | Petrolio Brent | 9.44% | | Solana | -2.01% |
| 3 | Gas naturale | 3.83% | | Bitcoin | -1.90% |
| 4 | Nasdaq Composite | 1.40% | | Ethereum | -1.83% |
| 5 | S&P 500 | 1.06% | | GBP/USD | -0.62% |
| 6 | Indice dollaro Fed (broad) | 0.58% | | Dow Jones | -0.51% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | VIX (volatilita) | -1.31% |
| 2 | US 5Y Treasury Yield | 3.20% | | GBP/USD | -0.65% |
| 3 | Gas naturale | 3.17% | | Dow Jones | -0.27% |
| 4 | Bitcoin | 2.78% | | EUR/USD | -0.18% |
| 5 | US 10Y Treasury Yield | 2.14% | | FTSE MIB | 0.00% |
| 6 | Petrolio Brent | 1.73% | | Euro Stoxx 50 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 34.12% | | VIX (volatilita) | -6.28% |
| 2 | Ethereum | 30.06% | | CAC 40 Francia | -2.57% |
| 3 | Bitcoin | 25.48% | | Nikkei 225 | -2.47% |
| 4 | Petrolio WTI | 21.65% | | FTSE MIB | -1.80% |
| 5 | Petrolio Brent | 20.57% | | Shanghai Composite | -1.45% |
| 6 | Gas naturale | 7.77% | | Russell 2000 | -1.26% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.016 | -0.07% | 25.48% | **-25.55 pp** |
| S&P 500 vs VIX (volatilita) | -0.033 | -0.07% | -6.28% | **6.21 pp** |
| S&P 500 vs Oro (spot) | 0.085 | -0.07% | 5.05% | **-5.12 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.030 | 1.84% | 5.05% | **-3.21 pp** |
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
| US 2Y Treasury Rate | 4.34 | 2026-09-03 | -0.05 |
| US 10Y Treasury Rate | 4.77 | 2026-09-03 | -0.02 |
| US 30Y Treasury Rate | 5.25 | 2026-09-03 | -0.02 |
| Spread 10Y-2Y USA | 0.41 | 2026-09-04 | -0.02 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **43.0 bp**, 30Y-10Y **48.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.3200 | -6.28% | 75.32% | -31.03% |
| Ethereum | 2 451.5248 | 30.06% | 56.09% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 101.8116 | 34.12% | 47.53% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 79 660.6401 | 25.48% | 43.18% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 4.36% | 24.41% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.05% | 16.75% | -4.96% |
| US 5Y Treasury Yield | 4.5200 | n/d | 16.50% | -0.66% |
| Nikkei 225 | 65 856.4300 | -2.47% | 16.07% | -12.83% |
| Nasdaq Composite | 26 584.0600 | -0.08% | 12.07% | -7.00% |
| US 10Y Treasury Yield | 4.7700 | 1.84% | 11.65% | -2.70% |
| Hang Seng | 25 511.1000 | 0.28% | 10.74% | -3.43% |
| Rame | 6.6680 | 0.92% | 10.54% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
