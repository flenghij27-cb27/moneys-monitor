# Moneys Monitor - Report di mercato

Generato: `2026-11-19T22:56:15+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-19T22:55:47+00:00` (563 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.18% | 0.00% | **0.18 pp** |
| 1w | -1.52% | 0.00% | **-1.52 pp** |
| 1m | -8.08% | 0.00% | **-8.08 pp** |
| 3m | -8.66% | 0.00% | **-8.66 pp** |
| 6m | -0.89% | 15.71% | **-16.61 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.33% | | VIX (volatilita) | -3.53% |
| 2 | USD/JPY | 1.07% | | GBP/USD | -1.19% |
| 3 | Solana | 0.98% | | Dow Jones | -1.11% |
| 4 | Petrolio Brent | 0.87% | | US 30Y Treasury Yield | -0.92% |
| 5 | Indice dollaro Fed (broad) | 0.63% | | US 10Y Treasury Yield | -0.59% |
| 6 | Ethereum | 0.50% | | S&P 500 | -0.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 40.42% | | Petrolio Brent | -26.56% |
| 2 | US 10Y Treasury Yield | 1.81% | | Petrolio WTI | -12.15% |
| 3 | US 5Y Treasury Yield | 1.66% | | Bitcoin | -5.13% |
| 4 | Solana | 1.51% | | Dow Jones | -4.36% |
| 5 | US 30Y Treasury Yield | 1.12% | | Nasdaq Composite | -4.07% |
| 6 | USD/JPY | 1.00% | | S&P 500 | -3.88% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 41.88% | | Solana | -24.35% |
| 2 | Gas naturale | 14.73% | | Ethereum | -22.14% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -21.32% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -7.57% |
| 5 | USD/JPY | 0.42% | | S&P 500 | -5.43% |
| 6 | FTSE MIB | 0.00% | | Dow Jones | -4.38% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.030 | -5.43% | 41.88% | **-47.31 pp** |
| S&P 500 vs Bitcoin | -0.014 | -5.43% | -21.32% | **15.89 pp** |
| S&P 500 vs Oro (spot) | -0.066 | -5.43% | 0.00% | **-5.43 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.057 | -2.15% | 0.00% | **-2.15 pp** |
| S&P 500 vs Nasdaq Composite | 0.087 | -5.43% | -7.57% | **2.14 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.057 | -1.55% | 0.00% | **-1.55 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.80 | 2026-11-18 | 0.00 |
| US 10Y Treasury Rate | 5.07 | 2026-11-18 | -0.03 |
| US 30Y Treasury Rate | 5.41 | 2026-11-18 | -0.05 |
| Spread 10Y-2Y USA | 0.28 | 2026-11-19 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **27.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 24.5600 | 41.88% | 300.09% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 73.0688 | -24.35% | 47.16% | -41.42% |
| Ethereum | 1 759.6242 | -22.14% | 47.07% | -36.82% |
| Bitcoin | 62 154.2451 | -21.32% | 35.64% | -28.43% |
| Nasdaq Composite | 24 429.8800 | -7.57% | 32.02% | -11.90% |
| US 5Y Treasury Yield | 4.8900 | -1.01% | 24.36% | -9.82% |
| S&P 500 | 7 323.6300 | -5.43% | 24.15% | -6.33% |
| Dow Jones | 50 198.1700 | -4.38% | 21.30% | -7.64% |
| US 10Y Treasury Yield | 5.0700 | -1.55% | 20.40% | -8.85% |
| US 30Y Treasury Yield | 5.4100 | -1.28% | 15.25% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
