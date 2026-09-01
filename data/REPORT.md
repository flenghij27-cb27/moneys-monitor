# Moneys Monitor - Report di mercato

Generato: `2026-09-01T23:28:27+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-01T23:27:53+00:00` (311 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.81% | 0.00% | **-0.81 pp** |
| 1w | -0.29% | 0.00% | **-0.29 pp** |
| 1m | 7.06% | 7.11% | **-0.05 pp** |
| 3m | 17.01% | 14.50% | **2.50 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.44% | | Solana | -3.39% |
| 2 | VIX (volatilita) | 3.40% | | Ethereum | -2.33% |
| 3 | Indice dollaro Fed (broad) | 0.58% | | Bitcoin | -1.92% |
| 4 | US 30Y Treasury Yield | 0.57% | | Petrolio WTI | -1.87% |
| 5 | USD/JPY | 0.47% | | Dow Jones | -0.79% |
| 6 | US 10Y Treasury Yield | 0.42% | | GBP/USD | -0.62% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 1.48% | | Petrolio Brent | -6.60% |
| 2 | US 10Y Treasury Yield | 0.98% | | VIX (volatilita) | -5.81% |
| 3 | Nasdaq Composite | 0.73% | | Petrolio WTI | -5.02% |
| 4 | USD/JPY | 0.67% | | Bitcoin | -2.66% |
| 5 | S&P 500 | 0.15% | | Ethereum | -2.62% |
| 6 | Gas naturale | 0.14% | | Dow Jones | -1.22% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 29.39% | | CAC 40 Francia | -3.01% |
| 2 | Ethereum | 25.80% | | Dow Jones | -2.35% |
| 3 | Bitcoin | 18.78% | | FTSE MIB | -1.83% |
| 4 | Petrolio Brent | 10.64% | | Shanghai Composite | -1.28% |
| 5 | Petrolio WTI | 9.76% | | Nasdaq Composite | -1.20% |
| 6 | Argento (spot) | 7.55% | | Euro Stoxx 50 | -0.96% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.018 | -0.92% | 18.78% | **-19.70 pp** |
| S&P 500 vs Oro (spot) | 0.091 | -0.92% | 6.67% | **-7.59 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.030 | 1.93% | 6.67% | **-4.74 pp** |
| S&P 500 vs VIX (volatilita) | 0.043 | -0.92% | 0.13% | **-1.05 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 6.67% | 7.55% | **-0.88 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| EUR/USD vs Indice dollaro DXY | -0.118 | 0.24% | -0.64% | **0.88 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | -0.92% | -1.20% | **0.28 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.34 | 2026-08-31 | 0.00 |
| US 10Y Treasury Rate | 4.75 | 2026-08-31 | 0.02 |
| US 30Y Treasury Rate | 5.25 | 2026-08-31 | 0.03 |
| Spread 10Y-2Y USA | 0.40 | 2026-09-01 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **41.0 bp**, 30Y-10Y **50.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.9200 | 0.13% | 62.35% | -31.03% |
| Ethereum | 2 413.6399 | 25.80% | 53.20% | -5.78% |
| Solana | 99.7972 | 29.39% | 45.61% | -13.59% |
| Bitcoin | 77 291.5735 | 18.78% | 39.74% | -5.72% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Argento (spot) | 68.2900 | 7.55% | 25.93% | -11.21% |
| Oro (spot) | 4 693.0000 | 6.67% | 17.99% | -4.96% |
| Nikkei 225 | 65 856.4300 | 0.38% | 17.09% | -12.83% |
| Bovespa Brasile | 172 458.6200 | -0.03% | 12.37% | -6.51% |
| Hang Seng | 25 511.1000 | -0.61% | 11.80% | -3.43% |
| US 10Y Treasury Yield | 4.7500 | 1.93% | 11.60% | -2.70% |
| Shanghai Composite | 3 889.4450 | -1.28% | 10.98% | -8.47% |
| Rame | 6.6680 | 1.17% | 10.72% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
