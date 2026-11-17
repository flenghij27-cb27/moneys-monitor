# Moneys Monitor - Report di mercato

Generato: `2026-11-17T04:05:45+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-17T04:05:12+00:00` (555 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.05% | 0.00% | **-0.05 pp** |
| 1w | -2.84% | 0.00% | **-2.84 pp** |
| 1m | -8.22% | 0.00% | **-8.22 pp** |
| 3m | -7.38% | 0.00% | **-7.38 pp** |
| 6m | 0.49% | 13.79% | **-13.30 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.91% |
| 2 | VIX (volatilita) | 3.21% | | Petrolio WTI | -10.06% |
| 3 | Solana | 1.71% | | S&P 500 | -1.92% |
| 4 | USD/JPY | 1.07% | | Dow Jones | -1.41% |
| 5 | US 10Y Treasury Yield | 0.98% | | GBP/USD | -1.19% |
| 6 | US 30Y Treasury Yield | 0.74% | | Nasdaq Composite | -0.91% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | US 5Y Treasury Yield | 8.50% | | Petrolio Brent | -26.55% |
| 2 | US 10Y Treasury Yield | 6.40% | | VIX (volatilita) | -24.73% |
| 3 | US 30Y Treasury Yield | 4.19% | | Solana | -10.58% |
| 4 | Nasdaq Composite | 2.27% | | Ethereum | -9.21% |
| 5 | USD/JPY | 1.00% | | Bitcoin | -9.14% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Petrolio WTI | -6.88% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 17.25% | | Solana | -27.99% |
| 2 | Gas naturale | 9.77% | | Ethereum | -22.18% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -19.50% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -7.60% |
| 5 | USD/JPY | 0.42% | | S&P 500 | -4.98% |
| 6 | FTSE MIB | 0.00% | | GBP/USD | -2.37% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.620 | -4.98% | 17.25% | **-22.23 pp** |
| S&P 500 vs Bitcoin | -0.038 | -4.98% | -19.50% | **14.52 pp** |
| S&P 500 vs Oro (spot) | -0.069 | -4.98% | 0.00% | **-4.98 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.773 | -4.98% | -7.60% | **2.62 pp** |
| EUR/USD vs Indice dollaro DXY | -0.035 | -2.12% | 0.00% | **-2.12 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.018 | -0.77% | 0.00% | **-0.77 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.88 | 2026-11-13 | 0.02 |
| US 10Y Treasury Rate | 5.15 | 2026-11-13 | 0.05 |
| US 30Y Treasury Rate | 5.47 | 2026-11-13 | 0.04 |
| Spread 10Y-2Y USA | 0.29 | 2026-11-16 | 0.02 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **27.0 bp**, 30Y-10Y **32.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 19.3000 | 17.25% | 296.11% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Ethereum | 1 829.2814 | -22.18% | 46.71% | -34.33% |
| Solana | 72.7468 | -27.99% | 43.72% | -41.42% |
| Bitcoin | 64 927.7905 | -19.50% | 34.10% | -25.20% |
| Nasdaq Composite | 25 136.2700 | -7.60% | 31.05% | -11.90% |
| US 5Y Treasury Yield | 4.9800 | -0.40% | 24.28% | -9.82% |
| S&P 500 | 7 416.5900 | -4.98% | 24.25% | -5.95% |
| Dow Jones | 51 608.1700 | -0.76% | 20.92% | -6.34% |
| US 10Y Treasury Yield | 5.1500 | -0.77% | 20.69% | -8.85% |
| US 30Y Treasury Yield | 5.4700 | -0.91% | 15.74% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
