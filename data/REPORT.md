# Moneys Monitor - Report di mercato

Generato: `2026-10-08T12:58:28+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-08T12:57:58+00:00` (432 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.67% | 0.00% | **-0.67 pp** |
| 1w | -1.04% | 0.00% | **-1.04 pp** |
| 1m | 2.79% | 0.00% | **2.79 pp** |
| 3m | 12.73% | 13.90% | **-1.17 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | Indice dollaro Fed (broad) | 0.88% | | VIX (volatilita) | -3.29% |
| 3 | USD/JPY | 0.40% | | Solana | -3.19% |
| 4 | Petrolio WTI | 0.08% | | Ethereum | -1.70% |
| 5 | FTSE MIB | 0.00% | | Bitcoin | -1.40% |
| 6 | Euro Stoxx 50 | 0.00% | | EUR/USD | -0.82% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | VIX (volatilita) | -6.42% |
| 2 | Petrolio WTI | 5.20% | | Solana | -6.03% |
| 3 | Gas naturale | 4.48% | | Ethereum | -5.86% |
| 4 | Nasdaq Composite | 2.52% | | Bitcoin | -2.98% |
| 5 | Indice dollaro Fed (broad) | 2.22% | | GBP/USD | -2.37% |
| 6 | S&P 500 | 1.96% | | EUR/USD | -1.57% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | VIX (volatilita) | -8.14% |
| 2 | Petrolio WTI | 15.44% | | EUR/USD | -3.76% |
| 3 | Solana | 10.89% | | Dow Jones | -3.04% |
| 4 | US 5Y Treasury Yield | 10.79% | | GBP/USD | -2.02% |
| 5 | US 10Y Treasury Yield | 10.25% | | USD/JPY | -0.95% |
| 6 | Gas naturale | 10.14% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.028 | 10.25% | 0.00% | **10.25 pp** |
| S&P 500 vs VIX (volatilita) | -0.046 | 1.67% | -8.14% | **9.81 pp** |
| S&P 500 vs Bitcoin | -0.089 | 1.67% | 7.68% | **-6.01 pp** |
| EUR/USD vs Indice dollaro DXY | -0.073 | -3.76% | 0.00% | **-3.76 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 1.67% | 4.23% | **-2.56 pp** |
| S&P 500 vs Oro (spot) | -0.159 | 1.67% | 0.00% | **1.67 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.79 | 2026-10-06 | -0.05 |
| US 10Y Treasury Rate | 5.27 | 2026-10-06 | -0.04 |
| US 30Y Treasury Rate | 5.64 | 2026-10-06 | -0.02 |
| Spread 10Y-2Y USA | 0.51 | 2026-10-07 | 0.03 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **48.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.0100 | -8.14% | 103.64% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 112.4419 | 10.89% | 40.46% | -13.59% |
| Bitcoin | 82 223.8270 | 7.68% | 29.15% | -6.86% |
| Ethereum | 2 529.5895 | 3.44% | 28.31% | -8.71% |
| US 5Y Treasury Yield | 5.0300 | 10.79% | 20.54% | -1.65% |
| US 10Y Treasury Yield | 5.2700 | 10.25% | 17.56% | -2.70% |
| Nasdaq Composite | 27 538.6900 | 4.23% | 13.93% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6400 | 7.63% | 13.46% | -1.49% |
| S&P 500 | 7 801.7700 | 1.67% | 10.27% | -3.42% |
| Dow Jones | 51 179.8700 | -3.04% | 10.10% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
