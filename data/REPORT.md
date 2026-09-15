# Moneys Monitor - Report di mercato

Generato: `2026-09-15T11:17:26+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-15T11:16:54+00:00` (358 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.55% | 0.00% | **-0.55 pp** |
| 1w | 0.16% | 0.00% | **0.16 pp** |
| 1m | 0.47% | -0.76% | **1.23 pp** |
| 3m | 9.81% | 13.79% | **-3.98 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 14.05% | | VIX (volatilita) | -11.21% |
| 2 | Petrolio WTI | 6.32% | | Gas naturale | -3.10% |
| 3 | US 5Y Treasury Yield | 0.63% | | Solana | -1.66% |
| 4 | US 10Y Treasury Yield | 0.20% | | USD/JPY | -1.54% |
| 5 | Indice dollaro Fed (broad) | 0.12% | | Bitcoin | -1.49% |
| 6 | GBP/USD | 0.02% | | Ethereum | -1.35% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 16.02% | | USD/JPY | -3.32% |
| 2 | Petrolio WTI | 11.72% | | Dow Jones | -1.86% |
| 3 | VIX (volatilita) | 10.61% | | S&P 500 | -1.28% |
| 4 | US 5Y Treasury Yield | 5.75% | | Nasdaq Composite | -1.21% |
| 5 | US 10Y Treasury Yield | 3.98% | | GBP/USD | -0.76% |
| 6 | Solana | 1.91% | | EUR/USD | -0.61% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 33.35% | | USD/JPY | -2.56% |
| 2 | Petrolio WTI | 26.39% | | Dow Jones | -2.44% |
| 3 | VIX (volatilita) | 11.16% | | S&P 500 | -2.13% |
| 4 | Solana | 6.10% | | Nasdaq Composite | -2.03% |
| 5 | US 10Y Treasury Yield | 5.62% | | Hang Seng | -1.92% |
| 6 | Gas naturale | 5.20% | | Argento (spot) | -1.78% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.592 | -2.13% | 11.16% | **-13.29 pp** |
| Petrolio WTI vs Petrolio Brent | 0.955 | 26.39% | 33.35% | **-6.96 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | 5.62% | 0.26% | **5.36 pp** |
| S&P 500 vs Oro (spot) | -0.178 | -2.13% | 0.26% | **-2.39 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 0.26% | -1.78% | **2.04 pp** |
| S&P 500 vs Bitcoin | -0.037 | -2.13% | -0.32% | **-1.81 pp** |
| EUR/USD vs Indice dollaro DXY | -0.015 | -0.27% | 0.12% | **-0.39 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | -2.13% | -2.03% | **-0.10 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.63 | 2026-09-11 | 0.07 |
| US 10Y Treasury Rate | 4.96 | 2026-09-11 | 0.01 |
| US 30Y Treasury Rate | 5.35 | 2026-09-11 | -0.02 |
| Spread 10Y-2Y USA | 0.32 | 2026-09-14 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **33.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.8400 | 11.16% | 92.61% | -31.03% |
| Petrolio Brent | 109.5100 | 33.35% | 64.88% | -21.50% |
| Petrolio WTI | 97.2600 | 26.39% | 51.50% | -18.71% |
| Solana | 100.8336 | 6.10% | 42.78% | -13.59% |
| Gas naturale | 2.8100 | 5.20% | 34.84% | -18.87% |
| Ethereum | 2 482.2614 | 1.72% | 29.97% | -5.78% |
| Bitcoin | 77 008.2019 | -0.32% | 27.44% | -5.72% |
| US 5Y Treasury Yield | 4.7800 | n/d | 16.58% | -0.66% |
| US 10Y Treasury Yield | 4.9600 | 5.62% | 13.37% | -2.70% |
| Nasdaq Composite | 26 186.4100 | -2.03% | 12.61% | -7.00% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| Dow Jones | 52 421.2000 | -2.44% | 11.03% | -4.20% |
| US 30Y Treasury Yield | 5.3500 | n/d | 9.36% | -0.57% |
| S&P 500 | 7 619.9800 | -2.13% | 9.01% | -3.42% |
| EUR/USD | 1.1551 | -0.27% | 4.57% | -1.12% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
