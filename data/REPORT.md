# Moneys Monitor - Report di mercato

Generato: `2026-11-14T13:06:20+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-14T13:05:45+00:00` (547 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.95% | 0.00% | **-0.95 pp** |
| 1w | -3.03% | 0.00% | **-3.03 pp** |
| 1m | -7.31% | 0.00% | **-7.31 pp** |
| 3m | -7.33% | 0.00% | **-7.33 pp** |
| 6m | 2.51% | 13.36% | **-10.84 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.91% |
| 2 | VIX (volatilita) | 6.92% | | Petrolio WTI | -10.06% |
| 3 | US 5Y Treasury Yield | 2.91% | | Solana | -4.32% |
| 4 | US 10Y Treasury Yield | 2.41% | | Bitcoin | -2.14% |
| 5 | US 30Y Treasury Yield | 1.50% | | Ethereum | -1.68% |
| 6 | USD/JPY | 0.48% | | Nasdaq Composite | -0.91% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | US 5Y Treasury Yield | 5.54% | | VIX (volatilita) | -33.64% |
| 2 | US 10Y Treasury Yield | 4.08% | | Petrolio Brent | -26.55% |
| 3 | US 30Y Treasury Yield | 2.84% | | Solana | -12.93% |
| 4 | S&P 500 | 2.83% | | Bitcoin | -11.28% |
| 5 | Nasdaq Composite | 2.27% | | Ethereum | -11.22% |
| 6 | Dow Jones | 2.07% | | Petrolio WTI | -6.88% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 10.85% | | Solana | -25.95% |
| 2 | Gas naturale | 9.77% | | Ethereum | -19.25% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -17.11% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -7.60% |
| 5 | Dow Jones | 0.33% | | S&P 500 | -3.15% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -2.34% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.629 | -3.15% | 10.85% | **-14.00 pp** |
| S&P 500 vs Bitcoin | -0.003 | -3.15% | -17.11% | **13.96 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.042 | -3.15% | -7.60% | **4.45 pp** |
| S&P 500 vs Oro (spot) | 0.037 | -3.15% | 0.00% | **-3.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.025 | -2.11% | 0.00% | **-2.11 pp** |
| EUR/USD vs Indice dollaro DXY | -0.008 | -1.39% | 0.00% | **-1.39 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.86 | 2026-11-12 | 0.13 |
| US 10Y Treasury Rate | 5.10 | 2026-11-12 | 0.12 |
| US 30Y Treasury Rate | 5.43 | 2026-11-12 | 0.08 |
| Spread 10Y-2Y USA | 0.27 | 2026-11-13 | 0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **24.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 18.7000 | 10.85% | 304.75% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Ethereum | 1 892.5478 | -19.25% | 45.36% | -31.70% |
| Solana | 75.3578 | -25.95% | 36.54% | -38.28% |
| Bitcoin | 66 768.4674 | -17.11% | 33.55% | -23.01% |
| Nasdaq Composite | 25 136.2700 | -7.60% | 31.05% | -11.90% |
| US 5Y Treasury Yield | 4.9500 | -1.00% | 25.08% | -9.82% |
| S&P 500 | 7 561.6700 | -3.15% | 23.65% | -5.95% |
| US 10Y Treasury Yield | 5.1000 | -2.11% | 21.32% | -8.85% |
| Dow Jones | 52 347.5500 | 0.33% | 20.28% | -6.34% |
| US 30Y Treasury Yield | 5.4300 | -2.34% | 16.58% | -7.41% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
