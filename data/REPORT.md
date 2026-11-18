# Moneys Monitor - Report di mercato

Generato: `2026-11-18T22:52:46+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-18T22:52:14+00:00` (560 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.37% | 0.00% | **-1.37 pp** |
| 1w | -3.15% | 0.00% | **-3.15 pp** |
| 1m | -9.18% | 0.00% | **-9.18 pp** |
| 3m | -8.53% | 0.00% | **-8.53 pp** |
| 6m | -0.49% | 17.52% | **-18.00 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 11.13% | | Bitcoin | -4.44% |
| 2 | Gas naturale | 3.33% | | Ethereum | -3.99% |
| 3 | USD/JPY | 1.07% | | Solana | -3.46% |
| 4 | Petrolio Brent | 0.87% | | Dow Jones | -1.64% |
| 5 | Indice dollaro Fed (broad) | 0.63% | | GBP/USD | -1.19% |
| 6 | FTSE MIB | 0.00% | | S&P 500 | -1.03% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 30.83% | | Petrolio Brent | -26.56% |
| 2 | US 5Y Treasury Yield | 4.93% | | Petrolio WTI | -12.15% |
| 3 | US 10Y Treasury Yield | 4.51% | | Ethereum | -9.04% |
| 4 | US 30Y Treasury Yield | 3.80% | | Bitcoin | -9.03% |
| 5 | USD/JPY | 1.00% | | Solana | -8.13% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Gas naturale | -3.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 38.07% | | Solana | -29.10% |
| 2 | Gas naturale | 14.73% | | Ethereum | -25.52% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -23.37% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -8.93% |
| 5 | US 30Y Treasury Yield | 0.55% | | S&P 500 | -4.90% |
| 6 | USD/JPY | 0.42% | | GBP/USD | -2.37% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.031 | -4.90% | 38.07% | **-42.97 pp** |
| S&P 500 vs Bitcoin | -0.014 | -4.90% | -23.37% | **18.47 pp** |
| S&P 500 vs Oro (spot) | -0.067 | -4.90% | 0.00% | **-4.90 pp** |
| S&P 500 vs Nasdaq Composite | 0.088 | -4.90% | -8.93% | **4.03 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.056 | -2.20% | 0.00% | **-2.20 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.058 | 0.20% | 0.00% | **0.20 pp** |
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
| Ethereum | 1 750.7963 | -25.52% | 46.67% | -36.82% |
| Solana | 72.3606 | -29.10% | 46.43% | -41.42% |
| Bitcoin | 62 068.3643 | -23.37% | 35.86% | -28.43% |
| Nasdaq Composite | 24 328.3800 | -8.93% | 31.92% | -11.90% |
| S&P 500 | 7 340.5300 | -4.90% | 24.35% | -6.12% |
| US 5Y Treasury Yield | 4.9000 | 0.20% | 24.35% | -9.82% |
| Dow Jones | 50 759.4200 | -2.32% | 21.29% | -6.60% |
| US 10Y Treasury Yield | 5.1000 | 0.20% | 20.40% | -8.85% |
| US 30Y Treasury Yield | 5.4600 | 0.55% | 15.41% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
