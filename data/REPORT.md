# Moneys Monitor - Report di mercato

Generato: `2026-11-13T21:50:03+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-13T21:49:26+00:00` (545 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.29% | 0.00% | **-1.29 pp** |
| 1w | -3.24% | 0.00% | **-3.24 pp** |
| 1m | -6.82% | 0.00% | **-6.82 pp** |
| 3m | -6.55% | 0.00% | **-6.55 pp** |
| 6m | 4.97% | 15.60% | **-10.62 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.91% |
| 2 | VIX (volatilita) | 6.92% | | Petrolio WTI | -10.06% |
| 3 | US 5Y Treasury Yield | 2.91% | | Bitcoin | -4.52% |
| 4 | US 10Y Treasury Yield | 2.41% | | Ethereum | -4.47% |
| 5 | US 30Y Treasury Yield | 1.50% | | Solana | -3.18% |
| 6 | USD/JPY | 0.48% | | Nasdaq Composite | -0.39% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | US 5Y Treasury Yield | 5.54% | | VIX (volatilita) | -33.64% |
| 2 | Nasdaq Composite | 4.32% | | Petrolio Brent | -26.55% |
| 3 | US 10Y Treasury Yield | 4.08% | | Ethereum | -13.55% |
| 4 | US 30Y Treasury Yield | 2.84% | | Solana | -11.87% |
| 5 | Dow Jones | 1.50% | | Bitcoin | -10.00% |
| 6 | GBP/USD | 1.04% | | Petrolio WTI | -6.88% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 10.85% | | Solana | -23.39% |
| 2 | Gas naturale | 9.77% | | Ethereum | -19.26% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -15.86% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -6.90% |
| 5 | Dow Jones | 1.31% | | S&P 500 | -2.81% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -2.34% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.021 | -2.81% | 10.85% | **-13.66 pp** |
| S&P 500 vs Bitcoin | -0.008 | -2.81% | -15.86% | **13.05 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.039 | -2.81% | -6.90% | **4.09 pp** |
| S&P 500 vs Oro (spot) | 0.037 | -2.81% | 0.00% | **-2.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.089 | -2.11% | 0.00% | **-2.11 pp** |
| EUR/USD vs Indice dollaro DXY | -0.130 | -1.39% | 0.00% | **-1.39 pp** |
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
| Spread 10Y-2Y USA | 0.24 | 2026-11-12 | -0.01 |
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
| Ethereum | 1 924.7997 | -19.26% | 45.32% | -30.54% |
| Solana | 78.7627 | -23.39% | 35.07% | -35.49% |
| Bitcoin | 68 230.0741 | -15.86% | 33.25% | -21.32% |
| Nasdaq Composite | 25 366.0900 | -6.90% | 31.50% | -11.90% |
| US 5Y Treasury Yield | 4.9500 | -1.00% | 25.08% | -9.82% |
| S&P 500 | 7 592.4000 | -2.81% | 23.63% | -5.95% |
| US 10Y Treasury Yield | 5.1000 | -2.11% | 21.32% | -8.85% |
| Dow Jones | 52 297.0900 | 1.31% | 20.32% | -6.34% |
| US 30Y Treasury Yield | 5.4300 | -2.34% | 16.58% | -7.41% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
