# Moneys Monitor - Report di mercato

Generato: `2026-11-10T21:41:03+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-10T21:40:31+00:00` (536 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.37% | 0.00% | **-0.37 pp** |
| 1w | -1.80% | 0.00% | **-1.80 pp** |
| 1m | -5.86% | 0.00% | **-5.86 pp** |
| 3m | -4.99% | 0.00% | **-4.99 pp** |
| 6m | 5.03% | 10.40% | **-5.37 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Nasdaq Composite | 2.74% | | VIX (volatilita) | -22.31% |
| 2 | S&P 500 | 2.67% | | Petrolio Brent | -13.05% |
| 3 | Dow Jones | 2.15% | | Gas naturale | -4.71% |
| 4 | US 5Y Treasury Yield | 0.65% | | Solana | -3.73% |
| 5 | USD/JPY | 0.48% | | Petrolio WTI | -3.61% |
| 6 | US 10Y Treasury Yield | 0.41% | | Ethereum | -3.51% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 3.62% | | Gas naturale | -17.30% |
| 2 | GBP/USD | 1.04% | | Ethereum | -7.87% |
| 3 | Dow Jones | 0.78% | | Solana | -7.41% |
| 4 | Indice dollaro Fed (broad) | 0.41% | | Petrolio Brent | -6.08% |
| 5 | Nasdaq Composite | 0.35% | | VIX (volatilita) | -5.82% |
| 6 | EUR/USD | 0.31% | | Bitcoin | -2.68% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 34.23% | | Solana | -21.02% |
| 2 | Petrolio WTI | 20.92% | | Ethereum | -15.50% |
| 3 | Petrolio Brent | 20.91% | | Bitcoin | -10.35% |
| 4 | Dow Jones | 1.42% | | Nasdaq Composite | -8.30% |
| 5 | EUR/USD | 0.30% | | US 10Y Treasury Yield | -6.51% |
| 6 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -6.41% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.039 | -3.44% | 34.23% | **-37.67 pp** |
| S&P 500 vs Bitcoin | 0.011 | -3.44% | -10.35% | **6.91 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.048 | -6.51% | 0.00% | **-6.51 pp** |
| S&P 500 vs Nasdaq Composite | 0.016 | -3.44% | -8.30% | **4.86 pp** |
| S&P 500 vs Oro (spot) | 0.038 | -3.44% | 0.00% | **-3.44 pp** |
| EUR/USD vs Indice dollaro DXY | -0.131 | 0.30% | 0.00% | **0.30 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.56 | 2026-11-09 | 0.05 |
| US 10Y Treasury Rate | 4.88 | 2026-11-09 | 0.02 |
| US 30Y Treasury Rate | 5.26 | 2026-11-09 | 0.00 |
| Spread 10Y-2Y USA | 0.32 | 2026-11-09 | -0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.9200 | 34.23% | 302.41% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 056.8166 | -15.50% | 45.51% | -25.77% |
| Solana | 83.3245 | -21.02% | 33.62% | -31.76% |
| Nasdaq Composite | 25 253.1400 | -8.30% | 30.88% | -11.90% |
| Bitcoin | 73 839.8024 | -10.35% | 29.98% | -14.85% |
| S&P 500 | 7 549.9400 | -3.44% | 23.19% | -5.95% |
| Dow Jones | 52 389.7500 | 1.42% | 20.57% | -6.34% |
| US 5Y Treasury Yield | 4.6700 | -6.41% | 19.14% | -9.82% |
| US 10Y Treasury Yield | 4.8800 | -6.51% | 17.24% | -8.85% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| US 30Y Treasury Yield | 5.2600 | -6.07% | 14.01% | -7.41% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
