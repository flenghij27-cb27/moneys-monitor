# Moneys Monitor - Report di mercato

Generato: `2026-09-14T23:57:15+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-14T23:56:43+00:00` (357 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.86% | 0.00% | **0.86 pp** |
| 1w | 0.14% | 0.00% | **0.14 pp** |
| 1m | 1.04% | -0.76% | **1.80 pp** |
| 3m | 10.30% | 13.79% | **-3.49 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | VIX (volatilita) | -11.21% |
| 2 | Petrolio WTI | 6.32% | | Gas naturale | -3.10% |
| 3 | Solana | 3.04% | | USD/JPY | -1.54% |
| 4 | Bitcoin | 1.98% | | US 30Y Treasury Yield | -0.37% |
| 5 | Ethereum | 1.76% | | EUR/USD | -0.35% |
| 6 | Nasdaq Composite | 0.96% | | Dow Jones | -0.29% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | USD/JPY | -3.32% |
| 2 | Petrolio WTI | 11.72% | | Dow Jones | -1.86% |
| 3 | VIX (volatilita) | 10.61% | | S&P 500 | -1.17% |
| 4 | US 5Y Treasury Yield | 5.75% | | Nasdaq Composite | -0.94% |
| 5 | US 10Y Treasury Yield | 3.98% | | GBP/USD | -0.76% |
| 6 | Ethereum | 2.29% | | EUR/USD | -0.61% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | USD/JPY | -2.56% |
| 2 | Petrolio WTI | 26.39% | | Dow Jones | -2.44% |
| 3 | VIX (volatilita) | 11.16% | | Hang Seng | -1.92% |
| 4 | Solana | 8.21% | | Argento (spot) | -1.78% |
| 5 | US 10Y Treasury Yield | 5.62% | | S&P 500 | -1.65% |
| 6 | Gas naturale | 5.20% | | Nasdaq Composite | -1.48% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.122 | -1.65% | 11.16% | **-12.81 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.136 | 5.62% | 0.26% | **5.36 pp** |
| S&P 500 vs Bitcoin | -0.050 | -1.65% | 0.97% | **-2.62 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 0.26% | -1.78% | **2.04 pp** |
| S&P 500 vs Oro (spot) | -0.181 | -1.65% | 0.26% | **-1.91 pp** |
| EUR/USD vs Indice dollaro DXY | 0.052 | -0.27% | 0.12% | **-0.39 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -1.65% | -1.48% | **-0.17 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.63 | 2026-09-11 | 0.07 |
| US 10Y Treasury Rate | 4.96 | 2026-09-11 | 0.01 |
| US 30Y Treasury Rate | 5.35 | 2026-09-11 | -0.02 |
| Spread 10Y-2Y USA | 0.32 | 2026-09-14 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **33.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.8400 | 11.16% | 92.61% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 102.5337 | 8.21% | 42.25% | -13.59% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 516.1300 | 3.04% | 29.80% | -5.78% |
| Bitcoin | 78 174.0195 | 0.97% | 27.85% | -5.72% |
| US 5Y Treasury Yield | 4.7800 | n/d | 16.58% | -0.66% |
| US 10Y Treasury Yield | 4.9600 | 5.62% | 13.37% | -2.70% |
| Nasdaq Composite | 26 333.0400 | -1.48% | 12.52% | -7.00% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| Dow Jones | 52 421.2000 | -2.44% | 11.03% | -4.20% |
| US 30Y Treasury Yield | 5.3500 | n/d | 9.36% | -0.57% |
| S&P 500 | 7 656.9800 | -1.65% | 9.03% | -3.42% |
| Hang Seng | 25 511.1000 | -1.92% | 6.71% | -3.43% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
