# Moneys Monitor - Report di mercato

Generato: `2026-11-13T14:04:32+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-13T14:03:58+00:00` (544 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.44% | 0.00% | **-0.44 pp** |
| 1w | -2.42% | 0.00% | **-2.42 pp** |
| 1m | -6.16% | 0.00% | **-6.16 pp** |
| 3m | -5.97% | 0.00% | **-5.97 pp** |
| 6m | 5.92% | 15.60% | **-9.68 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.91% |
| 2 | US 5Y Treasury Yield | 3.00% | | VIX (volatilita) | -10.12% |
| 3 | US 10Y Treasury Yield | 2.05% | | Petrolio WTI | -10.06% |
| 4 | US 30Y Treasury Yield | 1.71% | | Bitcoin | -2.83% |
| 5 | S&P 500 | 1.31% | | Ethereum | -2.54% |
| 6 | USD/JPY | 0.48% | | EUR/USD | -0.41% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 5.30% | | Petrolio Brent | -26.55% |
| 2 | Nasdaq Composite | 4.32% | | Ethereum | -11.80% |
| 3 | Dow Jones | 1.50% | | Solana | -8.96% |
| 4 | US 5Y Treasury Yield | 1.48% | | Bitcoin | -8.40% |
| 5 | GBP/USD | 1.04% | | Petrolio WTI | -6.88% |
| 6 | S&P 500 | 0.67% | | EUR/USD | -1.27% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 14.54% | | Solana | -20.86% |
| 2 | Gas naturale | 9.77% | | Ethereum | -17.63% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -14.37% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -6.90% |
| 5 | Dow Jones | 1.31% | | US 10Y Treasury Yield | -4.96% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -4.46% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.024 | -1.88% | 14.54% | **-16.42 pp** |
| S&P 500 vs Bitcoin | -0.019 | -1.88% | -14.37% | **12.49 pp** |
| S&P 500 vs Nasdaq Composite | -0.302 | -1.88% | -6.90% | **5.02 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.030 | -4.96% | 0.00% | **-4.96 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Oro (spot) | 0.020 | -1.88% | 0.00% | **-1.88 pp** |
| EUR/USD vs Indice dollaro DXY | -0.008 | -1.02% | 0.00% | **-1.02 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.73 | 2026-11-10 | 0.17 |
| US 10Y Treasury Rate | 4.98 | 2026-11-10 | 0.10 |
| US 30Y Treasury Rate | 5.35 | 2026-11-10 | 0.09 |
| Spread 10Y-2Y USA | 0.24 | 2026-11-12 | -0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **25.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.4900 | 14.54% | 304.57% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Ethereum | 1 963.6698 | -17.63% | 43.82% | -29.13% |
| Solana | 81.3652 | -20.86% | 34.56% | -33.37% |
| Nasdaq Composite | 25 366.0900 | -6.90% | 31.50% | -11.90% |
| Bitcoin | 69 442.2448 | -14.37% | 31.22% | -19.92% |
| S&P 500 | 7 619.3800 | -1.88% | 23.62% | -5.95% |
| US 5Y Treasury Yield | 4.8100 | -4.18% | 22.54% | -9.82% |
| Dow Jones | 52 297.0900 | 1.31% | 20.32% | -6.34% |
| US 10Y Treasury Yield | 4.9800 | -4.96% | 19.20% | -8.85% |
| US 30Y Treasury Yield | 5.3500 | -4.46% | 15.63% | -7.41% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
