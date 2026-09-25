# Moneys Monitor - Report di mercato

Generato: `2026-09-25T11:21:50+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-25T11:21:17+00:00` (391 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.63% | 0.00% | **0.63 pp** |
| 1w | 2.09% | 0.00% | **2.09 pp** |
| 1m | 4.19% | 0.00% | **4.19 pp** |
| 3m | 14.22% | 13.65% | **0.57 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 3.70% | | Petrolio Brent | -12.16% |
| 2 | US 5Y Treasury Yield | 3.31% | | Petrolio WTI | -9.91% |
| 3 | US 10Y Treasury Yield | 3.02% | | VIX (volatilita) | -4.44% |
| 4 | US 30Y Treasury Yield | 2.08% | | Gas naturale | -2.36% |
| 5 | USD/JPY | 2.06% | | GBP/USD | -1.12% |
| 6 | Ethereum | 1.74% | | EUR/USD | -0.39% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -17.38% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -1.91% |
| 3 | Solana | 9.58% | | USD/JPY | -1.43% |
| 4 | Gas naturale | 7.41% | | EUR/USD | -0.99% |
| 5 | Bitcoin | 4.81% | | Dow Jones | -0.83% |
| 6 | Ethereum | 3.64% | | FTSE MIB | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | VIX (volatilita) | -6.08% |
| 2 | Petrolio WTI | 23.32% | | Dow Jones | -3.87% |
| 3 | Solana | 19.18% | | EUR/USD | -2.66% |
| 4 | Ethereum | 11.52% | | GBP/USD | -0.89% |
| 5 | Gas naturale | 8.94% | | USD/JPY | -0.55% |
| 6 | US 10Y Treasury Yield | 8.63% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.032 | 8.63% | 0.00% | **8.63 pp** |
| S&P 500 vs VIX (volatilita) | 0.053 | 0.67% | -6.08% | **6.75 pp** |
| S&P 500 vs Bitcoin | -0.018 | 0.67% | 6.83% | **-6.16 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | 0.67% | 3.69% | **-3.02 pp** |
| EUR/USD vs Indice dollaro DXY | 0.103 | -2.66% | 0.00% | **-2.66 pp** |
| S&P 500 vs Oro (spot) | -0.087 | 0.67% | 0.00% | **0.67 pp** |
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
| Solana | 121.3401 | 19.18% | 60.91% | -13.59% |
| Ethereum | 2 734.0014 | 11.52% | 40.05% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 85 103.6166 | 6.83% | 37.88% | -6.86% |
| US 5Y Treasury Yield | 4.9900 | n/d | 19.32% | -1.65% |
| US 10Y Treasury Yield | 5.1100 | 8.63% | 16.12% | -2.70% |
| Nasdaq Composite | 26 939.3700 | 3.69% | 15.43% | -7.00% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| US 30Y Treasury Yield | 5.4000 | n/d | 12.44% | -1.49% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| S&P 500 | 7 704.1300 | 0.67% | 11.02% | -3.42% |
| Dow Jones | 51 349.9800 | -3.87% | 11.02% | -5.52% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
