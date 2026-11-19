# Moneys Monitor - Report di mercato

Generato: `2026-11-19T15:22:55+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-19T15:22:20+00:00` (562 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.70% | 0.00% | **0.70 pp** |
| 1w | -1.01% | 0.00% | **-1.01 pp** |
| 1m | -7.68% | 0.00% | **-7.68 pp** |
| 3m | -8.27% | 0.00% | **-8.27 pp** |
| 6m | -0.27% | 15.71% | **-15.99 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.33% | | VIX (volatilita) | -3.53% |
| 2 | Solana | 2.98% | | GBP/USD | -1.19% |
| 3 | Ethereum | 2.07% | | Dow Jones | -1.11% |
| 4 | Bitcoin | 1.81% | | US 5Y Treasury Yield | -0.61% |
| 5 | USD/JPY | 1.07% | | US 10Y Treasury Yield | -0.39% |
| 6 | Petrolio Brent | 0.87% | | S&P 500 | -0.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 40.42% | | Petrolio Brent | -26.56% |
| 2 | US 5Y Treasury Yield | 4.93% | | Petrolio WTI | -12.15% |
| 3 | US 10Y Treasury Yield | 4.51% | | Dow Jones | -4.36% |
| 4 | US 30Y Treasury Yield | 3.80% | | Nasdaq Composite | -4.07% |
| 5 | Solana | 3.53% | | S&P 500 | -3.88% |
| 6 | USD/JPY | 1.00% | | Gas naturale | -3.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 41.88% | | Solana | -22.85% |
| 2 | Gas naturale | 14.73% | | Ethereum | -20.93% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -20.01% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -7.57% |
| 5 | US 30Y Treasury Yield | 0.55% | | S&P 500 | -5.43% |
| 6 | USD/JPY | 0.42% | | Dow Jones | -4.38% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.030 | -5.43% | 41.88% | **-47.31 pp** |
| S&P 500 vs Bitcoin | -0.016 | -5.43% | -20.01% | **14.58 pp** |
| S&P 500 vs Oro (spot) | -0.066 | -5.43% | 0.00% | **-5.43 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.057 | -2.15% | 0.00% | **-2.15 pp** |
| S&P 500 vs Nasdaq Composite | 0.087 | -5.43% | -7.57% | **2.14 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.016 | 0.20% | 0.00% | **0.20 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.80 | 2026-11-17 | -0.03 |
| US 10Y Treasury Rate | 5.10 | 2026-11-17 | -0.02 |
| US 30Y Treasury Rate | 5.46 | 2026-11-17 | 0.00 |
| Spread 10Y-2Y USA | 0.27 | 2026-11-18 | -0.03 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **30.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 24.5600 | 41.88% | 300.09% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 74.5190 | -22.85% | 48.92% | -41.42% |
| Ethereum | 1 787.1195 | -20.93% | 48.12% | -36.82% |
| Bitcoin | 63 192.8899 | -20.01% | 36.85% | -28.43% |
| Nasdaq Composite | 24 429.8800 | -7.57% | 32.02% | -11.90% |
| US 5Y Treasury Yield | 4.9000 | 0.20% | 24.35% | -9.82% |
| S&P 500 | 7 323.6300 | -5.43% | 24.15% | -6.33% |
| Dow Jones | 50 198.1700 | -4.38% | 21.30% | -7.64% |
| US 10Y Treasury Yield | 5.1000 | 0.20% | 20.40% | -8.85% |
| US 30Y Treasury Yield | 5.4600 | 0.55% | 15.41% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
