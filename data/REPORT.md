# Moneys Monitor - Report di mercato

Generato: `2026-11-20T02:29:28+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-20T02:28:53+00:00` (564 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.42% | 0.00% | **-0.42 pp** |
| 1w | -1.88% | 0.00% | **-1.88 pp** |
| 1m | -8.00% | 0.00% | **-8.00 pp** |
| 3m | -10.64% | 0.00% | **-10.64 pp** |
| 6m | -1.93% | 16.43% | **-18.36 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.33% | | VIX (volatilita) | -3.53% |
| 2 | USD/JPY | 1.07% | | Dow Jones | -2.19% |
| 3 | Petrolio Brent | 0.87% | | Solana | -1.67% |
| 4 | Indice dollaro Fed (broad) | 0.63% | | Ethereum | -1.64% |
| 5 | Nasdaq Composite | 0.42% | | GBP/USD | -1.19% |
| 6 | EUR/USD | 0.22% | | Bitcoin | -1.11% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 40.42% | | Petrolio Brent | -26.56% |
| 2 | US 10Y Treasury Yield | 1.81% | | Petrolio WTI | -12.15% |
| 3 | US 5Y Treasury Yield | 1.66% | | Dow Jones | -6.12% |
| 4 | US 30Y Treasury Yield | 1.12% | | Bitcoin | -5.46% |
| 5 | USD/JPY | 1.00% | | Ethereum | -5.24% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Nasdaq Composite | -4.07% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 41.88% | | Solana | -24.30% |
| 2 | Gas naturale | 14.73% | | Ethereum | -22.67% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -20.00% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -7.57% |
| 5 | USD/JPY | 0.42% | | Dow Jones | -7.11% |
| 6 | FTSE MIB | 0.00% | | S&P 500 | -5.43% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.030 | -5.43% | 41.88% | **-47.31 pp** |
| S&P 500 vs Bitcoin | 0.016 | -5.43% | -20.00% | **14.57 pp** |
| S&P 500 vs Oro (spot) | 0.015 | -5.43% | 0.00% | **-5.43 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | -0.035 | -2.15% | 0.00% | **-2.15 pp** |
| S&P 500 vs Nasdaq Composite | 0.087 | -5.43% | -7.57% | **2.14 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.015 | -1.55% | 0.00% | **-1.55 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.80 | 2026-11-18 | 0.00 |
| US 10Y Treasury Rate | 5.07 | 2026-11-18 | -0.03 |
| US 30Y Treasury Rate | 5.41 | 2026-11-18 | -0.05 |
| Spread 10Y-2Y USA | 0.28 | 2026-11-19 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **27.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 24.5600 | 41.88% | 300.09% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Ethereum | 1 730.7447 | -22.67% | 46.65% | -37.54% |
| Solana | 71.8481 | -24.30% | 46.37% | -41.42% |
| Bitcoin | 61 465.1409 | -20.00% | 34.90% | -29.12% |
| Nasdaq Composite | 24 429.8800 | -7.57% | 32.02% | -11.90% |
| US 5Y Treasury Yield | 4.8900 | -1.01% | 24.36% | -9.82% |
| S&P 500 | 7 323.6300 | -5.43% | 24.15% | -6.33% |
| Dow Jones | 49 097.0600 | -7.11% | 22.35% | -9.66% |
| US 10Y Treasury Yield | 5.0700 | -1.55% | 20.40% | -8.85% |
| US 30Y Treasury Yield | 5.4100 | -1.28% | 15.25% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
