# Moneys Monitor - Report di mercato

Generato: `2026-11-25T04:28:59+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-25T04:28:14+00:00` (577 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.26% | 0.00% | **0.26 pp** |
| 1w | -0.51% | 0.00% | **-0.51 pp** |
| 1m | -10.00% | 0.00% | **-10.00 pp** |
| 3m | -12.17% | 0.00% | **-12.17 pp** |
| 6m | -1.95% | 18.74% | **-20.69 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | S&P 500 | 4.73% | | VIX (volatilita) | -25.83% |
| 2 | Gas naturale | 3.33% | | Nasdaq Composite | -2.25% |
| 3 | Petrolio Brent | 0.87% | | GBP/USD | -0.82% |
| 4 | Dow Jones | 0.85% | | USD/JPY | -0.73% |
| 5 | Indice dollaro Fed (broad) | 0.77% | | US 30Y Treasury Yield | -0.38% |
| 6 | US 5Y Treasury Yield | 0.64% | | Ethereum | -0.24% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 16.19% | | Petrolio Brent | -26.56% |
| 2 | Ethereum | 2.55% | | Petrolio WTI | -12.15% |
| 3 | Indice dollaro Fed (broad) | 1.81% | | Nasdaq Composite | -5.86% |
| 4 | USD/JPY | 0.48% | | US 10Y Treasury Yield | -3.91% |
| 5 | Bitcoin | 0.46% | | US 5Y Treasury Yield | -3.85% |
| 6 | Solana | 0.16% | | Gas naturale | -3.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 36.86% | | Ethereum | -31.26% |
| 2 | Gas naturale | 14.73% | | Solana | -26.88% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -26.04% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -9.63% |
| 5 | FTSE MIB | 0.00% | | S&P 500 | -6.16% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -4.47% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.231 | -6.16% | 36.86% | **-43.02 pp** |
| S&P 500 vs Bitcoin | 0.070 | -6.16% | -26.04% | **19.88 pp** |
| S&P 500 vs Oro (spot) | 0.030 | -6.16% | 0.00% | **-6.16 pp** |
| S&P 500 vs Nasdaq Composite | -0.108 | -6.16% | -9.63% | **3.47 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.019 | -2.01% | 0.00% | **-2.01 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | -0.81% | 0.00% | **-0.81 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.63 | 2026-11-23 | 0.00 |
| US 10Y Treasury Rate | 4.92 | 2026-11-23 | 0.00 |
| US 30Y Treasury Rate | 5.29 | 2026-11-23 | -0.02 |
| Spread 10Y-2Y USA | 0.28 | 2026-11-24 | -0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 26.6200 | 36.86% | 328.23% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 69.1747 | -26.88% | 56.13% | -43.55% |
| Ethereum | 1 662.5979 | -31.26% | 47.88% | -41.49% |
| Bitcoin | 59 276.5599 | -26.04% | 35.61% | -31.96% |
| S&P 500 | 7 237.1700 | -6.16% | 33.03% | -11.62% |
| Nasdaq Composite | 23 879.2000 | -9.63% | 32.22% | -13.48% |
| Dow Jones | 50 018.7000 | -4.47% | 26.06% | -11.41% |
| US 5Y Treasury Yield | 4.7400 | -0.84% | 23.72% | -9.82% |
| US 10Y Treasury Yield | 4.9200 | -0.81% | 18.45% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.2900 | 0.00% | 13.70% | -7.41% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
