# Moneys Monitor - Report di mercato

Generato: `2026-09-02T10:49:32+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-02T10:49:00+00:00` (312 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.68% | 0.00% | **-0.68 pp** |
| 1w | -1.04% | 0.00% | **-1.04 pp** |
| 1m | 6.64% | 4.57% | **2.06 pp** |
| 3m | 12.27% | 16.34% | **-4.07 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.44% | | Ethereum | -2.14% |
| 2 | VIX (volatilita) | 3.40% | | Solana | -1.94% |
| 3 | Indice dollaro Fed (broad) | 0.58% | | Petrolio WTI | -1.87% |
| 4 | US 30Y Treasury Yield | 0.57% | | Nasdaq Composite | -1.03% |
| 5 | USD/JPY | 0.47% | | Bitcoin | -1.02% |
| 6 | US 10Y Treasury Yield | 0.42% | | Dow Jones | -0.79% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | US 10Y Treasury Yield | 0.98% | | Petrolio Brent | -6.60% |
| 2 | USD/JPY | 0.67% | | Solana | -5.85% |
| 3 | Nasdaq Composite | 0.46% | | VIX (volatilita) | -5.81% |
| 4 | Gas naturale | 0.14% | | Petrolio WTI | -5.02% |
| 5 | FTSE MIB | 0.00% | | Ethereum | -3.13% |
| 6 | Euro Stoxx 50 | 0.00% | | Bitcoin | -1.59% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 28.32% | | CAC 40 Francia | -3.14% |
| 2 | Ethereum | 25.78% | | Dow Jones | -2.35% |
| 3 | Bitcoin | 19.44% | | Nasdaq Composite | -2.21% |
| 4 | Petrolio Brent | 10.64% | | Shanghai Composite | -1.94% |
| 5 | Petrolio WTI | 9.76% | | FTSE MIB | -1.74% |
| 6 | Oro (spot) | 5.52% | | Nikkei 225 | -1.66% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.002 | -1.63% | 19.44% | **-21.07 pp** |
| S&P 500 vs Oro (spot) | 0.094 | -1.63% | 5.52% | **-7.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.073 | 1.93% | 5.52% | **-3.59 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.52% | 3.63% | **1.89 pp** |
| S&P 500 vs VIX (volatilita) | -0.727 | -1.63% | 0.13% | **-1.76 pp** |
| EUR/USD vs Indice dollaro DXY | 0.033 | 0.24% | -0.86% | **1.10 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| S&P 500 vs Nasdaq Composite | 0.953 | -1.63% | -2.21% | **0.58 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.34 | 2026-08-31 | 0.00 |
| US 10Y Treasury Rate | 4.75 | 2026-08-31 | 0.02 |
| US 30Y Treasury Rate | 5.25 | 2026-08-31 | 0.03 |
| Spread 10Y-2Y USA | 0.40 | 2026-09-01 | -0.01 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **41.0 bp**, 30Y-10Y **50.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.9200 | 0.13% | 62.35% | -31.03% |
| Ethereum | 2 362.0490 | 25.78% | 54.44% | -5.78% |
| Solana | 97.8660 | 28.32% | 46.68% | -13.59% |
| Bitcoin | 76 502.8682 | 19.44% | 39.95% | -5.72% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Argento (spot) | 68.2900 | 3.63% | 25.12% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.52% | 17.84% | -4.96% |
| Nikkei 225 | 65 856.4300 | -1.66% | 17.09% | -12.83% |
| US 10Y Treasury Yield | 4.7500 | 1.93% | 11.60% | -2.70% |
| Hang Seng | 25 511.1000 | -1.64% | 11.17% | -3.43% |
| Nasdaq Composite | 26 099.7700 | -2.21% | 10.96% | -7.00% |
| Rame | 6.6680 | 0.53% | 10.72% | -4.19% |
| Shanghai Composite | 3 889.4450 | -1.94% | 10.65% | -8.47% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
