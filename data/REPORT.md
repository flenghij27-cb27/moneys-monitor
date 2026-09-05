# Moneys Monitor - Report di mercato

Generato: `2026-09-05T14:45:12+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-05T14:44:36+00:00` (324 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.06% | 0.00% | **0.06 pp** |
| 1w | 0.06% | 0.00% | **0.06 pp** |
| 1m | 8.53% | 6.10% | **2.43 pp** |
| 3m | 11.24% | 12.43% | **-1.19 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | VIX (volatilita) | -5.79% |
| 2 | Petrolio Brent | 9.44% | | GBP/USD | -0.62% |
| 3 | Gas naturale | 3.83% | | Dow Jones | -0.51% |
| 4 | Solana | 0.98% | | US 5Y Treasury Yield | -0.44% |
| 5 | Indice dollaro Fed (broad) | 0.58% | | US 10Y Treasury Yield | -0.42% |
| 6 | USD/JPY | 0.47% | | S&P 500 | -0.38% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | VIX (volatilita) | -1.31% |
| 2 | US 5Y Treasury Yield | 3.20% | | GBP/USD | -0.65% |
| 3 | Gas naturale | 3.17% | | Ethereum | -0.56% |
| 4 | US 10Y Treasury Yield | 2.14% | | Solana | -0.47% |
| 5 | Petrolio Brent | 1.73% | | Dow Jones | -0.27% |
| 6 | Bitcoin | 1.17% | | EUR/USD | -0.18% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 34.84% | | VIX (volatilita) | -6.28% |
| 2 | Ethereum | 30.23% | | Nikkei 225 | -3.59% |
| 3 | Bitcoin | 25.77% | | CAC 40 Francia | -2.29% |
| 4 | Petrolio WTI | 21.65% | | FTSE MIB | -1.79% |
| 5 | Petrolio Brent | 20.57% | | Russell 2000 | -1.50% |
| 6 | Gas naturale | 7.77% | | Euro Stoxx 50 | -1.28% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.014 | -0.12% | 25.77% | **-25.89 pp** |
| S&P 500 vs Oro (spot) | 0.087 | -0.12% | 6.49% | **-6.61 pp** |
| S&P 500 vs VIX (volatilita) | -0.676 | -0.12% | -6.28% | **6.16 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.072 | 1.84% | 6.49% | **-4.65 pp** |
| EUR/USD vs Indice dollaro DXY | 0.034 | 0.67% | -1.01% | **1.68 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 6.49% | 5.71% | **0.78 pp** |
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
| VIX (volatilita) | 14.3200 | -6.28% | 75.32% | -31.03% |
| Ethereum | 2 457.4838 | 30.23% | 55.83% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 102.8118 | 34.84% | 46.26% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 79 726.1582 | 25.77% | 42.75% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 5.71% | 24.43% | -11.21% |
| Oro (spot) | 4 693.0000 | 6.49% | 16.77% | -4.96% |
| US 5Y Treasury Yield | 4.5200 | n/d | 16.50% | -0.66% |
| Nikkei 225 | 65 856.4300 | -3.59% | 15.83% | -12.83% |
| Nasdaq Composite | 26 506.9900 | 0.23% | 11.96% | -7.00% |
| US 10Y Treasury Yield | 4.7700 | 1.84% | 11.65% | -2.70% |
| Rame | 6.6680 | 1.26% | 10.49% | -4.19% |
| Shanghai Composite | 3 889.4450 | -0.96% | 10.44% | -8.47% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
