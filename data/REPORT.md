# Moneys Monitor - Report di mercato

Generato: `2026-09-04T10:48:44+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-04T10:48:12+00:00` (319 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.35% | 0.00% | **0.35 pp** |
| 1w | 1.20% | 0.00% | **1.20 pp** |
| 1m | 9.38% | 4.71% | **4.67 pp** |
| 3m | 13.94% | 15.30% | **-1.36 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | VIX (volatilita) | -6.98% |
| 2 | Petrolio Brent | 9.44% | | GBP/USD | -0.62% |
| 3 | Gas naturale | 3.83% | | US 5Y Treasury Yield | -0.22% |
| 4 | Nasdaq Composite | 1.40% | | Bitcoin | -0.20% |
| 5 | Ethereum | 1.22% | | FTSE MIB | 0.00% |
| 6 | Dow Jones | 1.18% | | Euro Stoxx 50 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | GBP/USD | -0.65% |
| 2 | Ethereum | 4.73% | | EUR/USD | -0.26% |
| 3 | Bitcoin | 4.56% | | VIX (volatilita) | -0.07% |
| 4 | US 5Y Treasury Yield | 3.89% | | FTSE MIB | 0.00% |
| 5 | Gas naturale | 3.17% | | Euro Stoxx 50 | 0.00% |
| 6 | US 10Y Treasury Yield | 2.79% | | Nikkei 225 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 36.93% | | CAC 40 Francia | -2.57% |
| 2 | Ethereum | 34.09% | | Nikkei 225 | -2.47% |
| 3 | Bitcoin | 27.65% | | FTSE MIB | -1.80% |
| 4 | Petrolio WTI | 21.65% | | VIX (volatilita) | -1.68% |
| 5 | Petrolio Brent | 20.57% | | Shanghai Composite | -1.45% |
| 6 | Gas naturale | 7.77% | | Russell 2000 | -1.26% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.006 | -0.07% | 27.65% | **-27.72 pp** |
| S&P 500 vs Oro (spot) | 0.085 | -0.07% | 5.05% | **-5.12 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.075 | 1.94% | 5.05% | **-3.11 pp** |
| EUR/USD vs Indice dollaro DXY | 0.034 | 0.61% | -1.04% | **1.65 pp** |
| S&P 500 vs VIX (volatilita) | -0.697 | -0.07% | -1.68% | **1.61 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.05% | 4.36% | **0.69 pp** |
| S&P 500 vs Nasdaq Composite | 0.954 | -0.07% | -0.08% | **0.01 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.39 | 2026-09-02 | 0.00 |
| US 10Y Treasury Rate | 4.79 | 2026-09-02 | 0.00 |
| US 30Y Treasury Rate | 5.27 | 2026-09-02 | 0.00 |
| Spread 10Y-2Y USA | 0.43 | 2026-09-03 | 0.03 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **40.0 bp**, 30Y-10Y **48.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.2000 | -1.68% | 74.36% | -31.03% |
| Ethereum | 2 527.5022 | 34.09% | 54.81% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 103.9457 | 36.93% | 46.06% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 81 042.2370 | 27.65% | 41.97% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 4.36% | 24.41% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.05% | 16.75% | -4.96% |
| US 5Y Treasury Yield | 4.5400 | n/d | 16.23% | -0.22% |
| Nikkei 225 | 65 856.4300 | -2.47% | 16.07% | -12.83% |
| Nasdaq Composite | 26 584.0600 | -0.08% | 12.07% | -7.00% |
| US 10Y Treasury Yield | 4.7900 | 1.94% | 11.51% | -2.70% |
| Hang Seng | 25 511.1000 | 0.28% | 10.74% | -3.43% |
| Rame | 6.6680 | 0.92% | 10.54% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
