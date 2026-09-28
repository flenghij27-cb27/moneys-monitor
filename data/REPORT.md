# Moneys Monitor - Report di mercato

Generato: `2026-09-28T21:38:15+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-28T21:37:43+00:00` (402 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.36% | 0.00% | **-0.36 pp** |
| 1w | 0.50% | 0.00% | **0.50 pp** |
| 1m | 3.20% | 0.00% | **3.20 pp** |
| 3m | 15.45% | 15.61% | **-0.15 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Dow Jones | 0.93% | | Petrolio Brent | -12.16% |
| 2 | Indice dollaro Fed (broad) | 0.68% | | Petrolio WTI | -9.91% |
| 3 | S&P 500 | 0.51% | | VIX (volatilita) | -4.44% |
| 4 | Nasdaq Composite | 0.48% | | Solana | -3.13% |
| 5 | US 30Y Treasury Yield | 0.37% | | Gas naturale | -2.36% |
| 6 | USD/JPY | 0.20% | | Bitcoin | -1.20% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -17.38% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 7.41% | | USD/JPY | -1.28% |
| 4 | US 10Y Treasury Yield | 3.19% | | Bitcoin | -1.15% |
| 5 | Solana | 2.96% | | EUR/USD | -0.97% |
| 6 | US 30Y Treasury Yield | 2.81% | | Ethereum | -0.08% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | VIX (volatilita) | -6.08% |
| 2 | Petrolio WTI | 23.32% | | Dow Jones | -3.04% |
| 3 | Solana | 14.04% | | EUR/USD | -2.28% |
| 4 | US 5Y Treasury Yield | 13.96% | | GBP/USD | -1.82% |
| 5 | US 10Y Treasury Yield | 10.94% | | USD/JPY | -0.40% |
| 6 | Gas naturale | 8.94% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.028 | 10.94% | 0.00% | **10.94 pp** |
| S&P 500 vs VIX (volatilita) | 0.205 | 0.94% | -6.08% | **7.02 pp** |
| S&P 500 vs Bitcoin | 0.007 | 0.94% | 5.60% | **-4.66 pp** |
| S&P 500 vs Nasdaq Composite | 0.951 | 0.94% | 3.59% | **-2.65 pp** |
| EUR/USD vs Indice dollaro DXY | 0.019 | -2.28% | 0.00% | **-2.28 pp** |
| S&P 500 vs Oro (spot) | 0.065 | 0.94% | 0.00% | **0.94 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.81 | 2026-09-25 | -0.06 |
| US 10Y Treasury Rate | 5.17 | 2026-09-25 | -0.01 |
| US 30Y Treasury Rate | 5.49 | 2026-09-25 | 0.02 |
| Spread 10Y-2Y USA | 0.32 | 2026-09-28 | -0.04 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **36.0 bp**, 30Y-10Y **32.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| VIX (volatilita) | 14.2100 | -6.08% | 100.28% | -31.22% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 118.2834 | 14.04% | 61.53% | -13.59% |
| Ethereum | 2 680.6972 | 7.86% | 39.53% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 83 429.9356 | 5.60% | 37.67% | -6.86% |
| US 5Y Treasury Yield | 4.9800 | 13.96% | 19.71% | -1.65% |
| US 10Y Treasury Yield | 5.1700 | 10.94% | 16.57% | -2.70% |
| Nasdaq Composite | 27 068.7200 | 3.59% | 14.57% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.4900 | 5.98% | 12.70% | -1.49% |
| Dow Jones | 51 828.6200 | -3.04% | 11.65% | -5.52% |
| S&P 500 | 7 743.4100 | 0.94% | 10.82% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
