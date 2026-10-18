# Moneys Monitor - Report di mercato

Generato: `2026-10-18T15:31:18+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-18T15:30:45+00:00` (464 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.30% | 0.00% | **-0.30 pp** |
| 1w | -1.63% | 0.00% | **-1.63 pp** |
| 1m | -2.87% | 0.00% | **-2.87 pp** |
| 3m | 9.62% | 5.63% | **3.99 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.27% | | VIX (volatilita) | -2.43% |
| 2 | Petrolio WTI | 5.89% | | US 5Y Treasury Yield | -1.80% |
| 3 | Petrolio Brent | 0.88% | | US 10Y Treasury Yield | -1.73% |
| 4 | EUR/USD | 0.40% | | US 30Y Treasury Yield | -1.63% |
| 5 | USD/JPY | 0.34% | | S&P 500 | -1.09% |
| 6 | Indice dollaro Fed (broad) | 0.18% | | Solana | -1.06% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 15.56% | | Ethereum | -5.24% |
| 2 | Gas naturale | 14.59% | | Solana | -4.60% |
| 3 | VIX (volatilita) | 6.81% | | US 30Y Treasury Yield | -4.23% |
| 4 | Petrolio WTI | 4.78% | | US 10Y Treasury Yield | -3.41% |
| 5 | Indice dollaro Fed (broad) | 2.99% | | Bitcoin | -2.71% |
| 6 | USD/JPY | 1.43% | | US 5Y Treasury Yield | -2.39% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -16.37% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -11.50% |
| 3 | Gas naturale | 15.16% | | Bitcoin | -3.97% |
| 4 | VIX (volatilita) | 3.91% | | GBP/USD | -2.05% |
| 5 | Nasdaq Composite | 2.83% | | EUR/USD | -1.99% |
| 6 | US 10Y Treasury Yield | 2.00% | | USD/JPY | -0.63% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs Bitcoin | 0.209 | 0.28% | -3.97% | **4.25 pp** |
| S&P 500 vs VIX (volatilita) | -0.022 | 0.28% | 3.91% | **-3.63 pp** |
| S&P 500 vs Nasdaq Composite | 0.100 | 0.28% | 2.83% | **-2.55 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.024 | 2.00% | 0.00% | **2.00 pp** |
| EUR/USD vs Indice dollaro DXY | -0.179 | -1.99% | 0.00% | **-1.99 pp** |
| S&P 500 vs Oro (spot) | 0.041 | 0.28% | 0.00% | **0.28 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.77 | 2026-10-15 | -0.05 |
| US 10Y Treasury Rate | 5.10 | 2026-10-15 | -0.09 |
| US 30Y Treasury Rate | 5.43 | 2026-10-15 | -0.09 |
| Spread 10Y-2Y USA | 0.35 | 2026-10-16 | 0.02 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **33.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 126.5500 | 42.82% | 107.21% | -21.50% |
| VIX (volatilita) | 16.4600 | 3.91% | 87.84% | -31.22% |
| Petrolio WTI | 101.9100 | 22.98% | 72.41% | -18.71% |
| Gas naturale | 3.2200 | 15.16% | 56.78% | -18.87% |
| Solana | 102.1138 | -16.37% | 31.33% | -16.37% |
| Ethereum | 2 377.5404 | -11.50% | 27.47% | -14.20% |
| US 5Y Treasury Yield | 4.9100 | 1.66% | 19.80% | -3.54% |
| US 10Y Treasury Yield | 5.1000 | 2.00% | 18.38% | -3.95% |
| Bitcoin | 81 095.8572 | -3.97% | 17.64% | -6.86% |
| US 30Y Treasury Yield | 5.4300 | 1.31% | 15.48% | -4.23% |
| Nasdaq Composite | 26 713.0300 | 2.83% | 14.71% | -7.00% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| S&P 500 | 7 659.4400 | 0.28% | 10.46% | -3.42% |
| Dow Jones | 52 002.4100 | 0.43% | 9.28% | -6.34% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
