# Moneys Monitor - Report di mercato

Generato: `2026-08-29T03:15:25+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-08-29T03:14:50+00:00` (299 snapshot, 30 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.18% | 0.00% | **-0.18 pp** |
| 1w | 1.17% | -0.76% | **1.93 pp** |
| 1m | 8.50% | 9.29% | **-0.80 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 7.79% | | Petrolio WTI | -1.87% |
| 2 | Gas naturale | 3.44% | | Nasdaq Composite | -1.54% |
| 3 | US 5Y Treasury Yield | 0.23% | | Petrolio Brent | -0.57% |
| 4 | US 30Y Treasury Yield | 0.19% | | US 10Y Treasury Yield | -0.49% |
| 5 | Solana | 0.06% | | S&P 500 | -0.25% |
| 6 | Ethereum | 0.03% | | Bitcoin | -0.06% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 9.77% | | Petrolio Brent | -6.60% |
| 2 | VIX (volatilita) | 3.37% | | Petrolio WTI | -5.02% |
| 3 | Rame | 1.23% | | US 10Y Treasury Yield | -1.92% |
| 4 | Bovespa Brasile | 0.83% | | Hang Seng | -1.92% |
| 5 | FTSE 100 UK | 0.65% | | Argento (spot) | -1.78% |
| 6 | DAX Germania | 0.60% | | Shanghai Composite | -0.40% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 40.74% | | CAC 40 Francia | -3.17% |
| 2 | Ethereum | 27.84% | | Bovespa Brasile | -2.96% |
| 3 | Bitcoin | 19.92% | | FTSE MIB | -1.98% |
| 4 | Petrolio Brent | 10.64% | | Dow Jones | -1.45% |
| 5 | Argento (spot) | 9.97% | | Nasdaq Composite | -0.88% |
| 6 | Petrolio WTI | 9.76% | | Rame | -0.85% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.070 | -0.15% | 19.92% | **-20.07 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.128 | -0.28% | 8.62% | **-8.90 pp** |
| S&P 500 vs Oro (spot) | 0.100 | -0.15% | 8.62% | **-8.77 pp** |
| S&P 500 vs VIX (volatilita) | 0.037 | -0.15% | 4.97% | **-5.12 pp** |
| EUR/USD vs Indice dollaro DXY | -0.901 | 0.84% | -0.78% | **1.62 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 8.62% | 9.97% | **-1.35 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| S&P 500 vs Nasdaq Composite | 0.946 | -0.15% | -0.88% | **0.73 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-07-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.20 | 2026-08-27 | 0.01 |
| US 10Y Treasury Rate | 4.67 | 2026-08-27 | 0.01 |
| US 30Y Treasury Rate | 5.19 | 2026-08-27 | 0.01 |
| Spread 10Y-2Y USA | 0.39 | 2026-08-28 | -0.08 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **52.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.6400 | 4.97% | 67.15% | -31.03% |
| Ethereum | 2 439.0818 | 27.84% | 52.26% | -5.78% |
| Bitcoin | 77 691.7826 | 19.92% | 39.13% | -5.72% |
| Solana | 104.0083 | 40.74% | 39.11% | -13.59% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Argento (spot) | 68.2900 | 9.97% | 28.93% | -11.21% |
| Nikkei 225 | 65 856.4300 | 0.26% | 18.73% | -12.83% |
| Oro (spot) | 4 693.0000 | 8.62% | 18.17% | -4.96% |
| Hang Seng | 25 511.1000 | 0.05% | 12.46% | -3.43% |
| Bovespa Brasile | 172 458.6200 | -2.96% | 12.40% | -6.51% |
| Nasdaq Composite | 26 131.7620 | -0.88% | 11.59% | -7.00% |
| Shanghai Composite | 3 889.4450 | -0.28% | 11.32% | -8.47% |
| Rame | 6.6680 | -0.85% | 10.94% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
