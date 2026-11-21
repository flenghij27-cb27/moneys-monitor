# Moneys Monitor - Report di mercato

Generato: `2026-11-21T14:21:42+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-21T14:21:08+00:00` (568 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.37% | 0.00% | **0.37 pp** |
| 1w | -2.74% | 0.00% | **-2.74 pp** |
| 1m | -9.00% | 0.00% | **-9.00 pp** |
| 3m | -11.38% | 0.00% | **-11.38 pp** |
| 6m | -1.39% | 20.19% | **-21.57 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.80% | | Nasdaq Composite | -2.25% |
| 2 | Ethereum | 3.98% | | S&P 500 | -2.02% |
| 3 | Gas naturale | 3.33% | | Dow Jones | -1.93% |
| 4 | Bitcoin | 2.09% | | GBP/USD | -1.19% |
| 5 | Solana | 1.91% | | US 5Y Treasury Yield | -0.61% |
| 6 | USD/JPY | 1.07% | | US 10Y Treasury Yield | -0.59% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 52.09% | | Petrolio Brent | -26.56% |
| 2 | USD/JPY | 1.00% | | Petrolio WTI | -12.15% |
| 3 | Indice dollaro Fed (broad) | 0.86% | | Dow Jones | -8.02% |
| 4 | FTSE MIB | 0.00% | | Ethereum | -7.35% |
| 5 | Euro Stoxx 50 | 0.00% | | Bitcoin | -7.14% |
| 6 | Nikkei 225 | 0.00% | | Nasdaq Composite | -5.86% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 70.50% | | Solana | -26.62% |
| 2 | Gas naturale | 14.73% | | Ethereum | -25.09% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -22.30% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -9.63% |
| 5 | USD/JPY | 0.42% | | Dow Jones | -8.93% |
| 6 | FTSE MIB | 0.00% | | S&P 500 | -6.31% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.061 | -6.31% | 70.50% | **-76.81 pp** |
| S&P 500 vs Bitcoin | -0.001 | -6.31% | -22.30% | **15.99 pp** |
| S&P 500 vs Oro (spot) | 0.018 | -6.31% | 0.00% | **-6.31 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| S&P 500 vs Nasdaq Composite | 0.120 | -6.31% | -9.63% | **3.32 pp** |
| EUR/USD vs Indice dollaro DXY | -0.035 | -1.92% | 0.00% | **-1.92 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.013 | -1.56% | 0.00% | **-1.56 pp** |
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
| VIX (volatilita) | 28.4400 | 70.50% | 300.96% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Ethereum | 1 685.8606 | -25.09% | 55.54% | -41.49% |
| Solana | 70.3813 | -26.62% | 50.06% | -43.44% |
| Bitcoin | 60 233.8447 | -22.30% | 39.15% | -31.96% |
| Nasdaq Composite | 23 879.2000 | -9.63% | 32.22% | -13.48% |
| S&P 500 | 7 175.8300 | -6.31% | 24.84% | -8.22% |
| US 5Y Treasury Yield | 4.8600 | -1.62% | 24.42% | -9.82% |
| Dow Jones | 48 147.3300 | -8.93% | 22.84% | -11.41% |
| US 10Y Treasury Yield | 5.0400 | -1.56% | 20.47% | -8.85% |
| US 30Y Treasury Yield | 5.4000 | -0.37% | 15.27% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
