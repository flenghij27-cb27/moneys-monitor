# Moneys Monitor - Report di mercato

Generato: `2026-09-17T23:37:45+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-17T23:37:11+00:00` (366 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.39% | 0.00% | **0.39 pp** |
| 1w | -0.67% | 0.00% | **-0.67 pp** |
| 1m | -0.51% | 0.00% | **-0.51 pp** |
| 3m | 8.95% | 15.71% | **-6.76 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | USD/JPY | -1.54% |
| 2 | Petrolio WTI | 10.03% | | EUR/USD | -0.49% |
| 3 | Gas naturale | 5.69% | | S&P 500 | -0.45% |
| 4 | VIX (volatilita) | 2.97% | | US 30Y Treasury Yield | -0.19% |
| 5 | Solana | 2.83% | | Nasdaq Composite | -0.01% |
| 6 | Ethereum | 1.20% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | USD/JPY | -3.32% |
| 2 | Petrolio WTI | 25.85% | | Ethereum | -3.09% |
| 3 | VIX (volatilita) | 7.59% | | EUR/USD | -1.16% |
| 4 | Gas naturale | 5.51% | | Bitcoin | -1.16% |
| 5 | US 5Y Treasury Yield | 5.42% | | S&P 500 | -1.11% |
| 6 | US 10Y Treasury Yield | 3.73% | | Nasdaq Composite | -1.05% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | Bitcoin | -3.84% |
| 2 | Petrolio WTI | 36.89% | | Dow Jones | -3.15% |
| 3 | VIX (volatilita) | 19.10% | | USD/JPY | -2.56% |
| 4 | Gas naturale | 11.57% | | S&P 500 | -1.82% |
| 5 | US 10Y Treasury Yield | 7.67% | | EUR/USD | -1.70% |
| 6 | Solana | 3.11% | | Ethereum | -1.33% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.143 | -1.82% | 19.10% | **-20.92 pp** |
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.136 | 7.67% | 0.00% | **7.67 pp** |
| S&P 500 vs Bitcoin | -0.027 | -1.82% | -3.84% | **2.02 pp** |
| S&P 500 vs Oro (spot) | -0.173 | -1.82% | 0.00% | **-1.82 pp** |
| EUR/USD vs Indice dollaro DXY | 0.046 | -1.70% | 0.00% | **-1.70 pp** |
| S&P 500 vs Nasdaq Composite | 0.947 | -1.82% | -1.18% | **-0.64 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.74 | 2026-09-16 | 0.07 |
| US 10Y Treasury Rate | 5.01 | 2026-09-16 | 0.01 |
| US 30Y Treasury Rate | 5.35 | 2026-09-16 | -0.01 |
| Spread 10Y-2Y USA | 0.27 | 2026-09-17 | 0.00 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **27.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| VIX (volatilita) | 17.7100 | 19.10% | 89.31% | -31.03% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Solana | 101.3991 | 3.11% | 42.41% | -13.59% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| Ethereum | 2 445.4622 | -1.33% | 33.72% | -5.78% |
| Bitcoin | 76 358.2411 | -3.84% | 28.37% | -6.86% |
| US 5Y Treasury Yield | 4.8600 | n/d | 14.67% | -0.66% |
| Nasdaq Composite | 25 978.4200 | -1.18% | 12.00% | -7.00% |
| US 10Y Treasury Yield | 5.0100 | 7.67% | 11.94% | -2.70% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| Dow Jones | 51 778.0400 | -3.15% | 11.28% | -5.31% |
| S&P 500 | 7 551.8100 | -1.82% | 8.86% | -3.42% |
| US 30Y Treasury Yield | 5.3500 | n/d | 8.68% | -0.57% |
| GBP/USD | 1.3524 | 0.25% | 3.59% | -1.82% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
