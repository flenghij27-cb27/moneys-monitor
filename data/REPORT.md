# Moneys Monitor - Report di mercato

Generato: `2026-10-16T10:55:04+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-16T10:53:56+00:00` (456 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.26% | 0.00% | **0.26 pp** |
| 1w | -1.09% | 0.00% | **-1.09 pp** |
| 1m | -1.79% | 0.00% | **-1.79 pp** |
| 3m | 10.71% | 4.71% | **6.01 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 10.48% | | US 30Y Treasury Yield | -0.72% |
| 2 | Gas naturale | 6.27% | | US 10Y Treasury Yield | -0.38% |
| 3 | Petrolio WTI | 5.89% | | GBP/USD | -0.04% |
| 4 | Solana | 1.19% | | Bitcoin | -0.01% |
| 5 | Dow Jones | 1.08% | | FTSE MIB | 0.00% |
| 6 | Ethereum | 0.97% | | Euro Stoxx 50 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 15.56% | | Solana | -4.25% |
| 2 | Gas naturale | 14.59% | | Ethereum | -2.83% |
| 3 | VIX (volatilita) | 11.87% | | GBP/USD | -2.16% |
| 4 | Petrolio WTI | 4.78% | | US 30Y Treasury Yield | -2.13% |
| 5 | Indice dollaro Fed (broad) | 2.99% | | Bitcoin | -1.79% |
| 6 | Dow Jones | 1.85% | | Nasdaq Composite | -1.77% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -12.44% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -8.51% |
| 3 | Gas naturale | 15.16% | | VIX (volatilita) | -5.44% |
| 4 | US 10Y Treasury Yield | 4.43% | | EUR/USD | -2.85% |
| 5 | US 5Y Treasury Yield | 4.17% | | Bitcoin | -2.34% |
| 6 | US 30Y Treasury Yield | 3.37% | | GBP/USD | -2.05% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs VIX (volatilita) | -0.032 | 2.55% | -5.44% | **7.99 pp** |
| S&P 500 vs Bitcoin | 0.019 | 2.55% | -2.34% | **4.89 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.032 | 4.43% | 0.00% | **4.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.008 | -2.85% | 0.00% | **-2.85 pp** |
| S&P 500 vs Oro (spot) | 0.282 | 2.55% | 0.00% | **2.55 pp** |
| S&P 500 vs Nasdaq Composite | 0.948 | 2.55% | 2.83% | **-0.28 pp** |
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
| Solana | 106.5329 | -12.44% | 33.55% | -14.70% |
| Ethereum | 2 461.9312 | -8.51% | 27.92% | -12.70% |
| US 5Y Treasury Yield | 5.0000 | 4.17% | 18.62% | -1.96% |
| Bitcoin | 82 104.9970 | -2.34% | 17.97% | -6.86% |
| US 10Y Treasury Yield | 5.1900 | 4.43% | 17.06% | -2.70% |
| Nasdaq Composite | 26 713.0300 | 2.83% | 14.71% | -7.00% |
| US 30Y Treasury Yield | 5.5200 | 3.37% | 14.16% | -2.65% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| S&P 500 | 7 744.0600 | 2.55% | 9.62% | -3.42% |
| Dow Jones | 52 177.6900 | 1.39% | 9.22% | -6.34% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
