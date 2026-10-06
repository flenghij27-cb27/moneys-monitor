# Moneys Monitor - Report di mercato

Generato: `2026-10-06T20:49:40+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-06T20:48:57+00:00` (427 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.01% | 0.00% | **0.01 pp** |
| 1w | 0.74% | 0.00% | **0.74 pp** |
| 1m | 5.37% | 0.00% | **5.37 pp** |
| 3m | 16.65% | 16.23% | **0.43 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | Petrolio Brent | -0.81% |
| 2 | VIX (volatilita) | 1.37% | | Ethereum | -0.78% |
| 3 | Nasdaq Composite | 1.05% | | Bitcoin | -0.41% |
| 4 | Indice dollaro Fed (broad) | 0.88% | | Solana | -0.40% |
| 5 | S&P 500 | 0.66% | | Petrolio WTI | -0.26% |
| 6 | EUR/USD | 0.58% | | GBP/USD | -0.12% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | VIX (volatilita) | -3.42% |
| 2 | Petrolio WTI | 16.80% | | GBP/USD | -2.37% |
| 3 | Gas naturale | 13.86% | | USD/JPY | -1.35% |
| 4 | Solana | 2.52% | | EUR/USD | -0.76% |
| 5 | Nasdaq Composite | 2.45% | | Dow Jones | -0.41% |
| 6 | Indice dollaro Fed (broad) | 2.22% | | FTSE MIB | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -4.50% |
| 2 | Solana | 24.47% | | EUR/USD | -3.04% |
| 3 | Petrolio WTI | 16.87% | | GBP/USD | -2.02% |
| 4 | Gas naturale | 14.55% | | USD/JPY | -0.95% |
| 5 | Bitcoin | 13.24% | | FTSE MIB | 0.00% |
| 6 | Ethereum | 12.33% | | Euro Stoxx 50 | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.081 | 0.34% | 13.24% | **-12.90 pp** |
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.075 | 11.32% | 0.00% | **11.32 pp** |
| S&P 500 vs VIX (volatilita) | 0.140 | 0.34% | 4.02% | **-3.68 pp** |
| EUR/USD vs Indice dollaro DXY | 0.096 | -3.04% | 0.00% | **-3.04 pp** |
| S&P 500 vs Nasdaq Composite | 0.950 | 0.34% | 3.36% | **-3.02 pp** |
| S&P 500 vs Oro (spot) | -0.159 | 0.34% | 0.00% | **0.34 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.84 | 2026-10-05 | 0.01 |
| US 10Y Treasury Rate | 5.31 | 2026-10-05 | 0.03 |
| US 30Y Treasury Rate | 5.66 | 2026-10-05 | 0.03 |
| Spread 10Y-2Y USA | 0.47 | 2026-10-05 | 0.02 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.5200 | 4.02% | 106.06% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 121.0043 | 24.47% | 53.51% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Bitcoin | 85 644.0158 | 13.24% | 33.60% | -6.86% |
| Ethereum | 2 697.6551 | 12.33% | 32.45% | -5.78% |
| US 5Y Treasury Yield | 5.0600 | 11.95% | 20.14% | -1.65% |
| US 10Y Treasury Yield | 5.3100 | 11.32% | 16.95% | -2.70% |
| Nasdaq Composite | 27 477.3100 | 3.36% | 14.29% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6600 | 7.81% | 13.21% | -1.49% |
| Dow Jones | 51 267.9000 | -4.50% | 10.57% | -6.34% |
| S&P 500 | 7 773.9500 | 0.34% | 10.52% | -3.42% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
