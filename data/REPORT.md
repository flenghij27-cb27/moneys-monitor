# Moneys Monitor - Report di mercato

Generato: `2026-10-13T21:02:09+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-13T21:01:23+00:00` (448 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.17% | 0.00% | **0.17 pp** |
| 1w | 0.06% | 0.00% | **0.06 pp** |
| 1m | -1.61% | 0.00% | **-1.61 pp** |
| 3m | 11.08% | 7.11% | **3.97 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | VIX (volatilita) | 2.49% | | Nasdaq Composite | -0.44% |
| 3 | Bitcoin | 1.02% | | S&P 500 | -0.06% |
| 4 | Ethereum | 0.97% | | GBP/USD | -0.04% |
| 5 | US 5Y Treasury Yield | 0.60% | | FTSE MIB | 0.00% |
| 6 | Dow Jones | 0.38% | | Euro Stoxx 50 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -2.49% |
| 2 | Petrolio WTI | 5.20% | | GBP/USD | -2.16% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -2.00% |
| 4 | Indice dollaro Fed (broad) | 2.99% | | Nasdaq Composite | -0.84% |
| 5 | Bitcoin | 2.00% | | US 5Y Treasury Yield | -0.79% |
| 6 | Ethereum | 1.46% | | US 10Y Treasury Yield | -0.76% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | Solana | -9.52% |
| 2 | Petrolio WTI | 15.44% | | Ethereum | -8.77% |
| 3 | Gas naturale | 10.14% | | VIX (volatilita) | -3.24% |
| 4 | US 10Y Treasury Yield | 5.86% | | Bitcoin | -3.22% |
| 5 | US 5Y Treasury Yield | 5.68% | | EUR/USD | -3.14% |
| 6 | US 30Y Treasury Yield | 4.28% | | GBP/USD | -2.05% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.104 | 5.86% | 0.00% | **5.86 pp** |
| S&P 500 vs VIX (volatilita) | 0.119 | 1.96% | -3.24% | **5.20 pp** |
| S&P 500 vs Bitcoin | 0.023 | 1.96% | -3.22% | **5.18 pp** |
| EUR/USD vs Indice dollaro DXY | 0.053 | -3.14% | 0.00% | **-3.14 pp** |
| S&P 500 vs Oro (spot) | 0.285 | 1.96% | 0.00% | **1.96 pp** |
| S&P 500 vs Nasdaq Composite | 0.947 | 1.96% | 3.47% | **-1.51 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.80 | 2026-10-09 | 0.05 |
| US 10Y Treasury Rate | 5.24 | 2026-10-09 | 0.02 |
| US 30Y Treasury Rate | 5.60 | 2026-10-09 | 0.00 |
| Spread 10Y-2Y USA | 0.44 | 2026-10-09 | -0.03 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **44.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.2100 | -3.24% | 98.01% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 107.0424 | -9.52% | 36.43% | -13.59% |
| Ethereum | 2 509.0966 | -8.77% | 24.71% | -10.76% |
| US 5Y Treasury Yield | 5.0200 | 5.68% | 18.54% | -1.96% |
| US 10Y Treasury Yield | 5.2400 | 5.86% | 16.70% | -2.70% |
| Bitcoin | 83 350.9617 | -3.22% | 16.27% | -6.86% |
| Nasdaq Composite | 27 245.9000 | 3.47% | 14.33% | -7.00% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| US 30Y Treasury Yield | 5.6000 | 4.28% | 13.45% | -1.49% |
| Dow Jones | 51 850.5500 | -1.37% | 9.86% | -6.34% |
| S&P 500 | 7 807.2400 | 1.96% | 9.73% | -3.42% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
