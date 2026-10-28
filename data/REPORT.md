# Moneys Monitor - Report di mercato

Generato: `2026-10-28T20:50:25+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-28T20:49:55+00:00` (497 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.32% | 0.00% | **0.32 pp** |
| 1w | -0.16% | 0.00% | **-0.16 pp** |
| 1m | -2.61% | 0.00% | **-2.61 pp** |
| 3m | 0.65% | -0.53% | **1.18 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 6.84% | | Gas naturale | -10.97% |
| 2 | Nasdaq Composite | 1.18% | | VIX (volatilita) | -4.73% |
| 3 | Solana | 1.03% | | Petrolio WTI | -4.19% |
| 4 | S&P 500 | 0.60% | | USD/JPY | -0.72% |
| 5 | Bitcoin | 0.42% | | US 5Y Treasury Yield | -0.41% |
| 6 | GBP/USD | 0.34% | | US 10Y Treasury Yield | -0.20% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 7.22% | | Gas naturale | -4.83% |
| 2 | Petrolio Brent | 7.15% | | US 10Y Treasury Yield | -2.54% |
| 3 | Indice dollaro Fed (broad) | 1.51% | | US 5Y Treasury Yield | -2.43% |
| 4 | VIX (volatilita) | 1.21% | | US 30Y Treasury Yield | -2.21% |
| 5 | S&P 500 | 0.41% | | Ethereum | -1.40% |
| 6 | Nasdaq Composite | 0.20% | | EUR/USD | -0.90% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -12.13% |
| 2 | Petrolio WTI | 25.40% | | Ethereum | -8.66% |
| 3 | VIX (volatilita) | 9.02% | | US 10Y Treasury Yield | -3.48% |
| 4 | Dow Jones | 1.74% | | US 30Y Treasury Yield | -3.46% |
| 5 | Gas naturale | 1.55% | | US 5Y Treasury Yield | -3.21% |
| 6 | FTSE MIB | 0.00% | | Bitcoin | -2.87% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| S&P 500 vs VIX (volatilita) | 0.083 | -0.27% | 9.02% | **-9.29 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.043 | -3.48% | 0.00% | **-3.48 pp** |
| S&P 500 vs Bitcoin | 0.203 | -0.27% | -2.87% | **2.60 pp** |
| EUR/USD vs Indice dollaro DXY | 0.002 | -1.96% | 0.00% | **-1.96 pp** |
| S&P 500 vs Nasdaq Composite | 0.854 | -0.27% | -2.18% | **1.91 pp** |
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
| US 2Y Treasury Rate | 4.70 | 2026-10-27 | 0.02 |
| US 10Y Treasury Rate | 4.99 | 2026-10-27 | -0.01 |
| US 30Y Treasury Rate | 5.30 | 2026-10-27 | -0.01 |
| Spread 10Y-2Y USA | 0.29 | 2026-10-27 | -0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **31.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.5200 | 9.02% | 116.17% | -31.22% |
| Petrolio Brent | 123.1000 | 38.92% | 115.48% | -21.50% |
| Petrolio WTI | 103.3700 | 25.40% | 76.78% | -18.71% |
| Gas naturale | 2.7600 | 1.55% | 72.11% | -18.87% |
| Ethereum | 2 350.6009 | -8.66% | 30.66% | -16.88% |
| Solana | 102.0608 | -12.13% | 28.11% | -17.96% |
| Bitcoin | 80 996.2324 | -2.87% | 21.70% | -8.03% |
| US 5Y Treasury Yield | 4.8200 | -3.21% | 16.90% | -6.09% |
| US 10Y Treasury Yield | 4.9900 | -3.48% | 16.34% | -6.59% |
| Nasdaq Composite | 26 477.8100 | -2.18% | 16.12% | -7.00% |
| US 30Y Treasury Yield | 5.3000 | -3.46% | 14.03% | -6.70% |
| USD/JPY | 156.8700 | -1.68% | 13.95% | -6.19% |
| S&P 500 | 7 722.6000 | -0.27% | 10.90% | -3.42% |
| Dow Jones | 52 377.5700 | 1.74% | 9.54% | -6.34% |
| Indice dollaro Fed (broad) | 121.3202 | n/d | 8.60% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
