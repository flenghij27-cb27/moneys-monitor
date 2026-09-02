# Moneys Monitor - Report di mercato

Generato: `2026-09-02T23:29:24+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-02T23:28:48+00:00` (314 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.30% | 0.00% | **-0.30 pp** |
| 1w | -0.67% | 0.00% | **-0.67 pp** |
| 1m | 7.12% | 4.57% | **2.55 pp** |
| 3m | 12.78% | 16.34% | **-3.55 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | Ethereum | -1.21% |
| 2 | VIX (volatilita) | 9.52% | | Nasdaq Composite | -1.03% |
| 3 | Petrolio Brent | 9.44% | | S&P 500 | -0.71% |
| 4 | Gas naturale | 3.83% | | GBP/USD | -0.62% |
| 5 | US 5Y Treasury Yield | 1.34% | | Bitcoin | -0.17% |
| 6 | US 10Y Treasury Yield | 0.84% | | EUR/USD | -0.10% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | Solana | -3.90% |
| 2 | VIX (volatilita) | 4.48% | | Ethereum | -2.21% |
| 3 | Gas naturale | 3.17% | | EUR/USD | -0.86% |
| 4 | US 10Y Treasury Yield | 3.08% | | Bitcoin | -0.75% |
| 5 | Petrolio Brent | 1.73% | | Dow Jones | -0.73% |
| 6 | USD/JPY | 0.67% | | GBP/USD | -0.65% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 30.98% | | CAC 40 Francia | -3.14% |
| 2 | Ethereum | 26.97% | | Nasdaq Composite | -2.21% |
| 3 | Petrolio WTI | 21.65% | | Shanghai Composite | -1.94% |
| 4 | Petrolio Brent | 20.57% | | Dow Jones | -1.80% |
| 5 | Bitcoin | 20.46% | | FTSE MIB | -1.74% |
| 6 | VIX (volatilita) | 9.66% | | Nikkei 225 | -1.66% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.011 | -1.63% | 20.46% | **-22.09 pp** |
| S&P 500 vs VIX (volatilita) | 0.005 | -1.63% | 9.66% | **-11.29 pp** |
| S&P 500 vs Oro (spot) | 0.094 | -1.63% | 5.52% | **-7.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.033 | 2.79% | 5.52% | **-2.73 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.52% | 3.63% | **1.89 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| EUR/USD vs Indice dollaro DXY | -0.119 | 0.14% | -0.86% | **1.00 pp** |
| S&P 500 vs Nasdaq Composite | 0.953 | -1.63% | -2.21% | **0.58 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.39 | 2026-09-01 | 0.05 |
| US 10Y Treasury Rate | 4.79 | 2026-09-01 | 0.04 |
| US 30Y Treasury Rate | 5.27 | 2026-09-01 | 0.02 |
| Spread 10Y-2Y USA | 0.40 | 2026-09-02 | 0.00 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **40.0 bp**, 30Y-10Y **48.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.3400 | 9.66% | 69.77% | -31.03% |
| Ethereum | 2 384.4283 | 26.97% | 53.78% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 99.8956 | 30.98% | 45.33% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 77 160.0960 | 20.46% | 39.50% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 3.63% | 25.12% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.52% | 17.84% | -4.96% |
| Nikkei 225 | 65 856.4300 | -1.66% | 17.09% | -12.83% |
| US 5Y Treasury Yield | 4.5500 | n/d | 15.76% | 0.00% |
| US 10Y Treasury Yield | 4.7900 | 2.79% | 11.60% | -2.70% |
| Hang Seng | 25 511.1000 | -1.64% | 11.17% | -3.43% |
| Nasdaq Composite | 26 099.7700 | -2.21% | 10.96% | -7.00% |
| Rame | 6.6680 | 0.53% | 10.72% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
