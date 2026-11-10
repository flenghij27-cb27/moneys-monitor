# Moneys Monitor - Report di mercato

Generato: `2026-11-10T03:43:32+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-10T03:42:57+00:00` (534 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.64% | 0.00% | **-0.64 pp** |
| 1w | -2.34% | 0.00% | **-2.34 pp** |
| 1m | -5.81% | 0.00% | **-5.81 pp** |
| 3m | -4.96% | 0.00% | **-4.96 pp** |
| 6m | 5.88% | 10.40% | **-4.52 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Dow Jones | 2.15% | | Petrolio Brent | -13.05% |
| 2 | Nasdaq Composite | 1.09% | | VIX (volatilita) | -9.01% |
| 3 | US 5Y Treasury Yield | 1.09% | | Gas naturale | -4.71% |
| 4 | USD/JPY | 0.48% | | S&P 500 | -4.36% |
| 5 | US 10Y Treasury Yield | 0.41% | | Petrolio WTI | -3.61% |
| 6 | EUR/USD | 0.25% | | Solana | -1.15% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 32.03% | | Gas naturale | -17.30% |
| 2 | Petrolio WTI | 3.62% | | Nasdaq Composite | -6.13% |
| 3 | GBP/USD | 1.04% | | Petrolio Brent | -6.08% |
| 4 | Dow Jones | 0.78% | | Ethereum | -5.41% |
| 5 | Indice dollaro Fed (broad) | 0.41% | | S&P 500 | -5.04% |
| 6 | USD/JPY | 0.27% | | Solana | -4.92% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 66.39% | | Solana | -18.91% |
| 2 | Petrolio WTI | 20.92% | | Ethereum | -13.25% |
| 3 | Petrolio Brent | 20.91% | | Nasdaq Composite | -10.94% |
| 4 | Dow Jones | 1.42% | | Bitcoin | -9.62% |
| 5 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -7.95% |
| 6 | Euro Stoxx 50 | 0.00% | | US 5Y Treasury Yield | -7.75% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.119 | -5.41% | 66.39% | **-71.80 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.085 | -7.95% | 0.00% | **-7.95 pp** |
| S&P 500 vs Nasdaq Composite | -0.055 | -5.41% | -10.94% | **5.53 pp** |
| S&P 500 vs Oro (spot) | 0.029 | -5.41% | 0.00% | **-5.41 pp** |
| S&P 500 vs Bitcoin | -0.036 | -5.41% | -9.62% | **4.21 pp** |
| EUR/USD vs Indice dollaro DXY | -0.005 | -0.12% | 0.00% | **-0.12 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.51 | 2026-11-06 | 0.05 |
| US 10Y Treasury Rate | 4.86 | 2026-11-06 | 0.02 |
| US 30Y Treasury Rate | 5.26 | 2026-11-06 | 0.01 |
| Spread 10Y-2Y USA | 0.32 | 2026-11-09 | -0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **35.0 bp**, 30Y-10Y **40.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 25.6400 | 66.39% | 287.60% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 111.7077 | -13.25% | 44.50% | -23.79% |
| Solana | 85.5599 | -18.91% | 32.35% | -29.93% |
| Bitcoin | 74 443.3101 | -9.62% | 29.68% | -14.15% |
| Nasdaq Composite | 24 579.4200 | -10.94% | 28.75% | -11.90% |
| S&P 500 | 7 353.7300 | -5.41% | 20.66% | -5.95% |
| Dow Jones | 52 389.7500 | 1.42% | 20.57% | -6.34% |
| US 5Y Treasury Yield | 4.6400 | -7.75% | 19.11% | -9.82% |
| US 10Y Treasury Yield | 4.8600 | -7.95% | 17.23% | -8.85% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| US 30Y Treasury Yield | 5.2600 | -7.23% | 14.01% | -7.41% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
