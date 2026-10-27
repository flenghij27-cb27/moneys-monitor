# Moneys Monitor - Report di mercato

Generato: `2026-10-27T17:37:50+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-27T17:37:19+00:00` (494 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.56% | 0.00% | **0.56 pp** |
| 1w | -0.61% | 0.00% | **-0.61 pp** |
| 1m | -3.84% | 0.00% | **-3.84 pp** |
| 3m | 1.04% | -0.76% | **1.80 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.87% | | Petrolio Brent | -8.95% |
| 2 | Ethereum | 2.07% | | VIX (volatilita) | -5.45% |
| 3 | Bitcoin | 1.14% | | Gas naturale | -3.73% |
| 4 | Solana | 0.85% | | USD/JPY | -0.72% |
| 5 | US 5Y Treasury Yield | 0.84% | | EUR/USD | -0.34% |
| 6 | Nasdaq Composite | 0.82% | | Indice dollaro Fed (broad) | -0.07% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 4.38% | | Petrolio Brent | -11.91% |
| 2 | Indice dollaro Fed (broad) | 1.51% | | Solana | -3.01% |
| 3 | Petrolio WTI | 0.81% | | US 30Y Treasury Yield | -1.84% |
| 4 | Dow Jones | 0.76% | | US 10Y Treasury Yield | -1.77% |
| 5 | S&P 500 | 0.23% | | Ethereum | -1.43% |
| 6 | GBP/USD | 0.02% | | US 5Y Treasury Yield | -1.43% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 32.93% | | Solana | -16.52% |
| 2 | Petrolio Brent | 32.51% | | Ethereum | -12.86% |
| 3 | VIX (volatilita) | 29.42% | | Bitcoin | -5.82% |
| 4 | Gas naturale | 13.51% | | US 5Y Treasury Yield | -3.41% |
| 5 | Dow Jones | 1.03% | | Nasdaq Composite | -2.86% |
| 6 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -2.15% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.091 | -0.36% | 29.42% | **-29.78 pp** |
| S&P 500 vs Bitcoin | 0.203 | -0.36% | -5.82% | **5.46 pp** |
| S&P 500 vs Nasdaq Composite | 0.853 | -0.36% | -2.86% | **2.50 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.053 | -2.15% | 0.00% | **-2.15 pp** |
| EUR/USD vs Indice dollaro DXY | 0.002 | -2.00% | 0.00% | **-2.00 pp** |
| Petrolio WTI vs Petrolio Brent | 0.819 | 32.93% | 32.51% | **0.42 pp** |
| S&P 500 vs Oro (spot) | 0.185 | -0.36% | 0.00% | **-0.36 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.69 | 2026-10-23 | 0.04 |
| US 10Y Treasury Rate | 5.00 | 2026-10-23 | 0.04 |
| US 30Y Treasury Rate | 5.33 | 2026-10-23 | 0.04 |
| Spread 10Y-2Y USA | 0.32 | 2026-10-26 | 0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **31.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 18.3900 | 29.42% | 114.47% | -31.22% |
| Petrolio Brent | 115.2200 | 32.51% | 114.17% | -21.50% |
| Petrolio WTI | 107.8900 | 32.93% | 74.25% | -18.71% |
| Gas naturale | 3.1000 | 13.51% | 58.95% | -18.87% |
| Ethereum | 2 350.7376 | -12.86% | 33.28% | -16.88% |
| Solana | 101.0200 | -16.52% | 32.97% | -17.96% |
| Bitcoin | 80 657.9108 | -5.82% | 22.70% | -8.03% |
| US 5Y Treasury Yield | 4.8200 | -3.41% | 18.22% | -6.09% |
| US 10Y Treasury Yield | 5.0000 | -2.15% | 17.28% | -6.59% |
| Nasdaq Composite | 26 169.3800 | -2.86% | 15.69% | -7.00% |
| US 30Y Treasury Yield | 5.3300 | -1.30% | 15.11% | -6.70% |
| USD/JPY | 156.8700 | -1.68% | 13.95% | -6.19% |
| S&P 500 | 7 676.7700 | -0.36% | 11.04% | -3.42% |
| Dow Jones | 52 361.5800 | 1.03% | 9.62% | -6.34% |
| Indice dollaro Fed (broad) | 121.3202 | n/d | 8.60% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
