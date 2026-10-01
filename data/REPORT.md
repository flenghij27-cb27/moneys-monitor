# Moneys Monitor - Report di mercato

Generato: `2026-10-01T12:37:51+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-01T12:37:15+00:00` (410 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.11% | 0.00% | **0.11 pp** |
| 1w | -0.41% | 0.00% | **-0.41 pp** |
| 1m | 4.07% | 0.00% | **4.07 pp** |
| 3m | 15.74% | 17.81% | **-2.07 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | GBP/USD | -0.91% |
| 2 | Ethereum | 0.98% | | Dow Jones | -0.86% |
| 3 | Indice dollaro Fed (broad) | 0.68% | | Petrolio Brent | -0.81% |
| 4 | US 30Y Treasury Yield | 0.54% | | Petrolio WTI | -0.26% |
| 5 | US 10Y Treasury Yield | 0.38% | | S&P 500 | -0.25% |
| 6 | Bitcoin | 0.33% | | Solana | -0.25% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | Solana | -2.99% |
| 2 | Petrolio WTI | 16.80% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 13.86% | | USD/JPY | -1.28% |
| 4 | US 10Y Treasury Yield | 6.05% | | Dow Jones | -1.18% |
| 5 | US 30Y Treasury Yield | 5.67% | | S&P 500 | -0.71% |
| 6 | US 5Y Treasury Yield | 4.76% | | Bitcoin | -0.53% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -4.29% |
| 2 | Solana | 18.94% | | EUR/USD | -2.03% |
| 3 | Petrolio WTI | 16.87% | | GBP/USD | -1.82% |
| 4 | Gas naturale | 14.55% | | S&P 500 | -0.45% |
| 5 | US 5Y Treasury Yield | 12.95% | | USD/JPY | -0.40% |
| 6 | US 10Y Treasury Yield | 11.21% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.100 | 11.21% | 0.00% | **11.21 pp** |
| S&P 500 vs Bitcoin | 0.009 | -0.45% | 9.44% | **-9.89 pp** |
| S&P 500 vs VIX (volatilita) | -0.041 | -0.45% | 2.56% | **-3.01 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | -0.45% | 1.86% | **-2.31 pp** |
| EUR/USD vs Indice dollaro DXY | 0.021 | -2.03% | 0.00% | **-2.03 pp** |
| S&P 500 vs Oro (spot) | 0.068 | -0.45% | 0.00% | **-0.45 pp** |
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
| Spread 10Y-2Y USA | 0.41 | 2026-09-30 | 0.04 |
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
| Solana | 117.6921 | 18.94% | 59.35% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Ethereum | 2 705.1010 | 10.89% | 37.97% | -5.78% |
| Bitcoin | 83 896.4672 | 9.44% | 36.67% | -6.86% |
| US 5Y Treasury Yield | 5.0600 | 12.95% | 19.18% | -1.65% |
| US 10Y Treasury Yield | 5.2600 | 11.21% | 16.61% | -2.70% |
| Nasdaq Composite | 26 861.0600 | 1.86% | 14.26% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.5900 | 7.09% | 13.14% | -1.49% |
| Dow Jones | 50 906.0500 | -4.29% | 11.69% | -6.34% |
| S&P 500 | 7 651.5400 | -0.45% | 10.82% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
