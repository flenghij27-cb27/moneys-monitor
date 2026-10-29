# Moneys Monitor - Report di mercato

Generato: `2026-10-29T12:27:12+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-29T12:26:38+00:00` (499 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.36% | 0.00% | **-0.36 pp** |
| 1w | -0.32% | 0.00% | **-0.32 pp** |
| 1m | -1.71% | 0.00% | **-1.71 pp** |
| 3m | -0.26% | 0.00% | **-0.26 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 6.84% | | Gas naturale | -10.97% |
| 2 | GBP/USD | 0.34% | | VIX (volatilita) | -4.73% |
| 3 | S&P 500 | 0.28% | | Petrolio WTI | -4.19% |
| 4 | Nasdaq Composite | 0.27% | | Solana | -1.74% |
| 5 | Dow Jones | 0.19% | | Ethereum | -1.23% |
| 6 | FTSE MIB | 0.00% | | Bitcoin | -1.22% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 7.22% | | Gas naturale | -4.83% |
| 2 | Petrolio Brent | 7.15% | | US 10Y Treasury Yield | -2.54% |
| 3 | Indice dollaro Fed (broad) | 1.51% | | US 5Y Treasury Yield | -2.43% |
| 4 | VIX (volatilita) | 1.21% | | US 30Y Treasury Yield | -2.21% |
| 5 | S&P 500 | 0.41% | | Solana | -1.45% |
| 6 | GBP/USD | 0.02% | | Ethereum | -0.93% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -8.65% |
| 2 | Petrolio WTI | 25.40% | | Ethereum | -6.11% |
| 3 | VIX (volatilita) | 9.02% | | US 10Y Treasury Yield | -3.48% |
| 4 | Dow Jones | 2.19% | | US 30Y Treasury Yield | -3.46% |
| 5 | Gas naturale | 1.55% | | US 5Y Treasury Yield | -3.21% |
| 6 | S&P 500 | 0.78% | | Bitcoin | -2.09% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| S&P 500 vs VIX (volatilita) | -0.094 | 0.78% | 9.02% | **-8.24 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.054 | -3.48% | 0.00% | **-3.48 pp** |
| S&P 500 vs Bitcoin | 0.200 | 0.78% | -2.09% | **2.87 pp** |
| EUR/USD vs Indice dollaro DXY | 0.074 | -1.96% | 0.00% | **-1.96 pp** |
| S&P 500 vs Nasdaq Composite | 0.854 | 0.78% | -1.01% | **1.79 pp** |
| S&P 500 vs Oro (spot) | 0.182 | 0.78% | 0.00% | **0.78 pp** |
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
| Spread 10Y-2Y USA | 0.38 | 2026-10-28 | 0.09 |
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
| Ethereum | 2 321.7957 | -6.11% | 30.82% | -16.88% |
| Solana | 100.2855 | -8.65% | 28.47% | -17.96% |
| Bitcoin | 80 010.8693 | -2.09% | 21.89% | -8.03% |
| US 5Y Treasury Yield | 4.8200 | -3.21% | 16.90% | -6.09% |
| US 10Y Treasury Yield | 4.9900 | -3.48% | 16.34% | -6.59% |
| Nasdaq Composite | 26 549.8500 | -1.01% | 16.16% | -7.00% |
| US 30Y Treasury Yield | 5.3000 | -3.46% | 14.03% | -6.70% |
| USD/JPY | 156.8700 | -1.68% | 13.95% | -6.19% |
| S&P 500 | 7 743.9800 | 0.78% | 10.91% | -3.42% |
| Dow Jones | 52 475.1000 | 2.19% | 8.83% | -6.34% |
| Indice dollaro Fed (broad) | 121.3202 | n/d | 8.60% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
