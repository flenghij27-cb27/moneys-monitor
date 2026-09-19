# Moneys Monitor - Report di mercato

Generato: `2026-09-19T18:28:01+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-19T18:27:28+00:00` (373 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.11% | 0.00% | **0.11 pp** |
| 1w | 1.87% | 0.00% | **1.87 pp** |
| 1m | 1.76% | 0.00% | **1.76 pp** |
| 3m | 12.99% | 20.19% | **-7.19 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | VIX (volatilita) | -12.82% |
| 2 | Petrolio WTI | 10.03% | | Solana | -1.88% |
| 3 | Gas naturale | 5.69% | | US 5Y Treasury Yield | -1.65% |
| 4 | S&P 500 | 1.14% | | USD/JPY | -1.54% |
| 5 | Ethereum | 0.98% | | US 10Y Treasury Yield | -1.40% |
| 6 | Bitcoin | 0.51% | | US 30Y Treasury Yield | -1.12% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | VIX (volatilita) | -13.45% |
| 2 | Petrolio WTI | 25.85% | | USD/JPY | -3.32% |
| 3 | Solana | 8.27% | | Dow Jones | -1.69% |
| 4 | Gas naturale | 5.51% | | US 30Y Treasury Yield | -1.49% |
| 5 | Ethereum | 4.92% | | EUR/USD | -1.14% |
| 6 | Bitcoin | 4.16% | | GBP/USD | -0.76% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | VIX (volatilita) | -3.50% |
| 2 | Petrolio WTI | 36.89% | | USD/JPY | -2.56% |
| 3 | Gas naturale | 11.57% | | Dow Jones | -2.04% |
| 4 | Ethereum | 7.57% | | EUR/USD | -1.90% |
| 5 | US 10Y Treasury Yield | 5.20% | | S&P 500 | -0.91% |
| 6 | Solana | 5.14% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.114 | 5.20% | 0.00% | **5.20 pp** |
| S&P 500 vs Bitcoin | -0.077 | -0.91% | 4.09% | **-5.00 pp** |
| S&P 500 vs Nasdaq Composite | -0.013 | -0.91% | 1.75% | **-2.66 pp** |
| S&P 500 vs VIX (volatilita) | -0.189 | -0.91% | -3.50% | **2.59 pp** |
| EUR/USD vs Indice dollaro DXY | -0.020 | -1.90% | 0.00% | **-1.90 pp** |
| S&P 500 vs Oro (spot) | 0.111 | -0.91% | 0.00% | **-0.91 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.67 | 2026-09-17 | -0.07 |
| US 10Y Treasury Rate | 4.94 | 2026-09-17 | -0.07 |
| US 30Y Treasury Rate | 5.29 | 2026-09-17 | -0.06 |
| Spread 10Y-2Y USA | 0.25 | 2026-09-18 | -0.02 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **27.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.4400 | -3.50% | 99.37% | -31.03% |
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Solana | 111.0134 | 5.14% | 57.76% | -13.59% |
| Ethereum | 2 639.9310 | 7.57% | 40.98% | -5.78% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| Bitcoin | 81 424.8701 | 4.09% | 35.59% | -6.86% |
| US 5Y Treasury Yield | 4.7800 | n/d | 17.25% | -1.65% |
| US 10Y Treasury Yield | 4.9400 | 5.20% | 13.20% | -2.70% |
| Nasdaq Composite | 26 522.5500 | 1.75% | 12.97% | -7.00% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| Dow Jones | 51 682.6400 | -2.04% | 10.54% | -5.31% |
| US 30Y Treasury Yield | 5.2900 | n/d | 10.04% | -1.49% |
| S&P 500 | 7 637.7600 | -0.91% | 9.41% | -3.42% |
| GBP/USD | 1.3524 | 0.25% | 3.59% | -1.82% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
