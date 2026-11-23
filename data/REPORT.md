# Moneys Monitor - Report di mercato

Generato: `2026-11-23T17:35:19+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-23T17:34:43+00:00` (574 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.29% | 0.00% | **0.29 pp** |
| 1w | -1.25% | 0.00% | **-1.25 pp** |
| 1m | -8.06% | 0.00% | **-8.06 pp** |
| 3m | -12.10% | 0.00% | **-12.10 pp** |
| 6m | 0.83% | 19.01% | **-18.18 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 26.20% | | S&P 500 | -3.70% |
| 2 | Solana | 5.36% | | Nasdaq Composite | -2.25% |
| 3 | Gas naturale | 3.33% | | Dow Jones | -1.93% |
| 4 | Ethereum | 2.04% | | GBP/USD | -1.19% |
| 5 | Bitcoin | 1.40% | | US 5Y Treasury Yield | -0.61% |
| 6 | USD/JPY | 1.07% | | US 10Y Treasury Yield | -0.59% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 85.96% | | Petrolio Brent | -26.56% |
| 2 | Solana | 2.24% | | Petrolio WTI | -12.15% |
| 3 | USD/JPY | 1.00% | | S&P 500 | -8.61% |
| 4 | Indice dollaro Fed (broad) | 0.86% | | Dow Jones | -8.02% |
| 5 | Ethereum | 0.32% | | Nasdaq Composite | -5.86% |
| 6 | FTSE MIB | 0.00% | | Gas naturale | -3.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 88.60% | | Ethereum | -21.96% |
| 2 | Gas naturale | 14.73% | | Bitcoin | -19.58% |
| 3 | Petrolio WTI | 5.78% | | Solana | -19.30% |
| 4 | Petrolio Brent | 2.35% | | S&P 500 | -10.15% |
| 5 | USD/JPY | 0.42% | | Nasdaq Composite | -9.63% |
| 6 | FTSE MIB | 0.00% | | Dow Jones | -8.93% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.143 | -10.15% | 88.60% | **-98.75 pp** |
| S&P 500 vs Oro (spot) | 0.065 | -10.15% | 0.00% | **-10.15 pp** |
| S&P 500 vs Bitcoin | 0.055 | -10.15% | -19.58% | **9.43 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.028 | -2.27% | 0.00% | **-2.27 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | -1.56% | 0.00% | **-1.56 pp** |
| S&P 500 vs Nasdaq Composite | 0.749 | -10.15% | -9.63% | **-0.52 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.76 | 2026-11-19 | -0.04 |
| US 10Y Treasury Rate | 5.04 | 2026-11-19 | -0.03 |
| US 30Y Treasury Rate | 5.40 | 2026-11-19 | -0.01 |
| Spread 10Y-2Y USA | 0.29 | 2026-11-20 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **28.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 35.8900 | 88.60% | 311.54% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Ethereum | 1 756.4257 | -21.96% | 56.83% | -41.49% |
| Solana | 73.9846 | -19.30% | 54.18% | -43.44% |
| Bitcoin | 61 712.8239 | -19.58% | 40.02% | -31.96% |
| Nasdaq Composite | 23 879.2000 | -9.63% | 32.22% | -13.48% |
| S&P 500 | 6 910.3900 | -10.15% | 27.42% | -11.62% |
| US 5Y Treasury Yield | 4.8600 | -1.62% | 24.42% | -9.82% |
| Dow Jones | 48 147.3300 | -8.93% | 22.84% | -11.41% |
| US 10Y Treasury Yield | 5.0400 | -1.56% | 20.47% | -8.85% |
| US 30Y Treasury Yield | 5.4000 | -0.37% | 15.27% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
