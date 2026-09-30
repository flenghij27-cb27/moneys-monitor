# Moneys Monitor - Report di mercato

Generato: `2026-09-30T20:37:14+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-30T20:36:40+00:00` (408 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.18% | 0.00% | **-0.18 pp** |
| 1w | -0.69% | 0.00% | **-0.69 pp** |
| 1m | 3.33% | 0.00% | **3.33 pp** |
| 3m | 14.03% | 15.71% | **-1.68 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | Solana | -0.99% |
| 2 | Indice dollaro Fed (broad) | 0.68% | | GBP/USD | -0.91% |
| 3 | US 30Y Treasury Yield | 0.54% | | Petrolio Brent | -0.81% |
| 4 | US 10Y Treasury Yield | 0.38% | | Ethereum | -0.51% |
| 5 | USD/JPY | 0.20% | | Dow Jones | -0.26% |
| 6 | FTSE MIB | 0.00% | | Petrolio WTI | -0.26% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | Solana | -3.03% |
| 2 | Petrolio WTI | 16.80% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 13.86% | | Nasdaq Composite | -1.64% |
| 4 | US 10Y Treasury Yield | 6.05% | | USD/JPY | -1.28% |
| 5 | US 30Y Treasury Yield | 5.67% | | S&P 500 | -1.21% |
| 6 | US 5Y Treasury Yield | 4.76% | | Dow Jones | -0.99% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -4.13% |
| 2 | Petrolio WTI | 16.87% | | EUR/USD | -2.03% |
| 3 | Solana | 16.32% | | GBP/USD | -1.82% |
| 4 | Gas naturale | 14.55% | | S&P 500 | -0.53% |
| 5 | US 5Y Treasury Yield | 12.95% | | USD/JPY | -0.40% |
| 6 | US 10Y Treasury Yield | 11.21% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.031 | 11.21% | 0.00% | **11.21 pp** |
| S&P 500 vs Bitcoin | 0.009 | -0.53% | 7.06% | **-7.59 pp** |
| S&P 500 vs VIX (volatilita) | 0.158 | -0.53% | 2.56% | **-3.09 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | -0.53% | 1.50% | **-2.03 pp** |
| EUR/USD vs Indice dollaro DXY | 0.018 | -2.03% | 0.00% | **-2.03 pp** |
| S&P 500 vs Oro (spot) | 0.067 | -0.53% | 0.00% | **-0.53 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.89 | 2026-09-29 | -0.03 |
| US 10Y Treasury Rate | 5.26 | 2026-09-29 | 0.02 |
| US 30Y Treasury Rate | 5.59 | 2026-09-29 | 0.03 |
| Spread 10Y-2Y USA | 0.37 | 2026-09-29 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **37.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.0400 | 2.56% | 110.34% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 117.9813 | 16.32% | 59.87% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Ethereum | 2 678.7220 | 8.90% | 39.06% | -5.78% |
| Bitcoin | 83 618.4955 | 7.06% | 36.68% | -6.86% |
| US 5Y Treasury Yield | 5.0600 | 12.95% | 19.18% | -1.65% |
| US 10Y Treasury Yield | 5.2600 | 11.21% | 16.61% | -2.70% |
| Nasdaq Composite | 26 797.5400 | 1.50% | 14.85% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.5900 | 7.09% | 13.14% | -1.49% |
| Dow Jones | 51 349.9200 | -4.13% | 11.63% | -5.52% |
| S&P 500 | 7 670.8400 | -0.53% | 11.09% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
