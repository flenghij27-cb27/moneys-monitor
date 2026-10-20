# Moneys Monitor - Report di mercato

Generato: `2026-10-20T00:31:33+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-20T00:30:43+00:00` (469 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.01% | 0.00% | **0.01 pp** |
| 1w | -0.66% | 0.00% | **-0.66 pp** |
| 1m | -2.26% | 0.00% | **-2.26 pp** |
| 3m | 9.85% | 5.32% | **4.53 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 21.45% | | Bitcoin | -0.46% |
| 2 | Gas naturale | 6.27% | | US 5Y Treasury Yield | -0.41% |
| 3 | Petrolio WTI | 5.89% | | EUR/USD | -0.25% |
| 4 | Petrolio Brent | 0.88% | | USD/JPY | -0.21% |
| 5 | GBP/USD | 0.76% | | US 10Y Treasury Yield | -0.20% |
| 6 | S&P 500 | 0.41% | | Indice dollaro Fed (broad) | -0.16% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 34.70% | | US 30Y Treasury Yield | -3.04% |
| 2 | Petrolio Brent | 15.56% | | US 10Y Treasury Yield | -2.49% |
| 3 | Gas naturale | 14.59% | | US 5Y Treasury Yield | -2.00% |
| 4 | Petrolio WTI | 4.78% | | Nasdaq Composite | -1.77% |
| 5 | USD/JPY | 2.79% | | Ethereum | -1.76% |
| 6 | Indice dollaro Fed (broad) | 2.70% | | S&P 500 | -1.49% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -12.36% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -11.04% |
| 3 | VIX (volatilita) | 16.90% | | Bitcoin | -2.52% |
| 4 | Gas naturale | 15.16% | | EUR/USD | -2.05% |
| 5 | Nasdaq Composite | 2.83% | | GBP/USD | -1.22% |
| 6 | US 10Y Treasury Yield | 1.60% | | USD/JPY | -0.88% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs VIX (volatilita) | 0.003 | 0.53% | 16.90% | **-16.37 pp** |
| S&P 500 vs Bitcoin | 0.151 | 0.53% | -2.52% | **3.05 pp** |
| S&P 500 vs Nasdaq Composite | -0.133 | 0.53% | 2.83% | **-2.30 pp** |
| EUR/USD vs Indice dollaro DXY | -0.133 | -2.05% | 0.00% | **-2.05 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.098 | 1.60% | 0.00% | **1.60 pp** |
| S&P 500 vs Oro (spot) | 0.015 | 0.53% | 0.00% | **0.53 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.74 | 2026-10-16 | -0.03 |
| US 10Y Treasury Rate | 5.09 | 2026-10-16 | -0.01 |
| US 30Y Treasury Rate | 5.43 | 2026-10-16 | 0.00 |
| Spread 10Y-2Y USA | 0.38 | 2026-10-19 | 0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **35.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.9900 | 16.90% | 116.39% | -31.22% |
| Petrolio Brent | 126.5500 | 42.82% | 107.21% | -21.50% |
| Petrolio WTI | 101.9100 | 22.98% | 72.41% | -18.71% |
| Gas naturale | 3.2200 | 15.16% | 56.78% | -18.87% |
| Solana | 104.4304 | -12.36% | 31.62% | -15.47% |
| Ethereum | 2 395.3675 | -11.04% | 27.56% | -13.58% |
| US 5Y Treasury Yield | 4.8900 | 0.62% | 18.86% | -3.93% |
| Bitcoin | 81 508.5223 | -2.52% | 18.01% | -6.86% |
| US 10Y Treasury Yield | 5.0900 | 1.60% | 17.56% | -4.14% |
| US 30Y Treasury Yield | 5.4300 | 1.50% | 14.83% | -4.23% |
| Nasdaq Composite | 26 713.0300 | 2.83% | 14.71% | -7.00% |
| USD/JPY | 158.0000 | -0.88% | 13.75% | -6.19% |
| S&P 500 | 7 690.7300 | 0.53% | 9.03% | -3.42% |
| Dow Jones | 51 966.0300 | 0.55% | 8.93% | -6.34% |
| Indice dollaro Fed (broad) | 121.4048 | n/d | 8.89% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
