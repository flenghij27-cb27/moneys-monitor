# Moneys Monitor - Report di mercato

Generato: `2026-09-12T10:15:17+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-12T10:14:39+00:00` (347 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.28% | 0.00% | **0.28 pp** |
| 1w | -0.38% | 0.00% | **-0.38 pp** |
| 1m | 3.36% | 1.25% | **2.11 pp** |
| 3m | 11.21% | 13.36% | **-2.15 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | VIX (volatilita) | 8.38% | | USD/JPY | -2.41% |
| 3 | Petrolio WTI | 6.32% | | Indice dollaro Fed (broad) | -0.57% |
| 4 | US 5Y Treasury Yield | 3.04% | | GBP/USD | -0.25% |
| 5 | US 10Y Treasury Yield | 2.48% | | EUR/USD | -0.21% |
| 6 | US 30Y Treasury Yield | 1.70% | | Solana | -0.09% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 17.37% | | Dow Jones | -2.07% |
| 2 | Petrolio Brent | 16.02% | | Bitcoin | -2.06% |
| 3 | Petrolio WTI | 11.72% | | USD/JPY | -1.78% |
| 4 | US 5Y Treasury Yield | 4.63% | | Solana | -1.55% |
| 5 | US 10Y Treasury Yield | 3.34% | | S&P 500 | -1.17% |
| 6 | Ethereum | 1.95% | | Nasdaq Composite | -0.94% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Dow Jones | -2.16% |
| 2 | Petrolio WTI | 26.39% | | S&P 500 | -1.65% |
| 3 | VIX (volatilita) | 25.19% | | Nasdaq Composite | -1.48% |
| 4 | Solana | 16.97% | | USD/JPY | -1.10% |
| 5 | Ethereum | 9.19% | | Hang Seng | -0.73% |
| 6 | Bitcoin | 6.45% | | Nikkei 225 | -0.54% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.639 | -1.65% | 25.19% | **-26.84 pp** |
| S&P 500 vs Bitcoin | 0.007 | -1.65% | 6.45% | **-8.10 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| S&P 500 vs Oro (spot) | 0.057 | -1.65% | 2.46% | **-4.11 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | 5.41% | 2.46% | **2.95 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 2.46% | 0.04% | **2.42 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -1.65% | -1.48% | **-0.17 pp** |
| EUR/USD vs Indice dollaro DXY | 0.012 | 0.16% | 0.08% | **0.08 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.56 | 2026-09-10 | 0.13 |
| US 10Y Treasury Rate | 4.95 | 2026-09-10 | 0.12 |
| US 30Y Treasury Rate | 5.37 | 2026-09-10 | 0.09 |
| Spread 10Y-2Y USA | 0.33 | 2026-09-11 | -0.06 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **39.0 bp**, 30Y-10Y **42.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.8400 | 25.19% | 84.34% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 102.1121 | 16.97% | 41.54% | -13.59% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 533.7897 | 9.19% | 28.24% | -5.78% |
| Bitcoin | 77 379.4732 | 6.45% | 26.81% | -5.72% |
| US 5Y Treasury Yield | 4.7500 | n/d | 17.44% | -0.66% |
| US 10Y Treasury Yield | 4.9500 | 5.41% | 13.43% | -2.70% |
| Nasdaq Composite | 26 333.0400 | -1.48% | 12.52% | -7.00% |
| Dow Jones | 52 573.2900 | -2.16% | 11.11% | -4.20% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| US 30Y Treasury Yield | 5.3700 | n/d | 9.14% | -0.57% |
| S&P 500 | 7 656.9800 | -1.65% | 9.03% | -3.42% |
| Hang Seng | 25 511.1000 | -0.73% | 6.71% | -3.43% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
