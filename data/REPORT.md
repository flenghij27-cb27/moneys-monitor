# Moneys Monitor - Report di mercato

Generato: `2026-11-19T02:43:55+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-19T02:43:19+00:00` (561 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.23% | 0.00% | **0.23 pp** |
| 1w | -1.25% | 0.00% | **-1.25 pp** |
| 1m | -8.09% | 0.00% | **-8.09 pp** |
| 3m | -8.56% | 0.00% | **-8.56 pp** |
| 6m | -0.71% | 15.71% | **-16.42 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 11.13% | | GBP/USD | -1.19% |
| 2 | Gas naturale | 3.33% | | Dow Jones | -1.11% |
| 3 | Solana | 1.20% | | Nasdaq Composite | -0.74% |
| 4 | Ethereum | 1.12% | | US 5Y Treasury Yield | -0.61% |
| 5 | USD/JPY | 1.07% | | US 10Y Treasury Yield | -0.39% |
| 6 | Bitcoin | 0.90% | | S&P 500 | -0.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 30.83% | | Petrolio Brent | -26.56% |
| 2 | US 5Y Treasury Yield | 4.93% | | Petrolio WTI | -12.15% |
| 3 | US 10Y Treasury Yield | 4.51% | | Bitcoin | -4.40% |
| 4 | US 30Y Treasury Yield | 3.80% | | Dow Jones | -4.36% |
| 5 | Solana | 1.74% | | S&P 500 | -3.88% |
| 6 | USD/JPY | 1.00% | | Gas naturale | -3.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 38.07% | | Solana | -24.18% |
| 2 | Gas naturale | 14.73% | | Ethereum | -21.67% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -20.72% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -8.93% |
| 5 | US 30Y Treasury Yield | 0.55% | | S&P 500 | -5.43% |
| 6 | USD/JPY | 0.42% | | Dow Jones | -4.38% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.625 | -5.43% | 38.07% | **-43.50 pp** |
| S&P 500 vs Bitcoin | -0.015 | -5.43% | -20.72% | **15.29 pp** |
| S&P 500 vs Oro (spot) | -0.066 | -5.43% | 0.00% | **-5.43 pp** |
| S&P 500 vs Nasdaq Composite | 0.775 | -5.43% | -8.93% | **3.50 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | -0.037 | -2.20% | 0.00% | **-2.20 pp** |
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
| VIX (volatilita) | 25.4600 | 38.07% | 300.12% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Ethereum | 1 770.3315 | -21.67% | 47.41% | -36.82% |
| Solana | 73.2279 | -24.18% | 47.30% | -41.42% |
| Bitcoin | 62 628.5701 | -20.72% | 36.08% | -28.43% |
| Nasdaq Composite | 24 328.3800 | -8.93% | 31.92% | -11.90% |
| US 5Y Treasury Yield | 4.9000 | 0.20% | 24.35% | -9.82% |
| S&P 500 | 7 323.6300 | -5.43% | 24.15% | -6.33% |
| Dow Jones | 50 198.1700 | -4.38% | 21.30% | -7.64% |
| US 10Y Treasury Yield | 5.1000 | 0.20% | 20.40% | -8.85% |
| US 30Y Treasury Yield | 5.4600 | 0.55% | 15.41% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
