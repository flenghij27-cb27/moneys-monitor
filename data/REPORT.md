# Moneys Monitor - Report di mercato

Generato: `2026-09-06T18:05:25+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-06T18:04:53+00:00` (329 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.27% | 0.00% | **0.27 pp** |
| 1w | 1.34% | 0.00% | **1.34 pp** |
| 1m | 9.37% | 5.63% | **3.74 pp** |
| 3m | 10.50% | 10.40% | **0.10 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | VIX (volatilita) | -5.79% |
| 2 | Petrolio Brent | 9.44% | | GBP/USD | -0.62% |
| 3 | Gas naturale | 3.83% | | Dow Jones | -0.51% |
| 4 | Solana | 2.84% | | US 5Y Treasury Yield | -0.44% |
| 5 | Indice dollaro Fed (broad) | 0.58% | | US 10Y Treasury Yield | -0.42% |
| 6 | Ethereum | 0.54% | | S&P 500 | -0.38% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 6.46% | | VIX (volatilita) | -1.31% |
| 2 | Petrolio WTI | 5.08% | | GBP/USD | -0.65% |
| 3 | Ethereum | 3.27% | | Dow Jones | -0.27% |
| 4 | US 5Y Treasury Yield | 3.20% | | EUR/USD | -0.18% |
| 5 | Bitcoin | 3.19% | | FTSE MIB | 0.00% |
| 6 | Gas naturale | 3.17% | | Euro Stoxx 50 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 41.45% | | VIX (volatilita) | -6.28% |
| 2 | Ethereum | 32.71% | | Nikkei 225 | -4.16% |
| 3 | Bitcoin | 26.84% | | CAC 40 Francia | -2.14% |
| 4 | Petrolio WTI | 21.65% | | Russell 2000 | -2.00% |
| 5 | Petrolio Brent | 20.57% | | FTSE MIB | -1.59% |
| 6 | Gas naturale | 7.77% | | Euro Stoxx 50 | -1.19% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.092 | -0.12% | 26.84% | **-26.96 pp** |
| S&P 500 vs VIX (volatilita) | -0.676 | -0.12% | -6.28% | **6.16 pp** |
| S&P 500 vs Oro (spot) | 0.167 | -0.12% | 5.96% | **-6.08 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.182 | 1.84% | 5.96% | **-4.12 pp** |
| EUR/USD vs Indice dollaro DXY | -0.015 | 0.67% | -0.69% | **1.36 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.96% | 5.30% | **0.66 pp** |
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
| Ethereum | 2 492.5288 | 32.71% | 55.58% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 106.2437 | 41.45% | 46.12% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 79 760.6192 | 26.84% | 42.80% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 5.30% | 24.44% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.96% | 16.80% | -4.96% |
| US 5Y Treasury Yield | 4.5200 | n/d | 16.50% | -0.66% |
| Nikkei 225 | 65 856.4300 | -4.16% | 15.83% | -12.83% |
| Nasdaq Composite | 26 506.9900 | 0.23% | 11.96% | -7.00% |
| US 10Y Treasury Yield | 4.7700 | 1.84% | 11.65% | -2.70% |
| Rame | 6.6680 | 0.92% | 10.49% | -4.19% |
| Shanghai Composite | 3 889.4450 | -0.96% | 10.44% | -8.47% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
