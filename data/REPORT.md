# Moneys Monitor - Report di mercato

Generato: `2026-10-12T14:40:35+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-12T14:39:58+00:00` (444 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.18% | 0.00% | **-0.18 pp** |
| 1w | -0.67% | 0.00% | **-0.67 pp** |
| 1m | -1.33% | 0.00% | **-1.33 pp** |
| 3m | 11.63% | 7.11% | **4.52 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | Indice dollaro Fed (broad) | 0.88% | | VIX (volatilita) | -3.70% |
| 3 | Dow Jones | 0.83% | | Solana | -1.67% |
| 4 | Nasdaq Composite | 0.64% | | US 30Y Treasury Yield | -1.23% |
| 5 | S&P 500 | 0.59% | | US 10Y Treasury Yield | -1.14% |
| 6 | USD/JPY | 0.40% | | Bitcoin | -1.05% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -5.81% |
| 2 | Petrolio WTI | 5.20% | | VIX (volatilita) | -3.07% |
| 3 | Gas naturale | 4.48% | | GBP/USD | -2.37% |
| 4 | Indice dollaro Fed (broad) | 2.22% | | Ethereum | -1.84% |
| 5 | S&P 500 | 1.15% | | USD/JPY | -1.35% |
| 6 | Dow Jones | 0.93% | | Bitcoin | -0.80% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Ethereum | -8.84% |
| 2 | Petrolio WTI | 15.44% | | Solana | -7.66% |
| 3 | Gas naturale | 10.14% | | Bitcoin | -4.61% |
| 4 | US 5Y Treasury Yield | 8.24% | | EUR/USD | -3.55% |
| 5 | US 10Y Treasury Yield | 8.07% | | VIX (volatilita) | -3.01% |
| 6 | US 30Y Treasury Yield | 6.06% | | GBP/USD | -2.02% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.104 | 8.07% | 0.00% | **8.07 pp** |
| S&P 500 vs Bitcoin | 0.025 | 2.90% | -4.61% | **7.51 pp** |
| S&P 500 vs VIX (volatilita) | 0.120 | 2.90% | -3.01% | **5.91 pp** |
| EUR/USD vs Indice dollaro DXY | 0.053 | -3.55% | 0.00% | **-3.55 pp** |
| S&P 500 vs Oro (spot) | 0.285 | 2.90% | 0.00% | **2.90 pp** |
| S&P 500 vs Nasdaq Composite | 0.948 | 2.90% | 4.92% | **-2.02 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.75 | 2026-10-08 | -0.02 |
| US 10Y Treasury Rate | 5.22 | 2026-10-08 | -0.06 |
| US 30Y Treasury Rate | 5.60 | 2026-10-08 | -0.07 |
| Spread 10Y-2Y USA | 0.44 | 2026-10-09 | -0.03 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 14.8400 | -3.01% | 99.13% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 109.4088 | -7.66% | 35.37% | -13.59% |
| Ethereum | 2 525.9909 | -8.84% | 24.75% | -10.76% |
| US 5Y Treasury Yield | 4.9900 | 8.24% | 18.55% | -1.96% |
| Bitcoin | 82 720.7164 | -4.61% | 16.95% | -6.86% |
| US 10Y Treasury Yield | 5.2200 | 8.07% | 16.70% | -2.70% |
| Nasdaq Composite | 27 366.1700 | 4.92% | 14.41% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 6.06% | 13.60% | -1.49% |
| S&P 500 | 7 811.5400 | 2.90% | 9.95% | -3.42% |
| Dow Jones | 51 654.9500 | -0.79% | 9.76% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
