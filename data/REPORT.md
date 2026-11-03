# Moneys Monitor - Report di mercato

Generato: `2026-11-03T03:00:43+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-03T02:59:46+00:00` (513 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.35% | 0.00% | **-0.35 pp** |
| 1w | -0.99% | 0.00% | **-0.99 pp** |
| 1m | -3.60% | 0.00% | **-3.60 pp** |
| 3m | -1.81% | 0.00% | **-1.81 pp** |
| 6m | 14.16% | 14.50% | **-0.34 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 12.91% | | Gas naturale | -10.97% |
| 2 | Petrolio Brent | 6.84% | | Petrolio WTI | -4.19% |
| 3 | Dow Jones | 0.41% | | S&P 500 | -2.12% |
| 4 | EUR/USD | 0.39% | | US 5Y Treasury Yield | -1.46% |
| 5 | USD/JPY | 0.38% | | Nasdaq Composite | -1.38% |
| 6 | Indice dollaro Fed (broad) | 0.28% | | US 10Y Treasury Yield | -0.80% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 7.22% | | Solana | -4.97% |
| 2 | Petrolio Brent | 7.15% | | Gas naturale | -4.83% |
| 3 | GBP/USD | 1.12% | | Bitcoin | -2.95% |
| 4 | Indice dollaro Fed (broad) | 1.11% | | S&P 500 | -2.28% |
| 5 | Nasdaq Composite | 0.68% | | US 5Y Treasury Yield | -2.28% |
| 6 | EUR/USD | 0.25% | | US 10Y Treasury Yield | -1.20% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -14.25% |
| 2 | Petrolio WTI | 25.40% | | Ethereum | -10.30% |
| 3 | VIX (volatilita) | 18.49% | | Bitcoin | -8.02% |
| 4 | Dow Jones | 1.58% | | US 5Y Treasury Yield | -7.47% |
| 5 | Gas naturale | 1.55% | | US 10Y Treasury Yield | -6.62% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -5.85% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.452 | -1.18% | 18.49% | **-19.67 pp** |
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| S&P 500 vs Bitcoin | 0.150 | -1.18% | -8.02% | **6.84 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.010 | -6.62% | 0.00% | **-6.62 pp** |
| S&P 500 vs Oro (spot) | -0.015 | -1.18% | 0.00% | **-1.18 pp** |
| S&P 500 vs Nasdaq Composite | 0.847 | -1.18% | -2.29% | **1.11 pp** |
| EUR/USD vs Indice dollaro DXY | -0.136 | -0.08% | 0.00% | **-0.08 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.56 | 2026-10-30 | -0.05 |
| US 10Y Treasury Rate | 4.94 | 2026-10-30 | -0.04 |
| US 30Y Treasury Rate | 5.31 | 2026-10-30 | -0.01 |
| Spread 10Y-2Y USA | 0.32 | 2026-11-02 | -0.06 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **38.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.4200 | 18.49% | 121.82% | -31.22% |
| Petrolio Brent | 123.1000 | 38.92% | 115.48% | -21.50% |
| Petrolio WTI | 103.3700 | 25.40% | 76.78% | -18.71% |
| Gas naturale | 2.7600 | 1.55% | 72.11% | -18.87% |
| Solana | 91.7887 | -14.25% | 30.45% | -24.92% |
| Ethereum | 2 250.5433 | -10.30% | 29.45% | -19.23% |
| Bitcoin | 76 666.3329 | -8.02% | 23.29% | -11.59% |
| US 5Y Treasury Yield | 4.7100 | -7.47% | 17.32% | -7.47% |
| US 10Y Treasury Yield | 4.9400 | -6.62% | 17.18% | -6.97% |
| Nasdaq Composite | 26 184.7200 | -2.29% | 16.79% | -7.00% |
| US 30Y Treasury Yield | 5.3100 | -5.85% | 14.46% | -6.70% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| S&P 500 | 7 580.0700 | -1.18% | 13.33% | -3.42% |
| Dow Jones | 51 983.9800 | 1.58% | 9.91% | -6.34% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
