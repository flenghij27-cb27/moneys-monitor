# Moneys Monitor - Report di mercato

Generato: `2026-11-20T15:01:13+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-20T14:59:37+00:00` (565 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.75% | 0.00% | **-0.75 pp** |
| 1w | -2.12% | 0.00% | **-2.12 pp** |
| 1m | -8.24% | 0.00% | **-8.24 pp** |
| 3m | -10.79% | 0.00% | **-10.79 pp** |
| 6m | -1.99% | 16.43% | **-18.43 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.80% | | Solana | -3.02% |
| 2 | Gas naturale | 3.33% | | Nasdaq Composite | -2.25% |
| 3 | USD/JPY | 1.07% | | Dow Jones | -2.19% |
| 4 | Petrolio Brent | 0.87% | | GBP/USD | -1.19% |
| 5 | Indice dollaro Fed (broad) | 0.63% | | Ethereum | -1.12% |
| 6 | EUR/USD | 0.22% | | US 30Y Treasury Yield | -0.92% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 52.09% | | Petrolio Brent | -26.56% |
| 2 | US 10Y Treasury Yield | 1.81% | | Petrolio WTI | -12.15% |
| 3 | US 5Y Treasury Yield | 1.66% | | Dow Jones | -6.12% |
| 4 | US 30Y Treasury Yield | 1.12% | | Nasdaq Composite | -5.86% |
| 5 | USD/JPY | 1.00% | | Bitcoin | -5.20% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Ethereum | -4.74% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 70.50% | | Solana | -25.34% |
| 2 | Gas naturale | 14.73% | | Ethereum | -22.25% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -19.78% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -9.63% |
| 5 | USD/JPY | 0.42% | | Dow Jones | -7.11% |
| 6 | FTSE MIB | 0.00% | | S&P 500 | -5.43% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.143 | -5.43% | 70.50% | **-75.93 pp** |
| S&P 500 vs Bitcoin | 0.016 | -5.43% | -19.78% | **14.35 pp** |
| S&P 500 vs Oro (spot) | 0.015 | -5.43% | 0.00% | **-5.43 pp** |
| S&P 500 vs Nasdaq Composite | -0.257 | -5.43% | -9.63% | **4.20 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | -0.035 | -2.15% | 0.00% | **-2.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.015 | -1.55% | 0.00% | **-1.55 pp** |
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
| VIX (volatilita) | 28.4400 | 70.50% | 300.96% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 70.8631 | -25.34% | 46.73% | -41.96% |
| Ethereum | 1 739.9777 | -22.25% | 46.64% | -37.21% |
| Bitcoin | 61 634.3567 | -19.78% | 34.92% | -28.93% |
| Nasdaq Composite | 23 879.2000 | -9.63% | 32.22% | -13.48% |
| US 5Y Treasury Yield | 4.8900 | -1.01% | 24.36% | -9.82% |
| S&P 500 | 7 323.6300 | -5.43% | 24.15% | -6.33% |
| Dow Jones | 49 097.0600 | -7.11% | 22.35% | -9.66% |
| US 10Y Treasury Yield | 5.0700 | -1.55% | 20.40% | -8.85% |
| US 30Y Treasury Yield | 5.4100 | -1.28% | 15.25% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
