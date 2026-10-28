# Moneys Monitor - Report di mercato

Generato: `2026-10-28T12:17:08+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-28T12:16:33+00:00` (496 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.26% | 0.00% | **0.26 pp** |
| 1w | -0.23% | 0.00% | **-0.23 pp** |
| 1m | -2.67% | 0.00% | **-2.67 pp** |
| 3m | 0.59% | -0.53% | **1.12 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.87% | | Petrolio Brent | -8.95% |
| 2 | Nasdaq Composite | 1.18% | | VIX (volatilita) | -5.45% |
| 3 | Solana | 0.86% | | Gas naturale | -3.73% |
| 4 | S&P 500 | 0.60% | | USD/JPY | -0.72% |
| 5 | US 5Y Treasury Yield | 0.41% | | US 30Y Treasury Yield | -0.38% |
| 6 | GBP/USD | 0.34% | | EUR/USD | -0.34% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 4.38% | | Petrolio Brent | -11.91% |
| 2 | Indice dollaro Fed (broad) | 1.51% | | US 30Y Treasury Yield | -3.10% |
| 3 | Petrolio WTI | 0.81% | | US 10Y Treasury Yield | -2.91% |
| 4 | S&P 500 | 0.41% | | US 5Y Treasury Yield | -2.02% |
| 5 | Nasdaq Composite | 0.20% | | Ethereum | -1.68% |
| 6 | GBP/USD | 0.02% | | Solana | -0.90% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 32.93% | | Solana | -12.28% |
| 2 | Petrolio Brent | 32.51% | | Ethereum | -8.91% |
| 3 | VIX (volatilita) | 29.42% | | US 5Y Treasury Yield | -3.78% |
| 4 | Gas naturale | 13.51% | | US 10Y Treasury Yield | -3.47% |
| 5 | Dow Jones | 1.74% | | Bitcoin | -3.03% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -2.93% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.091 | -0.27% | 29.42% | **-29.69 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.054 | -3.47% | 0.00% | **-3.47 pp** |
| S&P 500 vs Bitcoin | 0.203 | -0.27% | -3.03% | **2.76 pp** |
| EUR/USD vs Indice dollaro DXY | 0.074 | -2.00% | 0.00% | **-2.00 pp** |
| S&P 500 vs Nasdaq Composite | 0.854 | -0.27% | -2.18% | **1.91 pp** |
| Petrolio WTI vs Petrolio Brent | 0.819 | 32.93% | 32.51% | **0.42 pp** |
| S&P 500 vs Oro (spot) | 0.183 | -0.27% | 0.00% | **-0.27 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.68 | 2026-10-26 | -0.01 |
| US 10Y Treasury Rate | 5.00 | 2026-10-26 | 0.00 |
| US 30Y Treasury Rate | 5.31 | 2026-10-26 | -0.02 |
| Spread 10Y-2Y USA | 0.29 | 2026-10-27 | -0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **31.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 18.3900 | 29.42% | 114.47% | -31.22% |
| Petrolio Brent | 115.2200 | 32.51% | 114.17% | -21.50% |
| Petrolio WTI | 107.8900 | 32.93% | 74.25% | -18.71% |
| Gas naturale | 3.1000 | 13.51% | 58.95% | -18.87% |
| Ethereum | 2 343.9428 | -8.91% | 30.65% | -16.88% |
| Solana | 101.8865 | -12.28% | 28.00% | -17.96% |
| Bitcoin | 80 860.4479 | -3.03% | 21.66% | -8.03% |
| US 5Y Treasury Yield | 4.8400 | -3.78% | 18.10% | -6.09% |
| US 10Y Treasury Yield | 5.0000 | -3.47% | 17.29% | -6.59% |
| Nasdaq Composite | 26 477.8100 | -2.18% | 16.12% | -7.00% |
| US 30Y Treasury Yield | 5.3100 | -2.93% | 15.02% | -6.70% |
| USD/JPY | 156.8700 | -1.68% | 13.95% | -6.19% |
| S&P 500 | 7 722.6000 | -0.27% | 10.90% | -3.42% |
| Dow Jones | 52 377.5700 | 1.74% | 9.54% | -6.34% |
| Indice dollaro Fed (broad) | 121.3202 | n/d | 8.60% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
