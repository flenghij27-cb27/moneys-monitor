# Moneys Monitor - Report di mercato

Generato: `2026-10-08T21:05:17+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-08T21:04:41+00:00` (433 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.18% | 0.00% | **-1.18 pp** |
| 1w | -1.53% | 0.00% | **-1.53 pp** |
| 1m | 2.23% | 0.00% | **2.23 pp** |
| 3m | 11.99% | 13.90% | **-1.91 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Solana | -5.49% |
| 2 | Indice dollaro Fed (broad) | 0.88% | | Gas naturale | -4.72% |
| 3 | US 30Y Treasury Yield | 0.53% | | Ethereum | -3.90% |
| 4 | VIX (volatilita) | 0.47% | | Bitcoin | -2.00% |
| 5 | USD/JPY | 0.40% | | Dow Jones | -0.66% |
| 6 | US 10Y Treasury Yield | 0.19% | | S&P 500 | -0.22% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | Solana | -8.26% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -7.97% |
| 3 | Gas naturale | 4.48% | | VIX (volatilita) | -7.71% |
| 4 | Nasdaq Composite | 2.52% | | Bitcoin | -3.58% |
| 5 | Indice dollaro Fed (broad) | 2.22% | | GBP/USD | -2.37% |
| 6 | S&P 500 | 1.96% | | USD/JPY | -1.35% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | EUR/USD | -4.00% |
| 2 | Petrolio WTI | 15.44% | | Dow Jones | -3.04% |
| 3 | Gas naturale | 10.14% | | GBP/USD | -2.02% |
| 4 | US 5Y Treasury Yield | 10.07% | | USD/JPY | -0.95% |
| 5 | US 10Y Treasury Yield | 10.00% | | VIX (volatilita) | -0.79% |
| 6 | Solana | 8.26% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.072 | 10.00% | 0.00% | **10.00 pp** |
| S&P 500 vs Bitcoin | -0.087 | 1.67% | 7.02% | **-5.35 pp** |
| EUR/USD vs Indice dollaro DXY | 0.088 | -4.00% | 0.00% | **-4.00 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 1.67% | 4.23% | **-2.56 pp** |
| S&P 500 vs VIX (volatilita) | 0.133 | 1.67% | -0.79% | **2.46 pp** |
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
| US 2Y Treasury Rate | 4.77 | 2026-10-07 | -0.02 |
| US 10Y Treasury Rate | 5.28 | 2026-10-07 | 0.01 |
| US 30Y Treasury Rate | 5.67 | 2026-10-07 | 0.03 |
| Spread 10Y-2Y USA | 0.47 | 2026-10-08 | -0.04 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **51.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 125.4400 | 40.77% | 108.07% | -21.50% |
| VIX (volatilita) | 15.0800 | -0.79% | 101.25% | -31.22% |
| Petrolio WTI | 96.2400 | 15.44% | 71.13% | -18.71% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Solana | 109.7771 | 8.26% | 43.56% | -13.59% |
| Ethereum | 2 472.8991 | 1.12% | 30.88% | -10.76% |
| Bitcoin | 81 717.8844 | 7.02% | 29.64% | -6.86% |
| US 5Y Treasury Yield | 5.0300 | 10.07% | 20.56% | -1.65% |
| US 10Y Treasury Yield | 5.2800 | 10.00% | 17.58% | -2.70% |
| Nasdaq Composite | 27 538.6900 | 4.23% | 13.93% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6700 | 8.00% | 13.45% | -1.49% |
| S&P 500 | 7 801.7700 | 1.67% | 10.27% | -3.42% |
| Dow Jones | 51 179.8700 | -3.04% | 10.10% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
