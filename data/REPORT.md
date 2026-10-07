# Moneys Monitor - Report di mercato

Generato: `2026-10-07T21:03:50+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-07T21:03:18+00:00` (430 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.02% | 0.00% | **-1.02 pp** |
| 1w | -0.13% | 0.00% | **-0.13 pp** |
| 1m | 3.93% | 0.00% | **3.93 pp** |
| 3m | 14.39% | 15.52% | **-1.13 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 10.07% | | Gas naturale | -4.72% |
| 2 | Indice dollaro Fed (broad) | 0.88% | | Ethereum | -4.61% |
| 3 | S&P 500 | 0.58% | | Solana | -4.01% |
| 4 | Dow Jones | 0.49% | | VIX (volatilita) | -3.29% |
| 5 | Nasdaq Composite | 0.45% | | Bitcoin | -2.63% |
| 6 | USD/JPY | 0.40% | | EUR/USD | -0.82% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.64% | | VIX (volatilita) | -6.42% |
| 2 | Petrolio WTI | 5.20% | | Ethereum | -3.52% |
| 3 | Gas naturale | 4.48% | | GBP/USD | -2.37% |
| 4 | Nasdaq Composite | 2.99% | | EUR/USD | -1.57% |
| 5 | Indice dollaro Fed (broad) | 2.22% | | Solana | -1.56% |
| 6 | S&P 500 | 1.93% | | USD/JPY | -1.35% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 40.77% | | VIX (volatilita) | -8.14% |
| 2 | Solana | 17.79% | | EUR/USD | -3.76% |
| 3 | Petrolio WTI | 15.44% | | Dow Jones | -3.54% |
| 4 | US 5Y Treasury Yield | 10.79% | | GBP/USD | -2.02% |
| 5 | US 10Y Treasury Yield | 10.25% | | USD/JPY | -0.95% |
| 6 | Gas naturale | 10.14% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.918 | 15.44% | 40.77% | **-25.33 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.073 | 10.25% | 0.00% | **10.25 pp** |
| S&P 500 vs VIX (volatilita) | 0.133 | 1.30% | -8.14% | **9.44 pp** |
| S&P 500 vs Bitcoin | -0.094 | 1.30% | 9.56% | **-8.26 pp** |
| EUR/USD vs Indice dollaro DXY | 0.087 | -3.76% | 0.00% | **-3.76 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 1.30% | 4.12% | **-2.82 pp** |
| S&P 500 vs Oro (spot) | -0.160 | 1.30% | 0.00% | **1.30 pp** |
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
| Solana | 116.1522 | 17.79% | 55.99% | -13.59% |
| Gas naturale | 3.0300 | 10.14% | 54.11% | -18.87% |
| Ethereum | 2 573.3307 | 6.49% | 37.17% | -7.13% |
| Bitcoin | 83 389.1147 | 9.56% | 35.52% | -6.86% |
| US 5Y Treasury Yield | 5.0300 | 10.79% | 20.54% | -1.65% |
| US 10Y Treasury Yield | 5.2700 | 10.25% | 17.56% | -2.70% |
| Nasdaq Composite | 27 599.8900 | 4.12% | 14.18% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6400 | 7.63% | 13.46% | -1.49% |
| S&P 500 | 7 818.9300 | 1.30% | 10.42% | -3.42% |
| Dow Jones | 51 521.2800 | -3.54% | 10.18% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
