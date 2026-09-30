# Moneys Monitor - Report di mercato

Generato: `2026-09-30T00:40:46+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-30T00:40:11+00:00` (406 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.23% | 0.00% | **-0.23 pp** |
| 1w | -0.61% | 0.00% | **-0.61 pp** |
| 1m | 3.31% | 0.00% | **3.31 pp** |
| 3m | 13.93% | 15.71% | **-1.77 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 13.09% | | Petrolio Brent | -12.16% |
| 2 | US 5Y Treasury Yield | 1.61% | | Petrolio WTI | -9.91% |
| 3 | US 10Y Treasury Yield | 1.35% | | Gas naturale | -2.36% |
| 4 | US 30Y Treasury Yield | 1.28% | | Nasdaq Composite | -0.92% |
| 5 | Indice dollaro Fed (broad) | 0.68% | | GBP/USD | -0.91% |
| 6 | USD/JPY | 0.20% | | Ethereum | -0.79% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -9.26% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 7.41% | | Solana | -2.35% |
| 4 | US 10Y Treasury Yield | 5.65% | | USD/JPY | -1.28% |
| 5 | US 30Y Treasury Yield | 5.10% | | S&P 500 | -1.21% |
| 6 | US 5Y Treasury Yield | 4.76% | | Nasdaq Composite | -1.11% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | Dow Jones | -4.13% |
| 2 | Petrolio WTI | 23.32% | | EUR/USD | -2.08% |
| 3 | Solana | 17.14% | | GBP/USD | -1.82% |
| 4 | US 5Y Treasury Yield | 15.53% | | S&P 500 | -0.53% |
| 5 | US 10Y Treasury Yield | 12.21% | | USD/JPY | -0.40% |
| 6 | Gas naturale | 8.94% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.099 | 12.21% | 0.00% | **12.21 pp** |
| S&P 500 vs Bitcoin | 0.009 | -0.53% | 6.90% | **-7.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.021 | -2.08% | 0.00% | **-2.08 pp** |
| S&P 500 vs VIX (volatilita) | -0.041 | -0.53% | 1.45% | **-1.98 pp** |
| S&P 500 vs Nasdaq Composite | 0.107 | -0.53% | 1.05% | **-1.58 pp** |
| S&P 500 vs Oro (spot) | 0.067 | -0.53% | 0.00% | **-0.53 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.92 | 2026-09-28 | 0.11 |
| US 10Y Treasury Rate | 5.24 | 2026-09-28 | 0.07 |
| US 30Y Treasury Rate | 5.56 | 2026-09-28 | 0.07 |
| Spread 10Y-2Y USA | 0.37 | 2026-09-29 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **32.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.0700 | 1.45% | 110.92% | -31.22% |
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 118.8096 | 17.14% | 59.63% | -13.59% |
| Ethereum | 2 671.2612 | 8.59% | 39.17% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 83 488.0579 | 6.90% | 36.71% | -6.86% |
| US 5Y Treasury Yield | 5.0600 | 15.53% | 19.10% | -1.65% |
| US 10Y Treasury Yield | 5.2400 | 12.21% | 16.61% | -2.70% |
| Nasdaq Composite | 26 820.3800 | 1.05% | 14.86% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.5600 | 7.13% | 13.14% | -1.49% |
| Dow Jones | 51 349.9200 | -4.13% | 11.63% | -5.52% |
| S&P 500 | 7 670.8400 | -0.53% | 11.09% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
