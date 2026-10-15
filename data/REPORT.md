# Moneys Monitor - Report di mercato

Generato: `2026-10-15T23:45:36+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-15T23:44:57+00:00` (455 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.05% | 0.00% | **-0.05 pp** |
| 1w | -1.28% | 0.00% | **-1.28 pp** |
| 1m | -1.74% | 0.00% | **-1.74 pp** |
| 3m | 10.49% | 5.61% | **4.88 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 10.48% | | Nasdaq Composite | -1.88% |
| 2 | Gas naturale | 6.27% | | S&P 500 | -1.11% |
| 3 | Petrolio WTI | 5.89% | | US 30Y Treasury Yield | -0.72% |
| 4 | Solana | 1.09% | | US 10Y Treasury Yield | -0.38% |
| 5 | Dow Jones | 1.08% | | GBP/USD | -0.04% |
| 6 | Petrolio Brent | 0.88% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 15.56% | | Solana | -4.64% |
| 2 | Gas naturale | 14.59% | | Nasdaq Composite | -3.07% |
| 3 | VIX (volatilita) | 11.87% | | Ethereum | -3.00% |
| 4 | Petrolio WTI | 4.78% | | GBP/USD | -2.16% |
| 5 | Indice dollaro Fed (broad) | 2.99% | | US 30Y Treasury Yield | -2.13% |
| 6 | Dow Jones | 1.85% | | US 10Y Treasury Yield | -1.52% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -10.02% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -9.26% |
| 3 | Gas naturale | 15.16% | | VIX (volatilita) | -5.44% |
| 4 | US 10Y Treasury Yield | 4.43% | | EUR/USD | -2.85% |
| 5 | US 5Y Treasury Yield | 4.17% | | Bitcoin | -2.67% |
| 6 | US 30Y Treasury Yield | 3.37% | | GBP/USD | -2.05% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs VIX (volatilita) | 0.075 | 1.76% | -5.44% | **7.20 pp** |
| S&P 500 vs Bitcoin | 0.020 | 1.76% | -2.67% | **4.43 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.101 | 4.43% | 0.00% | **4.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.054 | -2.85% | 0.00% | **-2.85 pp** |
| S&P 500 vs Oro (spot) | 0.283 | 1.76% | 0.00% | **1.76 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 1.76% | 2.74% | **-0.98 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.82 | 2026-10-14 | 0.03 |
| US 10Y Treasury Rate | 5.19 | 2026-10-14 | -0.02 |
| US 30Y Treasury Rate | 5.52 | 2026-10-14 | -0.04 |
| Spread 10Y-2Y USA | 0.33 | 2026-10-15 | -0.04 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **37.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 126.5500 | 42.82% | 107.21% | -21.50% |
| VIX (volatilita) | 16.8700 | -5.44% | 91.75% | -31.22% |
| Petrolio WTI | 101.9100 | 22.98% | 72.41% | -18.71% |
| Gas naturale | 3.2200 | 15.16% | 56.78% | -18.87% |
| Solana | 105.2842 | -10.02% | 32.90% | -14.70% |
| Ethereum | 2 438.2848 | -9.26% | 27.51% | -12.70% |
| US 5Y Treasury Yield | 5.0000 | 4.17% | 18.62% | -1.96% |
| Bitcoin | 82 111.0372 | -2.67% | 18.03% | -6.86% |
| US 10Y Treasury Yield | 5.1900 | 4.43% | 17.06% | -2.70% |
| Nasdaq Composite | 26 692.8700 | 2.74% | 15.81% | -7.00% |
| US 30Y Treasury Yield | 5.5200 | 3.37% | 14.16% | -2.65% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| S&P 500 | 7 718.9400 | 1.76% | 10.32% | -3.42% |
| Dow Jones | 52 177.6900 | 1.39% | 9.22% | -6.34% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
