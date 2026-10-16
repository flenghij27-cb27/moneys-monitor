# Moneys Monitor - Report di mercato

Generato: `2026-10-16T16:14:27+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-16T16:13:51+00:00` (457 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.17% | 0.00% | **-0.17 pp** |
| 1w | -1.50% | 0.00% | **-1.50 pp** |
| 1m | -2.18% | 0.00% | **-2.18 pp** |
| 3m | 10.14% | 4.71% | **5.43 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.27% | | VIX (volatilita) | -2.43% |
| 2 | Petrolio WTI | 5.89% | | Solana | -1.15% |
| 3 | Dow Jones | 1.08% | | Bitcoin | -0.76% |
| 4 | Petrolio Brent | 0.88% | | US 30Y Treasury Yield | -0.72% |
| 5 | EUR/USD | 0.40% | | US 10Y Treasury Yield | -0.38% |
| 6 | USD/JPY | 0.34% | | Ethereum | -0.23% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 15.56% | | Solana | -6.46% |
| 2 | Gas naturale | 14.59% | | Ethereum | -3.99% |
| 3 | VIX (volatilita) | 6.81% | | Bitcoin | -2.53% |
| 4 | Petrolio WTI | 4.78% | | GBP/USD | -2.16% |
| 5 | Indice dollaro Fed (broad) | 2.99% | | US 30Y Treasury Yield | -2.13% |
| 6 | Dow Jones | 1.85% | | Nasdaq Composite | -1.77% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -14.46% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -9.60% |
| 3 | Gas naturale | 15.16% | | Bitcoin | -3.08% |
| 4 | US 10Y Treasury Yield | 4.43% | | GBP/USD | -2.05% |
| 5 | US 5Y Treasury Yield | 4.17% | | EUR/USD | -1.99% |
| 6 | VIX (volatilita) | 3.91% | | USD/JPY | -0.63% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs Bitcoin | 0.018 | 2.55% | -3.08% | **5.63 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.032 | 4.43% | 0.00% | **4.43 pp** |
| S&P 500 vs Oro (spot) | 0.282 | 2.55% | 0.00% | **2.55 pp** |
| EUR/USD vs Indice dollaro DXY | 0.056 | -1.99% | 0.00% | **-1.99 pp** |
| S&P 500 vs VIX (volatilita) | 0.073 | 2.55% | 3.91% | **-1.36 pp** |
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
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **37.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 126.5500 | 42.82% | 107.21% | -21.50% |
| VIX (volatilita) | 16.4600 | 3.91% | 87.84% | -31.22% |
| Petrolio WTI | 101.9100 | 22.98% | 72.41% | -18.71% |
| Gas naturale | 3.2200 | 15.16% | 56.78% | -18.87% |
| Solana | 104.0741 | -14.46% | 32.90% | -14.76% |
| Ethereum | 2 432.6200 | -9.60% | 27.44% | -12.70% |
| US 5Y Treasury Yield | 5.0000 | 4.17% | 18.62% | -1.96% |
| Bitcoin | 81 483.7852 | -3.08% | 18.10% | -6.86% |
| US 10Y Treasury Yield | 5.1900 | 4.43% | 17.06% | -2.70% |
| Nasdaq Composite | 26 713.0300 | 2.83% | 14.71% | -7.00% |
| US 30Y Treasury Yield | 5.5200 | 3.37% | 14.16% | -2.65% |
| USD/JPY | 158.3400 | -0.63% | 13.74% | -6.19% |
| S&P 500 | 7 744.0600 | 2.55% | 9.62% | -3.42% |
| Dow Jones | 52 177.6900 | 1.39% | 9.22% | -6.34% |
| Indice dollaro Fed (broad) | 121.6023 | n/d | 8.91% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
