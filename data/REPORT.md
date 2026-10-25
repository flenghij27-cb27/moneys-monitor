# Moneys Monitor - Report di mercato

Generato: `2026-10-25T23:27:36+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-25T23:27:01+00:00` (489 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.10% | 0.00% | **-0.10 pp** |
| 1w | -1.31% | 0.00% | **-1.31 pp** |
| 1m | -3.99% | 0.00% | **-3.99 pp** |
| 3m | 1.77% | -0.57% | **2.34 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 14.09% | | Petrolio Brent | -8.95% |
| 2 | Petrolio WTI | 5.87% | | Gas naturale | -3.73% |
| 3 | GBP/USD | 0.76% | | US 5Y Treasury Yield | -3.43% |
| 4 | S&P 500 | 0.58% | | US 10Y Treasury Yield | -3.31% |
| 5 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -2.40% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -1.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.61% | | Petrolio Brent | -11.91% |
| 2 | Gas naturale | 4.38% | | Ethereum | -4.20% |
| 3 | USD/JPY | 2.79% | | Solana | -3.91% |
| 4 | Indice dollaro Fed (broad) | 2.70% | | Nasdaq Composite | -2.84% |
| 5 | Petrolio WTI | 0.81% | | US 10Y Treasury Yield | -2.75% |
| 6 | S&P 500 | 0.50% | | US 5Y Treasury Yield | -2.65% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 32.93% | | Solana | -16.61% |
| 2 | Petrolio Brent | 32.51% | | Ethereum | -13.62% |
| 3 | VIX (volatilita) | 28.49% | | Bitcoin | -5.95% |
| 4 | Gas naturale | 13.51% | | Nasdaq Composite | -3.64% |
| 5 | Dow Jones | 1.68% | | EUR/USD | -1.53% |
| 6 | FTSE MIB | 0.00% | | GBP/USD | -1.22% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.116 | -0.10% | 28.49% | **-28.59 pp** |
| S&P 500 vs Bitcoin | 0.196 | -0.10% | -5.95% | **5.85 pp** |
| S&P 500 vs Nasdaq Composite | 0.004 | -0.10% | -3.64% | **3.54 pp** |
| EUR/USD vs Indice dollaro DXY | 0.004 | -1.53% | 0.00% | **-1.53 pp** |
| Petrolio WTI vs Petrolio Brent | 0.819 | 32.93% | 32.51% | **0.42 pp** |
| S&P 500 vs Oro (spot) | 0.190 | -0.10% | 0.00% | **-0.10 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.044 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.65 | 2026-10-22 | -0.16 |
| US 10Y Treasury Rate | 4.96 | 2026-10-22 | -0.17 |
| US 30Y Treasury Rate | 5.29 | 2026-10-22 | -0.13 |
| Spread 10Y-2Y USA | 0.31 | 2026-10-23 | 0.00 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **31.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.0300 | 28.49% | 121.65% | -31.22% |
| Petrolio Brent | 115.2200 | 32.51% | 114.17% | -21.50% |
| Petrolio WTI | 107.8900 | 32.93% | 74.25% | -18.71% |
| Gas naturale | 3.1000 | 13.51% | 58.95% | -18.87% |
| Ethereum | 2 332.0189 | -13.62% | 34.98% | -15.84% |
| Solana | 101.3781 | -16.61% | 34.50% | -16.97% |
| Bitcoin | 80 189.1673 | -5.95% | 23.76% | -7.53% |
| US 5Y Treasury Yield | 4.7800 | -1.04% | 18.19% | -6.09% |
| US 10Y Treasury Yield | 4.9600 | 0.00% | 17.81% | -6.59% |
| US 30Y Treasury Yield | 5.2900 | 0.00% | 15.64% | -6.70% |
| Nasdaq Composite | 25 955.3400 | -3.64% | 15.45% | -7.00% |
| USD/JPY | 158.0000 | -0.88% | 13.75% | -6.19% |
| Dow Jones | 52 215.1600 | 1.68% | 9.95% | -6.34% |
| S&P 500 | 7 757.1700 | -0.10% | 8.93% | -3.42% |
| Indice dollaro Fed (broad) | 121.4048 | n/d | 8.89% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
