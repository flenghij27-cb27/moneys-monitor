# Moneys Monitor - Report di mercato

Generato: `2026-09-23T10:57:40+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-23T10:57:03+00:00` (385 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.13% | 0.00% | **-0.13 pp** |
| 1w | 2.14% | 0.00% | **2.14 pp** |
| 1m | 4.86% | 0.00% | **4.86 pp** |
| 3m | 14.92% | 18.74% | **-3.82 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | GBP/USD | -1.12% |
| 2 | Petrolio WTI | 10.03% | | US 10Y Treasury Yield | -1.00% |
| 3 | Gas naturale | 5.69% | | US 30Y Treasury Yield | -0.94% |
| 4 | USD/JPY | 2.06% | | Solana | -0.79% |
| 5 | Indice dollaro Fed (broad) | 1.10% | | Ethereum | -0.65% |
| 6 | Nasdaq Composite | 0.45% | | US 5Y Treasury Yield | -0.62% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | VIX (volatilita) | -13.04% |
| 2 | Petrolio WTI | 25.85% | | GBP/USD | -1.91% |
| 3 | Bitcoin | 5.95% | | USD/JPY | -1.43% |
| 4 | Gas naturale | 5.51% | | US 30Y Treasury Yield | -0.94% |
| 5 | Nasdaq Composite | 4.86% | | EUR/USD | -0.66% |
| 6 | Ethereum | 4.52% | | Dow Jones | -0.44% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | Dow Jones | -2.65% |
| 2 | Petrolio WTI | 36.89% | | EUR/USD | -1.84% |
| 3 | Solana | 17.49% | | VIX (volatilita) | -1.72% |
| 4 | Ethereum | 14.60% | | GBP/USD | -0.89% |
| 5 | Gas naturale | 11.57% | | USD/JPY | -0.55% |
| 6 | Bitcoin | 11.24% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| S&P 500 vs Bitcoin | -0.022 | 1.18% | 11.24% | **-10.06 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.042 | 4.69% | 0.00% | **4.69 pp** |
| S&P 500 vs VIX (volatilita) | -0.555 | 1.18% | -1.72% | **2.90 pp** |
| S&P 500 vs Nasdaq Composite | 0.951 | 1.18% | 4.06% | **-2.88 pp** |
| EUR/USD vs Indice dollaro DXY | 0.113 | -1.84% | 0.00% | **-1.84 pp** |
| S&P 500 vs Oro (spot) | -0.091 | 1.18% | 0.00% | **1.18 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.76 | 2026-09-21 | 0.00 |
| US 10Y Treasury Rate | 4.96 | 2026-09-21 | -0.05 |
| US 30Y Treasury Rate | 5.29 | 2026-09-21 | -0.05 |
| Spread 10Y-2Y USA | 0.25 | 2026-09-22 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **20.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.8700 | -1.72% | 100.58% | -31.03% |
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Solana | 117.3697 | 17.49% | 59.53% | -13.59% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| Ethereum | 2 732.5460 | 14.60% | 39.51% | -5.78% |
| Bitcoin | 85 835.3763 | 11.24% | 37.80% | -6.86% |
| US 5Y Treasury Yield | 4.8300 | n/d | 17.37% | -1.65% |
| Nasdaq Composite | 27 244.2800 | 4.06% | 15.13% | -7.00% |
| US 10Y Treasury Yield | 4.9600 | 4.69% | 14.55% | -2.70% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| Dow Jones | 51 863.6900 | -2.65% | 10.99% | -5.31% |
| US 30Y Treasury Yield | 5.2900 | n/d | 10.80% | -1.49% |
| S&P 500 | 7 764.6400 | 1.18% | 10.72% | -3.42% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
