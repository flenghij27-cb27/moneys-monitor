# Moneys Monitor - Report di mercato

Generato: `2026-11-17T23:23:07+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-17T23:22:33+00:00` (557 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.07% | 0.00% | **0.07 pp** |
| 1w | -3.12% | 0.00% | **-3.12 pp** |
| 1m | -8.09% | 0.00% | **-8.09 pp** |
| 3m | -7.38% | 0.00% | **-7.38 pp** |
| 6m | 0.81% | 13.79% | **-12.98 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 18.70% | | Petrolio Brent | -13.91% |
| 2 | Gas naturale | 14.07% | | Petrolio WTI | -10.06% |
| 3 | Solana | 4.80% | | Nasdaq Composite | -2.49% |
| 4 | USD/JPY | 1.07% | | S&P 500 | -1.92% |
| 5 | Indice dollaro Fed (broad) | 0.63% | | Dow Jones | -1.64% |
| 6 | Ethereum | 0.21% | | GBP/USD | -1.19% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.01% | | Petrolio Brent | -26.55% |
| 2 | US 5Y Treasury Yield | 6.25% | | Ethereum | -9.49% |
| 3 | US 10Y Treasury Yield | 5.35% | | Bitcoin | -9.11% |
| 4 | US 30Y Treasury Yield | 3.80% | | Solana | -7.87% |
| 5 | USD/JPY | 1.00% | | Petrolio WTI | -6.88% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Nasdaq Composite | -2.94% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 14.61% | | Solana | -25.80% |
| 2 | Gas naturale | 9.77% | | Ethereum | -22.43% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -19.47% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -8.18% |
| 5 | US 30Y Treasury Yield | 0.55% | | S&P 500 | -4.98% |
| 6 | USD/JPY | 0.42% | | GBP/USD | -2.37% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.020 | -4.98% | 14.61% | **-19.59 pp** |
| S&P 500 vs Bitcoin | -0.038 | -4.98% | -19.47% | **14.49 pp** |
| S&P 500 vs Oro (spot) | -0.069 | -4.98% | 0.00% | **-4.98 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.082 | -4.98% | -8.18% | **3.20 pp** |
| EUR/USD vs Indice dollaro DXY | 0.057 | -2.10% | 0.00% | **-2.10 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.059 | 0.39% | 0.00% | **0.39 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.83 | 2026-11-16 | -0.05 |
| US 10Y Treasury Rate | 5.12 | 2026-11-16 | -0.03 |
| US 30Y Treasury Rate | 5.46 | 2026-11-16 | -0.01 |
| Spread 10Y-2Y USA | 0.30 | 2026-11-17 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 22.9100 | 14.61% | 300.43% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Solana | 74.9546 | -25.80% | 48.02% | -41.42% |
| Ethereum | 1 823.5172 | -22.43% | 46.57% | -34.33% |
| Bitcoin | 64 954.2687 | -19.47% | 34.12% | -25.20% |
| Nasdaq Composite | 24 509.7600 | -8.18% | 31.98% | -11.90% |
| US 5Y Treasury Yield | 4.9300 | 0.41% | 24.53% | -9.82% |
| S&P 500 | 7 416.5900 | -4.98% | 24.25% | -5.95% |
| Dow Jones | 50 759.4200 | -2.32% | 21.29% | -6.60% |
| US 10Y Treasury Yield | 5.1200 | 0.39% | 20.80% | -8.85% |
| US 30Y Treasury Yield | 5.4600 | 0.55% | 15.76% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
