# Moneys Monitor - Report di mercato

Generato: `2026-11-10T14:28:53+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-10T14:28:22+00:00` (535 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -1.03% | 0.00% | **-1.03 pp** |
| 1w | -2.22% | 0.00% | **-2.22 pp** |
| 1m | -6.02% | 0.00% | **-6.02 pp** |
| 3m | -5.23% | 0.00% | **-5.23 pp** |
| 6m | 5.09% | 10.40% | **-5.31 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Nasdaq Composite | 2.74% | | Petrolio Brent | -13.05% |
| 2 | Dow Jones | 2.15% | | VIX (volatilita) | -9.01% |
| 3 | US 5Y Treasury Yield | 1.09% | | Gas naturale | -4.71% |
| 4 | USD/JPY | 0.48% | | S&P 500 | -4.36% |
| 5 | US 10Y Treasury Yield | 0.41% | | Petrolio WTI | -3.61% |
| 6 | EUR/USD | 0.25% | | Ethereum | -3.28% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 32.03% | | Gas naturale | -17.30% |
| 2 | Petrolio WTI | 3.62% | | Ethereum | -7.64% |
| 3 | GBP/USD | 1.04% | | Solana | -6.98% |
| 4 | Dow Jones | 0.78% | | Petrolio Brent | -6.08% |
| 5 | Indice dollaro Fed (broad) | 0.41% | | S&P 500 | -5.04% |
| 6 | Nasdaq Composite | 0.35% | | Bitcoin | -2.92% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 66.39% | | Solana | -20.66% |
| 2 | Petrolio WTI | 20.92% | | Ethereum | -15.29% |
| 3 | Petrolio Brent | 20.91% | | Bitcoin | -10.57% |
| 4 | Dow Jones | 1.42% | | Nasdaq Composite | -8.30% |
| 5 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -7.95% |
| 6 | Euro Stoxx 50 | 0.00% | | US 5Y Treasury Yield | -7.75% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.119 | -5.41% | 66.39% | **-71.80 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.085 | -7.95% | 0.00% | **-7.95 pp** |
| S&P 500 vs Oro (spot) | 0.029 | -5.41% | 0.00% | **-5.41 pp** |
| S&P 500 vs Bitcoin | -0.009 | -5.41% | -10.57% | **5.16 pp** |
| S&P 500 vs Nasdaq Composite | -0.294 | -5.41% | -8.30% | **2.89 pp** |
| EUR/USD vs Indice dollaro DXY | -0.005 | -0.12% | 0.00% | **-0.12 pp** |
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
| Ethereum | 2 061.9171 | -15.29% | 45.34% | -25.59% |
| Solana | 83.7086 | -20.66% | 33.22% | -31.44% |
| Nasdaq Composite | 25 253.1400 | -8.30% | 30.88% | -11.90% |
| Bitcoin | 73 662.9902 | -10.57% | 30.12% | -15.05% |
| S&P 500 | 7 353.7300 | -5.41% | 20.66% | -5.95% |
| Dow Jones | 52 389.7500 | 1.42% | 20.57% | -6.34% |
| US 5Y Treasury Yield | 4.6400 | -7.75% | 19.11% | -9.82% |
| US 10Y Treasury Yield | 4.8600 | -7.95% | 17.23% | -8.85% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| US 30Y Treasury Yield | 5.2600 | -7.23% | 14.01% | -7.41% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
