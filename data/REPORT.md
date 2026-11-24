# Moneys Monitor - Report di mercato

Generato: `2026-11-24T17:05:53+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-24T17:05:22+00:00` (576 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -2.19% | 0.00% | **-2.19 pp** |
| 1w | -3.01% | 0.00% | **-3.01 pp** |
| 1m | -9.75% | 0.00% | **-9.75 pp** |
| 3m | -13.03% | 0.00% | **-13.03 pp** |
| 6m | -1.21% | 19.01% | **-20.22 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.33% | | VIX (volatilita) | -25.83% |
| 2 | Dow Jones | 3.01% | | Solana | -6.84% |
| 3 | Petrolio Brent | 0.87% | | Ethereum | -5.12% |
| 4 | Indice dollaro Fed (broad) | 0.77% | | Bitcoin | -3.95% |
| 5 | EUR/USD | 0.22% | | S&P 500 | -3.70% |
| 6 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -3.09% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 16.19% | | Petrolio Brent | -26.56% |
| 2 | Indice dollaro Fed (broad) | 1.81% | | Petrolio WTI | -12.15% |
| 3 | USD/JPY | 0.48% | | S&P 500 | -8.61% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -5.86% |
| 5 | Euro Stoxx 50 | 0.00% | | Solana | -5.67% |
| 6 | Nikkei 225 | 0.00% | | US 5Y Treasury Yield | -5.42% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 36.86% | | Ethereum | -27.36% |
| 2 | Gas naturale | 14.73% | | Solana | -26.46% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -23.87% |
| 4 | Petrolio Brent | 2.35% | | S&P 500 | -10.15% |
| 5 | FTSE MIB | 0.00% | | Nasdaq Composite | -9.63% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -5.02% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.166 | -10.15% | 36.86% | **-47.01 pp** |
| S&P 500 vs Bitcoin | 0.077 | -10.15% | -23.87% | **13.72 pp** |
| S&P 500 vs Oro (spot) | 0.042 | -10.15% | 0.00% | **-10.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | -4.09% | 0.00% | **-4.09 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.029 | -2.01% | 0.00% | **-2.01 pp** |
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
| VIX (volatilita) | 26.6200 | 36.86% | 328.23% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 68.9259 | -26.46% | 57.21% | -43.55% |
| Ethereum | 1 666.5406 | -27.36% | 52.53% | -41.49% |
| Bitcoin | 59 272.6101 | -23.87% | 38.16% | -31.96% |
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
