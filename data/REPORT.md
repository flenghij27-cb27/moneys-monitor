# Moneys Monitor - Report di mercato

Generato: `2026-11-02T00:58:33+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-02T00:58:00+00:00` (510 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.02% | 0.00% | **0.02 pp** |
| 1w | -1.39% | 0.00% | **-1.39 pp** |
| 1m | -2.76% | 0.00% | **-2.76 pp** |
| 3m | -1.85% | 0.00% | **-1.85 pp** |
| 6m | 14.68% | 14.50% | **0.18 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 6.84% | | Gas naturale | -10.97% |
| 2 | VIX (volatilita) | 1.71% | | Petrolio WTI | -4.19% |
| 3 | Ethereum | 0.61% | | US 5Y Treasury Yield | -1.44% |
| 4 | Bitcoin | 0.48% | | US 10Y Treasury Yield | -1.39% |
| 5 | EUR/USD | 0.38% | | Nasdaq Composite | -1.38% |
| 6 | GBP/USD | 0.34% | | Dow Jones | -1.09% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 7.22% | | VIX (volatilita) | -9.62% |
| 2 | Petrolio Brent | 7.15% | | Solana | -7.96% |
| 3 | Indice dollaro Fed (broad) | 1.51% | | Gas naturale | -4.83% |
| 4 | Nasdaq Composite | 0.68% | | Bitcoin | -3.58% |
| 5 | US 30Y Treasury Yield | 0.57% | | Ethereum | -3.46% |
| 6 | S&P 500 | 0.41% | | Dow Jones | -0.85% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -12.02% |
| 2 | Petrolio WTI | 25.40% | | Ethereum | -8.68% |
| 3 | VIX (volatilita) | 5.26% | | US 5Y Treasury Yield | -5.53% |
| 4 | Dow Jones | 1.66% | | Bitcoin | -5.35% |
| 5 | Gas naturale | 1.55% | | US 10Y Treasury Yield | -5.32% |
| 6 | S&P 500 | 0.78% | | US 30Y Treasury Yield | -4.83% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| S&P 500 vs Bitcoin | 0.157 | 0.78% | -5.35% | **6.13 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.008 | -5.32% | 0.00% | **-5.32 pp** |
| S&P 500 vs VIX (volatilita) | -0.417 | 0.78% | 5.26% | **-4.48 pp** |
| S&P 500 vs Nasdaq Composite | -0.010 | 0.78% | -2.29% | **3.07 pp** |
| EUR/USD vs Indice dollaro DXY | -0.139 | -1.12% | 0.00% | **-1.12 pp** |
| S&P 500 vs Oro (spot) | -0.022 | 0.78% | 0.00% | **0.78 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.61 | 2026-10-29 | -0.06 |
| US 10Y Treasury Rate | 4.98 | 2026-10-29 | -0.07 |
| US 30Y Treasury Rate | 5.32 | 2026-10-29 | -0.05 |
| Spread 10Y-2Y USA | 0.38 | 2026-10-30 | 0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **37.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.2000 | 5.26% | 117.08% | -31.22% |
| Petrolio Brent | 123.1000 | 38.92% | 115.48% | -21.50% |
| Petrolio WTI | 103.3700 | 25.40% | 76.78% | -18.71% |
| Gas naturale | 2.7600 | 1.55% | 72.11% | -18.87% |
| Ethereum | 2 269.3531 | -8.68% | 31.82% | -19.23% |
| Solana | 93.9403 | -12.02% | 30.86% | -23.21% |
| Bitcoin | 78 096.8970 | -5.35% | 24.11% | -11.41% |
| US 5Y Treasury Yield | 4.7800 | -5.53% | 17.42% | -6.09% |
| US 10Y Treasury Yield | 4.9800 | -5.32% | 17.24% | -6.59% |
| Nasdaq Composite | 26 184.7200 | -2.29% | 16.79% | -7.00% |
| US 30Y Treasury Yield | 5.3200 | -4.83% | 14.48% | -6.70% |
| USD/JPY | 156.8700 | -1.68% | 13.95% | -6.19% |
| S&P 500 | 7 743.9800 | 0.78% | 10.91% | -3.42% |
| Dow Jones | 51 770.3100 | 1.66% | 9.84% | -6.34% |
| Indice dollaro Fed (broad) | 121.3202 | n/d | 8.60% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
