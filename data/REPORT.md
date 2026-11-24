# Moneys Monitor - Report di mercato

Generato: `2026-11-24T05:26:18+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-24T05:25:47+00:00` (575 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.38% | 0.00% | **-1.38 pp** |
| 1w | -2.20% | 0.00% | **-2.20 pp** |
| 1m | -9.12% | 0.00% | **-9.12 pp** |
| 3m | -12.50% | 0.00% | **-12.50 pp** |
| 6m | -0.24% | 19.01% | **-19.25 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 26.20% | | S&P 500 | -3.70% |
| 2 | Gas naturale | 3.33% | | Solana | -3.17% |
| 3 | Dow Jones | 3.01% | | US 5Y Treasury Yield | -3.09% |
| 4 | Petrolio Brent | 0.87% | | Ethereum | -2.95% |
| 5 | Indice dollaro Fed (broad) | 0.77% | | US 10Y Treasury Yield | -2.38% |
| 6 | FTSE MIB | 0.00% | | Nasdaq Composite | -2.25% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 85.96% | | Petrolio Brent | -26.56% |
| 2 | Indice dollaro Fed (broad) | 1.81% | | Petrolio WTI | -12.15% |
| 3 | USD/JPY | 0.48% | | S&P 500 | -8.61% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -5.86% |
| 5 | Euro Stoxx 50 | 0.00% | | US 5Y Treasury Yield | -5.42% |
| 6 | Nikkei 225 | 0.00% | | US 10Y Treasury Yield | -4.47% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 88.60% | | Ethereum | -25.70% |
| 2 | Gas naturale | 14.73% | | Solana | -23.56% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -22.14% |
| 4 | Petrolio Brent | 2.35% | | S&P 500 | -10.15% |
| 5 | FTSE MIB | 0.00% | | Nasdaq Composite | -9.63% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -5.02% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.143 | -10.15% | 88.60% | **-98.75 pp** |
| S&P 500 vs Bitcoin | 0.042 | -10.15% | -22.14% | **11.99 pp** |
| S&P 500 vs Oro (spot) | 0.042 | -10.15% | 0.00% | **-10.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | -4.09% | 0.00% | **-4.09 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.017 | -2.27% | 0.00% | **-2.27 pp** |
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
| US 2Y Treasury Rate | 4.63 | 2026-11-20 | -0.13 |
| US 10Y Treasury Rate | 4.92 | 2026-11-20 | -0.12 |
| US 30Y Treasury Rate | 5.31 | 2026-11-20 | -0.09 |
| Spread 10Y-2Y USA | 0.29 | 2026-11-23 | 0.00 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 35.8900 | 88.60% | 311.54% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 71.6426 | -23.56% | 54.07% | -43.44% |
| Ethereum | 1 704.6075 | -25.70% | 51.26% | -41.49% |
| Bitcoin | 60 619.3538 | -22.14% | 37.04% | -31.96% |
| Nasdaq Composite | 23 879.2000 | -9.63% | 32.22% | -13.48% |
| S&P 500 | 6 910.3900 | -10.15% | 27.42% | -11.62% |
| Dow Jones | 49 595.3100 | -5.02% | 25.78% | -11.41% |
| US 5Y Treasury Yield | 4.7100 | -4.85% | 23.81% | -9.82% |
| US 10Y Treasury Yield | 4.9200 | -4.09% | 18.71% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.3100 | -2.03% | 13.91% | -7.41% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
