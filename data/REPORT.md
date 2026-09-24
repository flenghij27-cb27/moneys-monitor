# Moneys Monitor - Report di mercato

Generato: `2026-09-24T23:58:20+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-24T23:57:45+00:00` (390 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.01% | 0.00% | **0.01 pp** |
| 1w | 1.69% | 0.00% | **1.69 pp** |
| 1m | 2.74% | 0.00% | **2.74 pp** |
| 3m | 13.00% | 15.23% | **-2.23 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | US 5Y Treasury Yield | 3.31% | | Petrolio Brent | -12.16% |
| 2 | US 10Y Treasury Yield | 3.02% | | Petrolio WTI | -9.91% |
| 3 | US 30Y Treasury Yield | 2.08% | | VIX (volatilita) | -4.44% |
| 4 | USD/JPY | 2.06% | | Gas naturale | -2.36% |
| 5 | Solana | 1.86% | | Nasdaq Composite | -1.13% |
| 6 | Indice dollaro Fed (broad) | 1.10% | | GBP/USD | -1.12% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -17.38% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -1.91% |
| 3 | Gas naturale | 7.41% | | USD/JPY | -1.43% |
| 4 | Solana | 5.48% | | EUR/USD | -0.99% |
| 5 | Bitcoin | 3.81% | | Dow Jones | -0.83% |
| 6 | Nasdaq Composite | 3.69% | | FTSE MIB | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | VIX (volatilita) | -6.08% |
| 2 | Petrolio WTI | 23.32% | | Dow Jones | -3.87% |
| 3 | Solana | 12.62% | | EUR/USD | -2.66% |
| 4 | Gas naturale | 8.94% | | GBP/USD | -0.89% |
| 5 | US 10Y Treasury Yield | 8.63% | | USD/JPY | -0.55% |
| 6 | Ethereum | 7.61% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.135 | 8.63% | 0.00% | **8.63 pp** |
| S&P 500 vs VIX (volatilita) | -0.534 | 0.41% | -6.08% | **6.49 pp** |
| S&P 500 vs Bitcoin | -0.017 | 0.41% | 3.89% | **-3.48 pp** |
| EUR/USD vs Indice dollaro DXY | 0.040 | -2.66% | 0.00% | **-2.66 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | 0.41% | 2.89% | **-2.48 pp** |
| S&P 500 vs Oro (spot) | -0.088 | 0.41% | 0.00% | **0.41 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.85 | 2026-09-23 | 0.14 |
| US 10Y Treasury Rate | 5.11 | 2026-09-23 | 0.15 |
| US 30Y Treasury Rate | 5.40 | 2026-09-23 | 0.11 |
| Spread 10Y-2Y USA | 0.31 | 2026-09-24 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **26.0 bp**, 30Y-10Y **29.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| VIX (volatilita) | 14.2100 | -6.08% | 100.28% | -31.22% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 117.0115 | 12.62% | 60.05% | -13.59% |
| Ethereum | 2 687.1645 | 7.61% | 39.86% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 84 364.1211 | 3.89% | 37.84% | -6.86% |
| US 5Y Treasury Yield | 4.9900 | n/d | 19.32% | -1.65% |
| US 10Y Treasury Yield | 5.1100 | 8.63% | 16.12% | -2.70% |
| Nasdaq Composite | 26 936.0400 | 2.89% | 15.49% | -7.00% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| US 30Y Treasury Yield | 5.4000 | n/d | 12.44% | -1.49% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| S&P 500 | 7 706.0300 | 0.41% | 11.05% | -3.42% |
| Dow Jones | 51 349.9800 | -3.87% | 11.02% | -5.52% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
