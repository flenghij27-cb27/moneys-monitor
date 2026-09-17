# Moneys Monitor - Report di mercato

Generato: `2026-09-17T11:10:16+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-17T11:09:42+00:00` (364 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.18% | 0.00% | **0.18 pp** |
| 1w | -0.87% | 0.00% | **-0.87 pp** |
| 1m | -0.72% | 0.00% | **-0.72 pp** |
| 3m | 8.68% | 15.71% | **-7.03 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | USD/JPY | -1.54% |
| 2 | Petrolio WTI | 10.03% | | Dow Jones | -1.21% |
| 3 | Gas naturale | 5.69% | | S&P 500 | -0.45% |
| 4 | Solana | 1.31% | | EUR/USD | -0.02% |
| 5 | Ethereum | 0.69% | | Nasdaq Composite | -0.01% |
| 6 | US 5Y Treasury Yield | 0.63% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | Ethereum | -3.58% |
| 2 | Petrolio WTI | 25.85% | | USD/JPY | -3.32% |
| 3 | VIX (volatilita) | 9.41% | | Dow Jones | -1.75% |
| 4 | US 5Y Treasury Yield | 5.69% | | Solana | -1.75% |
| 5 | Gas naturale | 5.51% | | Bitcoin | -1.23% |
| 6 | US 10Y Treasury Yield | 4.17% | | S&P 500 | -1.11% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | Bitcoin | -3.91% |
| 2 | Petrolio WTI | 36.89% | | Dow Jones | -3.53% |
| 3 | Gas naturale | 11.57% | | USD/JPY | -2.56% |
| 4 | VIX (volatilita) | 8.65% | | Ethereum | -1.83% |
| 5 | US 10Y Treasury Yield | 6.25% | | S&P 500 | -1.82% |
| 6 | Solana | 1.59% | | EUR/USD | -1.22% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| S&P 500 vs VIX (volatilita) | -0.595 | -1.82% | 8.65% | **-10.47 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.113 | 6.25% | 0.00% | **6.25 pp** |
| S&P 500 vs Bitcoin | -0.026 | -1.82% | -3.91% | **2.09 pp** |
| S&P 500 vs Oro (spot) | -0.173 | -1.82% | 0.00% | **-1.82 pp** |
| EUR/USD vs Indice dollaro DXY | -0.016 | -1.22% | 0.00% | **-1.22 pp** |
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
| US 2Y Treasury Rate | 4.67 | 2026-09-15 | 0.02 |
| US 10Y Treasury Rate | 5.00 | 2026-09-15 | 0.03 |
| US 30Y Treasury Rate | 5.36 | 2026-09-15 | 0.02 |
| Spread 10Y-2Y USA | 0.27 | 2026-09-16 | -0.06 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **33.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.2000 | 8.65% | 92.36% | -31.03% |
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Solana | 99.8994 | 1.59% | 41.35% | -13.59% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| Ethereum | 2 433.1456 | -1.83% | 33.53% | -5.78% |
| Bitcoin | 76 302.4487 | -3.91% | 28.36% | -6.86% |
| US 5Y Treasury Yield | 4.8300 | n/d | 15.25% | -0.66% |
| US 10Y Treasury Yield | 5.0000 | 6.25% | 12.12% | -2.70% |
| Nasdaq Composite | 25 978.4200 | -1.18% | 12.00% | -7.00% |
| Dow Jones | 51 461.9000 | -3.53% | 11.75% | -5.31% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| S&P 500 | 7 551.8100 | -1.82% | 8.86% | -3.42% |
| US 30Y Treasury Yield | 5.3600 | n/d | 8.81% | -0.57% |
| GBP/USD | 1.3524 | 0.25% | 3.59% | -1.82% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
