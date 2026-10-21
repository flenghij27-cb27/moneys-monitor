# Moneys Monitor - Report di mercato

Generato: `2026-10-21T00:03:32+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-21T00:01:47+00:00` (472 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.13% | 0.00% | **0.13 pp** |
| 1w | -0.02% | 0.00% | **-0.02 pp** |
| 1m | -1.88% | 0.00% | **-1.88 pp** |
| 3m | 10.24% | 4.20% | **6.04 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.27% | | VIX (volatilita) | -7.75% |
| 2 | Petrolio WTI | 5.89% | | Nasdaq Composite | -1.06% |
| 3 | US 10Y Treasury Yield | 1.18% | | USD/JPY | -0.21% |
| 4 | Dow Jones | 1.02% | | Indice dollaro Fed (broad) | -0.16% |
| 5 | US 5Y Treasury Yield | 1.02% | | EUR/USD | -0.09% |
| 6 | US 30Y Treasury Yield | 0.92% | | FTSE MIB | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 21.24% | | Nasdaq Composite | -3.42% |
| 2 | Petrolio Brent | 15.56% | | US 30Y Treasury Yield | -2.14% |
| 3 | Gas naturale | 14.59% | | US 10Y Treasury Yield | -1.72% |
| 4 | Petrolio WTI | 4.78% | | US 5Y Treasury Yield | -1.59% |
| 5 | USD/JPY | 2.79% | | S&P 500 | -1.49% |
| 6 | Indice dollaro Fed (broad) | 2.70% | | GBP/USD | -1.43% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.82% | | Solana | -9.84% |
| 2 | Petrolio WTI | 22.98% | | Ethereum | -8.68% |
| 3 | Gas naturale | 15.16% | | EUR/USD | -2.39% |
| 4 | VIX (volatilita) | 7.21% | | GBP/USD | -1.22% |
| 5 | US 10Y Treasury Yield | 4.25% | | USD/JPY | -0.88% |
| 6 | US 30Y Treasury Yield | 3.59% | | Bitcoin | -0.85% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.903 | 22.98% | 42.82% | **-19.84 pp** |
| S&P 500 vs VIX (volatilita) | -0.013 | 0.53% | 7.21% | **-6.68 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.099 | 4.25% | 0.00% | **4.25 pp** |
| EUR/USD vs Indice dollaro DXY | -0.134 | -2.39% | 0.00% | **-2.39 pp** |
| S&P 500 vs Bitcoin | 0.080 | 0.53% | -0.85% | **1.38 pp** |
| S&P 500 vs Oro (spot) | 0.042 | 0.53% | 0.00% | **0.53 pp** |
| S&P 500 vs Nasdaq Composite | 0.092 | 0.53% | 0.05% | **0.48 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.77 | 2026-10-19 | 0.03 |
| US 10Y Treasury Rate | 5.15 | 2026-10-19 | 0.06 |
| US 30Y Treasury Rate | 5.48 | 2026-10-19 | 0.05 |
| Spread 10Y-2Y USA | 0.33 | 2026-10-20 | -0.05 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **38.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 18.4400 | 7.21% | 120.15% | -31.22% |
| Petrolio Brent | 126.5500 | 42.82% | 107.21% | -21.50% |
| Petrolio WTI | 101.9100 | 22.98% | 72.41% | -18.71% |
| Gas naturale | 3.2200 | 15.16% | 56.78% | -18.87% |
| Solana | 106.3718 | -9.84% | 32.42% | -15.47% |
| Ethereum | 2 446.3235 | -8.68% | 28.46% | -13.58% |
| US 5Y Treasury Yield | 4.9400 | 3.35% | 18.28% | -3.93% |
| Bitcoin | 82 904.6152 | -0.85% | 17.77% | -6.86% |
| US 10Y Treasury Yield | 5.1500 | 4.25% | 17.35% | -4.14% |
| Nasdaq Composite | 26 430.8900 | 0.05% | 15.17% | -7.00% |
| US 30Y Treasury Yield | 5.4800 | 3.59% | 14.81% | -4.23% |
| USD/JPY | 158.0000 | -0.88% | 13.75% | -6.19% |
| Dow Jones | 52 495.8800 | 0.86% | 9.53% | -6.34% |
| S&P 500 | 7 690.7300 | 0.53% | 9.03% | -3.42% |
| Indice dollaro Fed (broad) | 121.4048 | n/d | 8.89% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
