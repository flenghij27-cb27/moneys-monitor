# Moneys Monitor - Report di mercato

Generato: `2026-10-01T20:51:30+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-01T20:50:56+00:00` (411 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.18% | 0.00% | **0.18 pp** |
| 1w | -0.33% | 0.00% | **-0.33 pp** |
| 1m | 4.16% | 0.00% | **4.16 pp** |
| 3m | 15.84% | 17.81% | **-1.97 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | GBP/USD | -0.91% |
| 2 | VIX (volatilita) | 1.87% | | Dow Jones | -0.86% |
| 3 | Bitcoin | 1.15% | | Petrolio Brent | -0.81% |
| 4 | US 30Y Treasury Yield | 0.89% | | EUR/USD | -0.50% |
| 5 | Indice dollaro Fed (broad) | 0.68% | | Petrolio WTI | -0.26% |
| 6 | Ethereum | 0.66% | | S&P 500 | -0.25% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | GBP/USD | -2.85% |
| 2 | Petrolio WTI | 16.80% | | Solana | -2.71% |
| 3 | Gas naturale | 13.86% | | USD/JPY | -1.28% |
| 4 | VIX (volatilita) | 10.33% | | Dow Jones | -1.18% |
| 5 | US 30Y Treasury Yield | 4.44% | | S&P 500 | -0.71% |
| 6 | US 10Y Treasury Yield | 3.52% | | EUR/USD | -0.61% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -4.29% |
| 2 | Solana | 19.29% | | EUR/USD | -2.42% |
| 3 | Petrolio WTI | 16.87% | | GBP/USD | -1.82% |
| 4 | Gas naturale | 14.55% | | S&P 500 | -0.45% |
| 5 | US 5Y Treasury Yield | 13.36% | | USD/JPY | -0.40% |
| 6 | US 10Y Treasury Yield | 11.37% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.032 | 11.37% | 0.00% | **11.37 pp** |
| S&P 500 vs Bitcoin | 0.006 | -0.45% | 10.33% | **-10.78 pp** |
| S&P 500 vs VIX (volatilita) | 0.156 | -0.45% | 7.43% | **-7.88 pp** |
| EUR/USD vs Indice dollaro DXY | 0.015 | -2.42% | 0.00% | **-2.42 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | -0.45% | 1.86% | **-2.31 pp** |
| S&P 500 vs Oro (spot) | 0.068 | -0.45% | 0.00% | **-0.45 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.88 | 2026-09-30 | -0.01 |
| US 10Y Treasury Rate | 5.29 | 2026-09-30 | 0.03 |
| US 30Y Treasury Rate | 5.64 | 2026-09-30 | 0.05 |
| Spread 10Y-2Y USA | 0.41 | 2026-09-30 | 0.04 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **41.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.3400 | 7.43% | 108.75% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 118.0319 | 19.29% | 59.30% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Ethereum | 2 696.2739 | 10.53% | 37.92% | -5.78% |
| Bitcoin | 84 577.4278 | 10.33% | 36.75% | -6.86% |
| US 5Y Treasury Yield | 5.0900 | 13.36% | 18.98% | -1.65% |
| US 10Y Treasury Yield | 5.2900 | 11.37% | 16.57% | -2.70% |
| Nasdaq Composite | 26 861.0600 | 1.86% | 14.26% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.6400 | 7.43% | 13.29% | -1.49% |
| Dow Jones | 50 906.0500 | -4.29% | 11.69% | -6.34% |
| S&P 500 | 7 651.5400 | -0.45% | 10.82% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
