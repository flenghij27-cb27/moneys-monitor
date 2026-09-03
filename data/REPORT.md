# Moneys Monitor - Report di mercato

Generato: `2026-09-03T19:13:55+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-03T19:13:25+00:00` (317 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 1.69% | 0.00% | **1.69 pp** |
| 1w | 0.61% | 0.00% | **0.61 pp** |
| 1m | 9.32% | 5.61% | **3.71 pp** |
| 3m | 15.81% | 16.18% | **-0.36 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | VIX (volatilita) | -6.98% |
| 2 | Petrolio Brent | 9.44% | | GBP/USD | -0.62% |
| 3 | Ethereum | 5.33% | | FTSE MIB | 0.00% |
| 4 | Solana | 5.32% | | Euro Stoxx 50 | 0.00% |
| 5 | Bitcoin | 5.31% | | Nikkei 225 | 0.00% |
| 6 | Gas naturale | 3.83% | | Oro (spot) | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | Dow Jones | -0.73% |
| 2 | Bitcoin | 3.88% | | GBP/USD | -0.65% |
| 3 | Gas naturale | 3.17% | | Solana | -0.36% |
| 4 | US 10Y Treasury Yield | 3.08% | | EUR/USD | -0.26% |
| 5 | Ethereum | 2.34% | | VIX (volatilita) | -0.07% |
| 6 | Petrolio Brent | 1.73% | | S&P 500 | -0.06% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 38.62% | | CAC 40 Francia | -3.01% |
| 2 | Ethereum | 33.69% | | FTSE MIB | -1.81% |
| 3 | Bitcoin | 27.74% | | Dow Jones | -1.80% |
| 4 | Petrolio WTI | 21.65% | | Nasdaq Composite | -1.77% |
| 5 | Petrolio Brent | 20.57% | | VIX (volatilita) | -1.68% |
| 6 | Gas naturale | 7.77% | | Nikkei 225 | -1.66% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.016 | -1.17% | 27.74% | **-28.91 pp** |
| S&P 500 vs Oro (spot) | 0.092 | -1.17% | 5.95% | **-7.12 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.076 | 2.79% | 5.95% | **-3.16 pp** |
| EUR/USD vs Indice dollaro DXY | -0.115 | 0.61% | -0.86% | **1.47 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.95% | 5.26% | **0.69 pp** |
| S&P 500 vs Nasdaq Composite | 0.953 | -1.17% | -1.77% | **0.60 pp** |
| S&P 500 vs VIX (volatilita) | -0.008 | -1.17% | -1.68% | **0.51 pp** |

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
| VIX (volatilita) | 15.2000 | -1.68% | 74.36% | -31.03% |
| Ethereum | 2 511.4851 | 33.69% | 55.54% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 105.2111 | 38.62% | 47.03% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 81 261.0244 | 27.74% | 42.05% | -5.72% |
| Gas naturale | 2.9000 | 7.77% | 32.58% | -18.87% |
| Argento (spot) | 68.2900 | 5.26% | 25.03% | -11.21% |
| Oro (spot) | 4 693.0000 | 5.95% | 17.74% | -4.96% |
| Nikkei 225 | 65 856.4300 | -1.66% | 16.76% | -12.83% |
| US 5Y Treasury Yield | 4.5500 | n/d | 15.76% | 0.00% |
| US 10Y Treasury Yield | 4.7900 | 2.79% | 11.60% | -2.70% |
| Nasdaq Composite | 26 217.8300 | -1.77% | 11.11% | -7.00% |
| Hang Seng | 25 511.1000 | -0.55% | 10.76% | -3.43% |
| Rame | 6.6680 | 0.59% | 10.63% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
