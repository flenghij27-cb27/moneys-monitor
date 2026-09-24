# Moneys Monitor - Report di mercato

Generato: `2026-09-24T16:40:18+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-24T16:39:46+00:00` (389 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.07% | 0.00% | **0.07 pp** |
| 1w | 1.76% | 0.00% | **1.76 pp** |
| 1m | 2.81% | 0.00% | **2.81 pp** |
| 3m | 13.08% | 15.23% | **-2.15 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 2.08% | | Petrolio Brent | -12.16% |
| 2 | USD/JPY | 2.06% | | Petrolio WTI | -9.91% |
| 3 | Indice dollaro Fed (broad) | 1.10% | | VIX (volatilita) | -4.44% |
| 4 | Ethereum | 0.26% | | Gas naturale | -2.36% |
| 5 | Bitcoin | 0.23% | | Nasdaq Composite | -1.13% |
| 6 | FTSE MIB | 0.00% | | GBP/USD | -1.12% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -17.38% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -1.91% |
| 3 | Gas naturale | 7.41% | | USD/JPY | -1.43% |
| 4 | Solana | 5.71% | | US 30Y Treasury Yield | -1.31% |
| 5 | Bitcoin | 4.09% | | EUR/USD | -0.99% |
| 6 | Nasdaq Composite | 3.69% | | US 10Y Treasury Yield | -0.80% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | VIX (volatilita) | -6.08% |
| 2 | Petrolio WTI | 23.32% | | Dow Jones | -3.31% |
| 3 | Solana | 12.87% | | EUR/USD | -2.66% |
| 4 | Gas naturale | 8.94% | | GBP/USD | -0.89% |
| 5 | Ethereum | 7.72% | | USD/JPY | -0.55% |
| 6 | US 10Y Treasury Yield | 4.69% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| S&P 500 vs VIX (volatilita) | -0.534 | 0.41% | -6.08% | **6.49 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.042 | 4.69% | 0.00% | **4.69 pp** |
| S&P 500 vs Bitcoin | -0.019 | 0.41% | 4.18% | **-3.77 pp** |
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
| US 2Y Treasury Rate | 4.71 | 2026-09-22 | -0.05 |
| US 10Y Treasury Rate | 4.96 | 2026-09-22 | 0.00 |
| US 30Y Treasury Rate | 5.29 | 2026-09-22 | 0.00 |
| Spread 10Y-2Y USA | 0.26 | 2026-09-23 | 0.01 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **25.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| VIX (volatilita) | 14.2100 | -6.08% | 100.28% | -31.22% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 117.2654 | 12.87% | 60.11% | -13.59% |
| Ethereum | 2 689.9368 | 7.72% | 39.85% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 84 592.8752 | 4.18% | 37.82% | -6.86% |
| US 5Y Treasury Yield | 4.8300 | n/d | 17.00% | -1.65% |
| Nasdaq Composite | 26 936.0400 | 2.89% | 15.49% | -7.00% |
| US 10Y Treasury Yield | 4.9600 | 4.69% | 14.14% | -2.70% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| S&P 500 | 7 706.0300 | 0.41% | 11.05% | -3.42% |
| Dow Jones | 51 511.5900 | -3.31% | 11.05% | -5.31% |
| US 30Y Treasury Yield | 5.2900 | n/d | 10.49% | -1.49% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
