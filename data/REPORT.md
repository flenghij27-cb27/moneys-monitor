# Moneys Monitor - Report di mercato

Generato: `2026-11-18T15:16:14+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-18T15:15:41+00:00` (559 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.89% | 0.00% | **-0.89 pp** |
| 1w | -2.55% | 0.00% | **-2.55 pp** |
| 1m | -8.75% | 0.00% | **-8.75 pp** |
| 3m | -8.03% | 0.00% | **-8.03 pp** |
| 6m | 0.21% | 17.52% | **-17.30 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.91% |
| 2 | VIX (volatilita) | 11.13% | | Petrolio WTI | -10.06% |
| 3 | USD/JPY | 1.07% | | Ethereum | -2.77% |
| 4 | Indice dollaro Fed (broad) | 0.63% | | Bitcoin | -2.16% |
| 5 | FTSE MIB | 0.00% | | S&P 500 | -1.92% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -1.64% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 30.83% | | Petrolio Brent | -26.55% |
| 2 | US 5Y Treasury Yield | 6.25% | | Ethereum | -7.89% |
| 3 | US 10Y Treasury Yield | 5.35% | | Petrolio WTI | -6.88% |
| 4 | US 30Y Treasury Yield | 3.80% | | Bitcoin | -6.86% |
| 5 | USD/JPY | 1.00% | | Solana | -6.07% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Nasdaq Composite | -2.94% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 38.07% | | Solana | -27.51% |
| 2 | Gas naturale | 9.77% | | Ethereum | -24.57% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -21.54% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -8.93% |
| 5 | US 30Y Treasury Yield | 0.55% | | S&P 500 | -4.98% |
| 6 | USD/JPY | 0.42% | | GBP/USD | -2.37% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.145 | -4.98% | 38.07% | **-43.05 pp** |
| S&P 500 vs Bitcoin | -0.007 | -4.98% | -21.54% | **16.56 pp** |
| S&P 500 vs Oro (spot) | 0.013 | -4.98% | 0.00% | **-4.98 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | -0.263 | -4.98% | -8.93% | **3.95 pp** |
| EUR/USD vs Indice dollaro DXY | 0.056 | -2.20% | 0.00% | **-2.20 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.017 | 0.39% | 0.00% | **0.39 pp** |
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
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 25.4600 | 38.07% | 300.12% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Ethereum | 1 772.9751 | -24.57% | 45.91% | -36.02% |
| Solana | 73.9857 | -27.51% | 45.78% | -41.42% |
| Bitcoin | 63 550.7915 | -21.54% | 33.97% | -26.72% |
| Nasdaq Composite | 24 328.3800 | -8.93% | 31.92% | -11.90% |
| US 5Y Treasury Yield | 4.9300 | 0.41% | 24.53% | -9.82% |
| S&P 500 | 7 416.5900 | -4.98% | 24.25% | -5.95% |
| Dow Jones | 50 759.4200 | -2.32% | 21.29% | -6.60% |
| US 10Y Treasury Yield | 5.1200 | 0.39% | 20.80% | -8.85% |
| US 30Y Treasury Yield | 5.4600 | 0.55% | 15.76% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
