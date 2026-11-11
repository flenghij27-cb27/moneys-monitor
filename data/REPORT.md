# Moneys Monitor - Report di mercato

Generato: `2026-11-11T13:43:12+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-11T13:42:39+00:00` (538 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.06% | 0.00% | **-0.06 pp** |
| 1w | -1.87% | 0.00% | **-1.87 pp** |
| 1m | -6.52% | 0.00% | **-6.52 pp** |
| 3m | -4.87% | 0.00% | **-4.87 pp** |
| 6m | 4.10% | 10.40% | **-6.30 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 1.01% | | VIX (volatilita) | -22.31% |
| 2 | US 5Y Treasury Yield | 0.65% | | Petrolio Brent | -13.05% |
| 3 | USD/JPY | 0.48% | | Gas naturale | -4.71% |
| 4 | US 10Y Treasury Yield | 0.41% | | Petrolio WTI | -3.61% |
| 5 | EUR/USD | 0.19% | | Nasdaq Composite | -0.74% |
| 6 | Indice dollaro Fed (broad) | 0.18% | | S&P 500 | -0.38% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 3.62% | | Gas naturale | -17.30% |
| 2 | GBP/USD | 1.04% | | Ethereum | -8.01% |
| 3 | Dow Jones | 0.86% | | Solana | -6.46% |
| 4 | Indice dollaro Fed (broad) | 0.41% | | Petrolio Brent | -6.08% |
| 5 | EUR/USD | 0.31% | | VIX (volatilita) | -5.82% |
| 6 | USD/JPY | 0.27% | | Bitcoin | -2.79% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 34.23% | | Solana | -22.38% |
| 2 | Petrolio WTI | 20.92% | | Ethereum | -18.46% |
| 3 | Petrolio Brent | 20.91% | | Bitcoin | -12.89% |
| 4 | Dow Jones | 0.74% | | Nasdaq Composite | -7.82% |
| 5 | EUR/USD | 0.30% | | US 10Y Treasury Yield | -6.51% |
| 6 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -6.41% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.640 | -3.60% | 34.23% | **-37.83 pp** |
| S&P 500 vs Bitcoin | 0.012 | -3.60% | -12.89% | **9.29 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.086 | -6.51% | 0.00% | **-6.51 pp** |
| S&P 500 vs Nasdaq Composite | 0.019 | -3.60% | -7.82% | **4.22 pp** |
| S&P 500 vs Oro (spot) | 0.039 | -3.60% | 0.00% | **-3.60 pp** |
| EUR/USD vs Indice dollaro DXY | -0.004 | 0.30% | 0.00% | **0.30 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.56 | 2026-11-09 | 0.05 |
| US 10Y Treasury Rate | 4.88 | 2026-11-09 | 0.02 |
| US 30Y Treasury Rate | 5.26 | 2026-11-09 | 0.00 |
| Spread 10Y-2Y USA | 0.25 | 2026-11-10 | -0.07 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.9200 | 34.23% | 302.41% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 050.2570 | -18.46% | 42.76% | -26.01% |
| Solana | 84.1668 | -22.38% | 33.01% | -31.76% |
| Nasdaq Composite | 25 065.8700 | -7.82% | 30.68% | -11.90% |
| Bitcoin | 73 701.9918 | -12.89% | 27.61% | -15.01% |
| S&P 500 | 7 520.9300 | -3.60% | 23.18% | -5.95% |
| Dow Jones | 52 231.8900 | 0.74% | 20.56% | -6.34% |
| US 5Y Treasury Yield | 4.6700 | -6.41% | 19.14% | -9.82% |
| US 10Y Treasury Yield | 4.8800 | -6.51% | 17.24% | -8.85% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| US 30Y Treasury Yield | 5.2600 | -6.07% | 14.01% | -7.41% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
