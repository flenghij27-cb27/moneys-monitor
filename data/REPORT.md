# Moneys Monitor - Report di mercato

Generato: `2026-10-15T10:59:59+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-15T10:59:28+00:00` (453 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.78% | 0.00% | **-0.78 pp** |
| 1w | -1.99% | 0.00% | **-1.99 pp** |
| 1m | -2.41% | 0.00% | **-2.41 pp** |
| 3m | 9.52% | 5.61% | **3.92 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 0.39% | | Ethereum | -2.22% |
| 3 | USD/JPY | 0.34% | | Nasdaq Composite | -1.88% |
| 4 | Indice dollaro Fed (broad) | 0.18% | | Solana | -1.77% |
| 5 | Petrolio WTI | 0.08% | | S&P 500 | -1.11% |
| 6 | EUR/USD | 0.06% | | Bitcoin | -0.80% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -7.34% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -5.90% |
| 3 | Gas naturale | 4.48% | | Nasdaq Composite | -3.07% |
| 4 | Indice dollaro Fed (broad) | 2.99% | | Bitcoin | -2.49% |
| 5 | VIX (volatilita) | 1.73% | | GBP/USD | -2.16% |
| 6 | USD/JPY | 1.43% | | US 10Y Treasury Yield | -1.88% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Solana | -12.57% |
| 2 | Petrolio WTI | 15.44% | | Ethereum | -11.98% |
| 3 | Gas naturale | 10.14% | | VIX (volatilita) | -7.23% |
| 4 | US 10Y Treasury Yield | 5.04% | | Bitcoin | -4.06% |
| 5 | US 5Y Treasury Yield | 4.60% | | EUR/USD | -2.98% |
| 6 | US 30Y Treasury Yield | 3.93% | | GBP/USD | -2.05% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| S&P 500 vs VIX (volatilita) | -0.043 | 1.76% | -7.23% | **8.99 pp** |
| S&P 500 vs Bitcoin | 0.036 | 1.76% | -4.06% | **5.82 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.034 | 5.04% | 0.00% | **5.04 pp** |
| EUR/USD vs Indice dollaro DXY | 0.007 | -2.98% | 0.00% | **-2.98 pp** |
| S&P 500 vs Oro (spot) | 0.283 | 1.76% | 0.00% | **1.76 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 1.76% | 2.74% | **-0.98 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.79 | 2026-10-13 | -0.01 |
| US 10Y Treasury Rate | 5.21 | 2026-10-13 | -0.03 |
| US 30Y Treasury Rate | 5.56 | 2026-10-13 | -0.04 |
| Spread 10Y-2Y USA | 0.37 | 2026-10-14 | -0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **42.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.2700 | -7.23% | 92.67% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 102.3081 | -12.57% | 32.40% | -16.21% |
| Ethereum | 2 365.3213 | -11.98% | 27.74% | -14.64% |
| US 5Y Treasury Yield | 5.0000 | 4.60% | 18.67% | -1.96% |
| Bitcoin | 80 940.7306 | -4.06% | 17.96% | -6.86% |
| US 10Y Treasury Yield | 5.2100 | 5.04% | 16.98% | -2.70% |
| Nasdaq Composite | 26 692.8700 | 2.74% | 15.81% | -7.00% |
| US 30Y Treasury Yield | 5.5600 | 3.93% | 13.79% | -1.94% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| S&P 500 | 7 718.9400 | 1.76% | 10.32% | -3.42% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |
| Dow Jones | 51 621.4800 | -0.91% | 8.66% | -6.34% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
