# Moneys Monitor - Report di mercato

Generato: `2026-09-11T10:46:20+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-11T10:45:45+00:00` (344 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.05% | 0.00% | **0.05 pp** |
| 1w | -1.34% | 0.00% | **-1.34 pp** |
| 1m | 4.82% | 2.72% | **2.10 pp** |
| 3m | 11.39% | 15.60% | **-4.20 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | Gas naturale | -3.10% |
| 2 | Petrolio WTI | 6.32% | | USD/JPY | -2.41% |
| 3 | VIX (volatilita) | 4.71% | | Nasdaq Composite | -0.65% |
| 4 | Ethereum | 0.97% | | Dow Jones | -0.60% |
| 5 | US 5Y Treasury Yield | 0.88% | | S&P 500 | -0.58% |
| 6 | US 10Y Treasury Yield | 0.63% | | Indice dollaro Fed (broad) | -0.57% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | Solana | -6.29% |
| 2 | Petrolio WTI | 11.72% | | Bitcoin | -3.82% |
| 3 | US 5Y Treasury Yield | 1.32% | | Dow Jones | -1.88% |
| 4 | US 10Y Treasury Yield | 0.84% | | Ethereum | -1.81% |
| 5 | VIX (volatilita) | 0.73% | | USD/JPY | -1.78% |
| 6 | US 30Y Treasury Yield | 0.19% | | S&P 500 | -0.98% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | Dow Jones | -3.10% |
| 2 | Petrolio WTI | 26.39% | | S&P 500 | -2.49% |
| 3 | Solana | 20.59% | | Nasdaq Composite | -2.42% |
| 4 | Ethereum | 16.65% | | USD/JPY | -1.10% |
| 5 | VIX (volatilita) | 15.35% | | Russell 2000 | -0.85% |
| 6 | Bitcoin | 12.24% | | CAC 40 Francia | -0.58% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.689 | -2.49% | 15.35% | **-17.84 pp** |
| S&P 500 vs Bitcoin | 0.010 | -2.49% | 12.24% | **-14.73 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| S&P 500 vs Oro (spot) | 0.061 | -2.49% | 2.74% | **-5.23 pp** |
| EUR/USD vs Indice dollaro DXY | 0.014 | 0.37% | 0.16% | **0.21 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.133 | 2.85% | 2.74% | **0.11 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -2.49% | -2.42% | **-0.07 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 2.74% | 2.70% | **0.04 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.43 | 2026-09-09 | 0.04 |
| US 10Y Treasury Rate | 4.83 | 2026-09-09 | 0.03 |
| US 30Y Treasury Rate | 5.28 | 2026-09-09 | 0.03 |
| Spread 10Y-2Y USA | 0.39 | 2026-09-10 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **40.0 bp**, 30Y-10Y **45.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.4600 | 15.35% | 80.09% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 99.2830 | 20.59% | 43.05% | -13.59% |
| Bitcoin | 76 991.7674 | 12.24% | 35.39% | -5.72% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 463.2066 | 16.65% | 30.94% | -5.78% |
| US 5Y Treasury Yield | 4.6100 | n/d | 13.18% | -0.66% |
| Nasdaq Composite | 26 081.7200 | -2.42% | 11.92% | -7.00% |
| US 10Y Treasury Yield | 4.8300 | 2.85% | 10.58% | -2.70% |
| USD/JPY | 156.1100 | -1.10% | 10.43% | -4.73% |
| Dow Jones | 52 064.1000 | -3.10% | 10.36% | -4.20% |
| S&P 500 | 7 591.7000 | -2.49% | 8.33% | -3.42% |
| Hang Seng | 25 511.1000 | 0.06% | 8.16% | -3.43% |
| Oro (spot) | 4 693.0000 | 2.74% | 7.56% | -4.96% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
