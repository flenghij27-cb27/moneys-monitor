# Moneys Monitor - Report di mercato

Generato: `2026-09-03T10:49:36+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-03T10:49:03+00:00` (315 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.17% | 0.00% | **0.17 pp** |
| 1w | -0.86% | 0.00% | **-0.86 pp** |
| 1m | 7.40% | 5.61% | **1.79 pp** |
| 3m | 13.68% | 16.18% | **-2.49 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 11.11% | | GBP/USD | -0.62% |
| 2 | VIX (volatilita) | 9.52% | | EUR/USD | -0.10% |
| 3 | Petrolio Brent | 9.44% | | FTSE MIB | 0.00% |
| 4 | Gas naturale | 3.83% | | Euro Stoxx 50 | 0.00% |
| 5 | US 5Y Treasury Yield | 1.34% | | Nikkei 225 | 0.00% |
| 6 | US 10Y Treasury Yield | 0.84% | | Oro (spot) | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 5.08% | | Solana | -5.33% |
| 2 | VIX (volatilita) | 4.48% | | Ethereum | -2.57% |
| 3 | Gas naturale | 3.17% | | Bitcoin | -0.94% |
| 4 | US 10Y Treasury Yield | 3.08% | | EUR/USD | -0.86% |
| 5 | Petrolio Brent | 1.73% | | Dow Jones | -0.73% |
| 6 | USD/JPY | 0.67% | | GBP/USD | -0.65% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 31.71% | | CAC 40 Francia | -3.01% |
| 2 | Ethereum | 27.28% | | FTSE MIB | -1.81% |
| 3 | Bitcoin | 21.82% | | Dow Jones | -1.80% |
| 4 | Petrolio WTI | 21.65% | | Nasdaq Composite | -1.77% |
| 5 | Petrolio Brent | 20.57% | | Nikkei 225 | -1.66% |
| 6 | VIX (volatilita) | 9.66% | | Euro Stoxx 50 | -1.37% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.011 | -1.17% | 21.82% | **-22.99 pp** |
| S&P 500 vs VIX (volatilita) | -0.688 | -1.17% | 9.66% | **-10.83 pp** |
| S&P 500 vs Oro (spot) | 0.092 | -1.17% | 5.95% | **-7.12 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.076 | 2.79% | 5.95% | **-3.16 pp** |
| Petrolio WTI vs Petrolio Brent | 0.982 | 21.65% | 20.57% | **1.08 pp** |
| EUR/USD vs Indice dollaro DXY | 0.032 | 0.14% | -0.86% | **1.00 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 5.95% | 5.26% | **0.69 pp** |
| S&P 500 vs Nasdaq Composite | 0.953 | -1.17% | -1.77% | **0.60 pp** |

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
| Ethereum | 2 391.0951 | 27.28% | 53.79% | -5.78% |
| Petrolio WTI | 91.4800 | 21.65% | 47.81% | -18.71% |
| Solana | 99.9664 | 31.71% | 45.31% | -13.59% |
| Petrolio Brent | 96.0200 | 20.57% | 44.72% | -21.50% |
| Bitcoin | 77 492.9898 | 21.82% | 39.31% | -5.72% |
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
