# Moneys Monitor - Report di mercato

Generato: `2026-09-22T16:28:32+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-22T16:27:52+00:00` (383 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.05% | 0.00% | **0.05 pp** |
| 1w | 4.55% | 0.00% | **4.55 pp** |
| 1m | 4.68% | 0.00% | **4.68 pp** |
| 3m | 15.84% | 19.01% | **-3.17 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | Ethereum | -1.34% |
| 2 | Petrolio WTI | 10.03% | | Solana | -1.27% |
| 3 | Gas naturale | 5.69% | | GBP/USD | -1.12% |
| 4 | Nasdaq Composite | 2.26% | | Bitcoin | -0.61% |
| 5 | USD/JPY | 2.06% | | EUR/USD | -0.23% |
| 6 | US 5Y Treasury Yield | 1.67% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | VIX (volatilita) | -13.04% |
| 2 | Petrolio WTI | 25.85% | | GBP/USD | -1.91% |
| 3 | Solana | 15.37% | | USD/JPY | -1.43% |
| 4 | Bitcoin | 12.88% | | Dow Jones | -0.71% |
| 5 | Ethereum | 11.79% | | EUR/USD | -0.66% |
| 6 | Gas naturale | 5.51% | | US 30Y Treasury Yield | -0.19% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | Dow Jones | -2.31% |
| 2 | Petrolio WTI | 36.89% | | EUR/USD | -1.84% |
| 3 | Solana | 17.22% | | VIX (volatilita) | -1.72% |
| 4 | Ethereum | 13.26% | | GBP/USD | -0.89% |
| 5 | Gas naturale | 11.57% | | USD/JPY | -0.55% |
| 6 | Bitcoin | 11.52% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| S&P 500 vs Bitcoin | -0.022 | 1.18% | 11.52% | **-10.34 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.039 | 5.74% | 0.00% | **5.74 pp** |
| S&P 500 vs VIX (volatilita) | -0.180 | 1.18% | -1.72% | **2.90 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | 1.18% | 3.60% | **-2.42 pp** |
| EUR/USD vs Indice dollaro DXY | 0.047 | -1.84% | 0.00% | **-1.84 pp** |
| S&P 500 vs Oro (spot) | -0.091 | 1.18% | 0.00% | **1.18 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.76 | 2026-09-18 | 0.09 |
| US 10Y Treasury Rate | 5.01 | 2026-09-18 | 0.07 |
| US 30Y Treasury Rate | 5.34 | 2026-09-18 | 0.05 |
| Spread 10Y-2Y USA | 0.20 | 2026-09-21 | -0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **25.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.8700 | -1.72% | 100.58% | -31.03% |
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| Solana | 116.9860 | 17.22% | 60.78% | -13.59% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Ethereum | 2 733.7872 | 13.26% | 42.34% | -5.78% |
| Bitcoin | 86 192.7124 | 11.52% | 41.52% | -6.86% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| US 5Y Treasury Yield | 4.8600 | n/d | 17.20% | -1.65% |
| Nasdaq Composite | 27 122.0900 | 3.60% | 15.12% | -7.00% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| US 10Y Treasury Yield | 5.0100 | 5.74% | 13.84% | -2.70% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| Dow Jones | 52 048.8300 | -2.31% | 10.97% | -5.31% |
| S&P 500 | 7 764.7000 | 1.18% | 10.72% | -3.42% |
| US 30Y Treasury Yield | 5.3400 | n/d | 10.21% | -1.49% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
