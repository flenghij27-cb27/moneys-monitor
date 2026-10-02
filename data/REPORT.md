# Moneys Monitor - Report di mercato

Generato: `2026-10-02T01:02:00+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-02T01:01:22+00:00` (412 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.17% | 0.00% | **0.17 pp** |
| 1w | -0.23% | 0.00% | **-0.23 pp** |
| 1m | 3.61% | 0.00% | **3.61 pp** |
| 3m | 17.02% | 16.04% | **0.99 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | GBP/USD | -0.91% |
| 2 | VIX (volatilita) | 1.87% | | Petrolio Brent | -0.81% |
| 3 | US 30Y Treasury Yield | 0.89% | | EUR/USD | -0.50% |
| 4 | Solana | 0.69% | | Petrolio WTI | -0.26% |
| 5 | Indice dollaro Fed (broad) | 0.68% | | FTSE MIB | 0.00% |
| 6 | US 5Y Treasury Yield | 0.59% | | Euro Stoxx 50 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | GBP/USD | -2.85% |
| 2 | Petrolio WTI | 16.80% | | Solana | -2.67% |
| 3 | Gas naturale | 13.86% | | USD/JPY | -1.28% |
| 4 | VIX (volatilita) | 10.33% | | Dow Jones | -0.82% |
| 5 | US 30Y Treasury Yield | 4.44% | | EUR/USD | -0.61% |
| 6 | US 10Y Treasury Yield | 3.52% | | S&P 500 | -0.49% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -3.49% |
| 2 | Petrolio WTI | 16.87% | | EUR/USD | -2.42% |
| 3 | Solana | 16.28% | | GBP/USD | -1.82% |
| 4 | Gas naturale | 14.55% | | USD/JPY | -0.40% |
| 5 | US 5Y Treasury Yield | 13.36% | | FTSE MIB | 0.00% |
| 6 | US 10Y Treasury Yield | 11.37% | | Euro Stoxx 50 | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.101 | 11.37% | 0.00% | **11.37 pp** |
| S&P 500 vs Bitcoin | 0.006 | 0.46% | 9.83% | **-9.37 pp** |
| S&P 500 vs VIX (volatilita) | -0.040 | 0.46% | 7.43% | **-6.97 pp** |
| EUR/USD vs Indice dollaro DXY | 0.018 | -2.42% | 0.00% | **-2.42 pp** |
| S&P 500 vs Nasdaq Composite | 0.108 | 0.46% | 1.86% | **-1.40 pp** |
| S&P 500 vs Oro (spot) | 0.068 | 0.46% | 0.00% | **0.46 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.88 | 2026-09-30 | -0.01 |
| US 10Y Treasury Rate | 5.29 | 2026-09-30 | 0.03 |
| US 30Y Treasury Rate | 5.64 | 2026-09-30 | 0.05 |
| Spread 10Y-2Y USA | 0.46 | 2026-10-01 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **41.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.3400 | 7.43% | 108.75% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 118.8454 | 16.28% | 59.10% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Ethereum | 2 706.9673 | 7.72% | 37.92% | -5.78% |
| Bitcoin | 84 752.4565 | 9.83% | 36.74% | -6.86% |
| US 5Y Treasury Yield | 5.0900 | 13.36% | 18.98% | -1.65% |
| US 10Y Treasury Yield | 5.2900 | 11.37% | 16.57% | -2.70% |
| Nasdaq Composite | 26 861.0600 | 1.86% | 14.26% | -7.00% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| US 30Y Treasury Yield | 5.6400 | 7.43% | 13.29% | -1.49% |
| Dow Jones | 50 926.5600 | -3.49% | 11.39% | -6.34% |
| S&P 500 | 7 666.4500 | 0.46% | 10.72% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
