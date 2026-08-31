# Moneys Monitor - Report di mercato

Generato: `2026-08-31T21:21:07+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-08-31T21:20:32+00:00` (307 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.50% | 0.00% | **0.50 pp** |
| 1w | 1.18% | -0.53% | **1.71 pp** |
| 1m | 8.44% | 7.11% | **1.33 pp** |
| 3m | 18.07% | 14.50% | **3.57 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.44% | | Petrolio WTI | -1.87% |
| 2 | Ethereum | 2.40% | | GBP/USD | -0.62% |
| 3 | US 5Y Treasury Yield | 2.28% | | Petrolio Brent | -0.57% |
| 4 | Bitcoin | 1.67% | | VIX (volatilita) | -0.55% |
| 5 | Solana | 1.67% | | Nasdaq Composite | -0.52% |
| 6 | US 10Y Treasury Yield | 1.28% | | EUR/USD | -0.40% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 7.48% | | Petrolio Brent | -6.60% |
| 2 | Rame | 1.00% | | Petrolio WTI | -5.02% |
| 3 | Nasdaq Composite | 0.85% | | VIX (volatilita) | -4.63% |
| 4 | DAX Germania | 0.71% | | Argento (spot) | -0.76% |
| 5 | USD/JPY | 0.67% | | EUR/USD | -0.70% |
| 6 | Dow Jones | 0.53% | | GBP/USD | -0.65% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 35.71% | | VIX (volatilita) | -3.15% |
| 2 | Ethereum | 28.80% | | CAC 40 Francia | -3.01% |
| 3 | Bitcoin | 21.19% | | FTSE MIB | -1.83% |
| 4 | Petrolio Brent | 10.64% | | Dow Jones | -1.45% |
| 5 | Petrolio WTI | 9.76% | | Shanghai Composite | -1.28% |
| 6 | Argento (spot) | 7.55% | | Euro Stoxx 50 | -0.96% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.033 | -0.15% | 21.19% | **-21.34 pp** |
| S&P 500 vs Oro (spot) | 0.089 | -0.15% | 6.67% | **-6.82 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.029 | 1.50% | 6.67% | **-5.17 pp** |
| S&P 500 vs VIX (volatilita) | 0.051 | -0.15% | -3.15% | **3.00 pp** |
| EUR/USD vs Indice dollaro DXY | -0.118 | 0.30% | -0.64% | **0.94 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 6.67% | 7.55% | **-0.88 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| S&P 500 vs Nasdaq Composite | 0.954 | -0.15% | 0.15% | **-0.30 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-07-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.34 | 2026-08-28 | 0.14 |
| US 10Y Treasury Rate | 4.73 | 2026-08-28 | 0.06 |
| US 30Y Treasury Rate | 5.22 | 2026-08-28 | 0.03 |
| Spread 10Y-2Y USA | 0.41 | 2026-08-31 | 0.02 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **39.0 bp**, 30Y-10Y **49.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.4300 | -3.15% | 61.11% | -31.03% |
| Ethereum | 2 471.2388 | 28.80% | 53.01% | -5.78% |
| Solana | 103.3017 | 35.71% | 43.09% | -13.59% |
| Bitcoin | 78 804.4118 | 21.19% | 39.42% | -5.72% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Argento (spot) | 68.2900 | 7.55% | 28.87% | -11.21% |
| Nikkei 225 | 65 856.4300 | 0.38% | 18.73% | -12.83% |
| Oro (spot) | 4 693.0000 | 6.67% | 18.18% | -4.96% |
| Hang Seng | 25 511.1000 | -0.61% | 12.46% | -3.43% |
| Bovespa Brasile | 172 458.6200 | -0.03% | 12.40% | -6.51% |
| US 10Y Treasury Yield | 4.7300 | 1.50% | 11.54% | -2.70% |
| Shanghai Composite | 3 889.4450 | -1.28% | 11.32% | -8.47% |
| Rame | 6.6680 | 1.17% | 10.94% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
