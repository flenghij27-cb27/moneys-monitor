# Moneys Monitor - Report di mercato

Generato: `2026-11-06T01:43:28+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-06T01:42:53+00:00` (522 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.33% | 0.00% | **0.33 pp** |
| 1w | -1.04% | 0.00% | **-1.04 pp** |
| 1m | -3.40% | 0.00% | **-3.40 pp** |
| 3m | -2.95% | 0.00% | **-2.95 pp** |
| 6m | 11.00% | 15.30% | **-4.30 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | S&P 500 | 1.58% | | VIX (volatilita) | -20.26% |
| 2 | Nasdaq Composite | 1.44% | | Petrolio Brent | -13.05% |
| 3 | USD/JPY | 0.38% | | Gas naturale | -4.71% |
| 4 | Indice dollaro Fed (broad) | 0.28% | | Petrolio WTI | -3.61% |
| 5 | Bitcoin | 0.26% | | Dow Jones | -3.44% |
| 6 | GBP/USD | 0.17% | | US 5Y Treasury Yield | -1.05% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 3.62% | | Gas naturale | -17.30% |
| 2 | GBP/USD | 1.12% | | Petrolio Brent | -6.08% |
| 3 | Indice dollaro Fed (broad) | 1.11% | | Solana | -4.14% |
| 4 | EUR/USD | 0.84% | | US 5Y Treasury Yield | -3.30% |
| 5 | USD/JPY | 0.18% | | US 10Y Treasury Yield | -2.97% |
| 6 | FTSE MIB | 0.00% | | Nasdaq Composite | -2.80% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 20.92% | | Solana | -13.82% |
| 2 | Petrolio Brent | 20.91% | | US 10Y Treasury Yield | -7.72% |
| 3 | VIX (volatilita) | 10.66% | | Ethereum | -7.67% |
| 4 | Dow Jones | 0.67% | | US 5Y Treasury Yield | -7.31% |
| 5 | EUR/USD | 0.42% | | Bitcoin | -6.71% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -6.71% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.494 | -0.44% | 10.66% | **-11.10 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.012 | -7.72% | 0.00% | **-7.72 pp** |
| S&P 500 vs Bitcoin | 0.092 | -0.44% | -6.71% | **6.27 pp** |
| S&P 500 vs Nasdaq Composite | 0.817 | -0.44% | -5.35% | **4.91 pp** |
| S&P 500 vs Oro (spot) | -0.018 | -0.44% | 0.00% | **-0.44 pp** |
| EUR/USD vs Indice dollaro DXY | -0.128 | 0.42% | 0.00% | **0.42 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.58 | 2026-11-04 | -0.03 |
| US 10Y Treasury Rate | 4.90 | 2026-11-04 | -0.05 |
| US 30Y Treasury Rate | 5.28 | 2026-11-04 | -0.04 |
| Spread 10Y-2Y USA | 0.38 | 2026-11-05 | 0.06 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.6100 | 10.66% | 146.80% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 235.7154 | -7.67% | 45.48% | -19.43% |
| Solana | 89.8707 | -13.82% | 35.51% | -26.40% |
| Bitcoin | 76 072.1348 | -6.71% | 32.40% | -12.50% |
| Nasdaq Composite | 25 736.5100 | -5.35% | 21.53% | -8.82% |
| Dow Jones | 51 523.0600 | 0.67% | 19.24% | -6.34% |
| US 5Y Treasury Yield | 4.6900 | -7.31% | 17.32% | -7.86% |
| US 10Y Treasury Yield | 4.9000 | -7.72% | 17.06% | -7.72% |
| US 30Y Treasury Yield | 5.2800 | -6.71% | 14.58% | -6.88% |
| S&P 500 | 7 688.6200 | -0.44% | 14.23% | -3.55% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
