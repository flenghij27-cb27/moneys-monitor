# Moneys Monitor - Report di mercato

Generato: `2026-11-12T22:06:24+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-12T22:05:52+00:00` (542 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.70% | 0.00% | **-0.70 pp** |
| 1w | -2.49% | 0.00% | **-2.49 pp** |
| 1m | -5.84% | 0.00% | **-5.84 pp** |
| 3m | -4.90% | 0.00% | **-4.90 pp** |
| 6m | 4.40% | 13.53% | **-9.13 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.05% |
| 2 | US 5Y Treasury Yield | 3.00% | | VIX (volatilita) | -10.12% |
| 3 | US 10Y Treasury Yield | 2.05% | | Bitcoin | -3.75% |
| 4 | US 30Y Treasury Yield | 1.71% | | Petrolio WTI | -3.61% |
| 5 | Nasdaq Composite | 1.60% | | Solana | -3.52% |
| 6 | S&P 500 | 1.31% | | Ethereum | -2.64% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 5.30% | | Ethereum | -9.77% |
| 2 | Petrolio WTI | 3.62% | | Solana | -9.16% |
| 3 | US 5Y Treasury Yield | 1.48% | | Petrolio Brent | -6.08% |
| 4 | GBP/USD | 1.04% | | Bitcoin | -5.62% |
| 5 | S&P 500 | 0.67% | | Dow Jones | -1.63% |
| 6 | US 10Y Treasury Yield | 0.61% | | EUR/USD | -1.27% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 20.92% | | Solana | -21.89% |
| 2 | Petrolio Brent | 20.91% | | Ethereum | -15.52% |
| 3 | VIX (volatilita) | 14.54% | | Bitcoin | -12.20% |
| 4 | Gas naturale | 9.77% | | Nasdaq Composite | -6.94% |
| 5 | Dow Jones | 1.58% | | US 10Y Treasury Yield | -4.96% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -4.46% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.024 | -1.88% | 14.54% | **-16.42 pp** |
| S&P 500 vs Bitcoin | -0.018 | -1.88% | -12.20% | **10.32 pp** |
| S&P 500 vs Nasdaq Composite | 0.037 | -1.88% | -6.94% | **5.06 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.087 | -4.96% | 0.00% | **-4.96 pp** |
| S&P 500 vs Oro (spot) | 0.036 | -1.88% | 0.00% | **-1.88 pp** |
| EUR/USD vs Indice dollaro DXY | -0.130 | -1.02% | 0.00% | **-1.02 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.73 | 2026-11-10 | 0.17 |
| US 10Y Treasury Rate | 4.98 | 2026-11-10 | 0.10 |
| US 30Y Treasury Rate | 5.35 | 2026-11-10 | 0.09 |
| Spread 10Y-2Y USA | 0.24 | 2026-11-12 | -0.01 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **25.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.4900 | 14.54% | 304.57% | -37.93% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Ethereum | 2 014.7703 | -15.52% | 43.49% | -27.29% |
| Solana | 81.3532 | -21.89% | 34.32% | -33.37% |
| Nasdaq Composite | 25 466.1900 | -6.94% | 31.50% | -11.90% |
| Bitcoin | 71 462.6454 | -12.20% | 30.21% | -17.59% |
| S&P 500 | 7 619.3800 | -1.88% | 23.62% | -5.95% |
| US 5Y Treasury Yield | 4.8100 | -4.18% | 22.54% | -9.82% |
| Dow Jones | 52 486.4900 | 1.58% | 20.60% | -6.34% |
| US 10Y Treasury Yield | 4.9800 | -4.96% | 19.20% | -8.85% |
| US 30Y Treasury Yield | 5.3500 | -4.46% | 15.63% | -7.41% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
