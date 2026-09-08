# Moneys Monitor - Report di mercato

Generato: `2026-09-08T16:11:54+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-08T16:10:09+00:00` (335 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.03% | 0.00% | **-0.03 pp** |
| 1w | -0.24% | 0.00% | **-0.24 pp** |
| 1m | 8.82% | 5.32% | **3.50 pp** |
| 3m | 10.24% | 10.40% | **-0.16 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | GBP/USD | -0.62% |
| 2 | Petrolio Brent | 9.44% | | Dow Jones | -0.51% |
| 3 | VIX (volatilita) | 6.84% | | US 5Y Treasury Yield | -0.44% |
| 4 | Gas naturale | 3.83% | | US 10Y Treasury Yield | -0.42% |
| 5 | Indice dollaro Fed (broad) | 0.58% | | S&P 500 | -0.38% |
| 6 | USD/JPY | 0.47% | | US 30Y Treasury Yield | -0.38% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 6.03% | | Bitcoin | -2.99% |
| 2 | Petrolio WTI | 5.08% | | GBP/USD | -0.65% |
| 3 | US 5Y Treasury Yield | 3.20% | | Dow Jones | -0.27% |
| 4 | Gas naturale | 3.17% | | Ethereum | -0.06% |
| 5 | US 10Y Treasury Yield | 2.14% | | FTSE MIB | 0.00% |
| 6 | Petrolio Brent | 1.73% | | Euro Stoxx 50 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 38.32% | | Nikkei 225 | -4.16% |
| 2 | Ethereum | 32.39% | | CAC 40 Francia | -2.14% |
| 3 | Bitcoin | 24.91% | | Russell 2000 | -2.00% |
| 4 | Petrolio WTI | 21.65% | | FTSE MIB | -1.59% |
| 5 | Petrolio Brent | 20.57% | | Euro Stoxx 50 | -1.19% |
| 6 | Gas naturale | 7.77% | | Shanghai Composite | -0.96% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.015 | -0.12% | 24.91% | **-25.03 pp** |
| S&P 500 vs Oro (spot) | 0.055 | -0.12% | 5.76% | **-5.88 pp** |
| S&P 500 vs VIX (volatilita) | -0.048 | -0.12% | 5.15% | **-5.27 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.137 | 1.84% | 5.76% | **-3.92 pp** |
| EUR/USD vs Indice dollaro DXY | -0.016 | 0.72% | -0.68% | **1.40 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.76% | 4.89% | **0.87 pp** |
| S&P 500 vs Nasdaq Composite | 0.953 | -0.12% | 0.23% | **-0.35 pp** |

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
| VIX (volatilita) | 15.3000 | 5.15% | 79.12% | -31.03% |
| Ethereum | 2 495.5902 | 32.39% | 56.08% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 104.0146 | 38.32% | 47.64% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 78 771.2003 | 24.91% | 43.68% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 4.89% | 24.11% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.76% | 16.71% | -4.96% |
| US 5Y Treasury Yield | 4.5200 | n/d | 16.50% | -0.66% |
| Nikkei 225 | 65 856.4300 | -4.16% | 15.46% | -12.83% |
| Nasdaq Composite | 26 506.9900 | 0.23% | 11.96% | -7.00% |
| US 10Y Treasury Yield | 4.7700 | 1.84% | 11.65% | -2.70% |
| Rame | 6.6680 | 0.83% | 10.49% | -4.19% |
| Dow Jones | 53 414.2500 | -0.70% | 9.12% | -2.93% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
