# Moneys Monitor - Report di mercato

Generato: `2026-08-28T18:18:15+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-08-28T18:17:45+00:00` (298 snapshot, 28 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.03% | 0.00% | **-0.03 pp** |
| 1w | 1.56% | -0.57% | **2.13 pp** |
| 1m | 8.35% | 9.38% | **-1.04 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 7.79% | | Bitcoin | -2.10% |
| 2 | Solana | 5.70% | | Petrolio WTI | -1.87% |
| 3 | Gas naturale | 3.44% | | Ethereum | -1.62% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -1.54% |
| 5 | Euro Stoxx 50 | 0.00% | | S&P 500 | -0.77% |
| 6 | Nikkei 225 | 0.00% | | Petrolio Brent | -0.57% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 13.64% | | Petrolio Brent | -6.60% |
| 2 | VIX (volatilita) | 3.37% | | Petrolio WTI | -5.02% |
| 3 | Rame | 1.34% | | US 10Y Treasury Yield | -1.92% |
| 4 | Bovespa Brasile | 0.84% | | Hang Seng | -1.92% |
| 5 | FTSE 100 UK | 0.65% | | Argento (spot) | -1.54% |
| 6 | DAX Germania | 0.60% | | Shanghai Composite | -0.40% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 40.17% | | Bovespa Brasile | -2.96% |
| 2 | Ethereum | 27.68% | | CAC 40 Francia | -2.50% |
| 3 | Bitcoin | 20.14% | | Dow Jones | -1.65% |
| 4 | Petrolio Brent | 10.64% | | Hang Seng | -1.56% |
| 5 | Petrolio WTI | 9.76% | | FTSE MIB | -1.34% |
| 6 | Argento (spot) | 9.76% | | Rame | -1.18% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.055 | -0.68% | 20.14% | **-20.82 pp** |
| S&P 500 vs Oro (spot) | 0.013 | -0.68% | 9.01% | **-9.69 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.128 | 0.65% | 9.01% | **-8.36 pp** |
| S&P 500 vs VIX (volatilita) | 0.016 | -0.68% | 4.97% | **-5.65 pp** |
| EUR/USD vs Indice dollaro DXY | 0.010 | 0.84% | -0.74% | **1.58 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 9.01% | 9.76% | **-0.75 pp** |
| S&P 500 vs Nasdaq Composite | 0.955 | -0.68% | -0.88% | **0.20 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-07-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.19 | 2026-08-26 | 0.02 |
| US 10Y Treasury Rate | 4.66 | 2026-08-26 | 0.02 |
| US 30Y Treasury Rate | 5.18 | 2026-08-26 | 0.01 |
| Spread 10Y-2Y USA | 0.47 | 2026-08-27 | 0.00 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **52.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.6400 | 4.97% | 67.15% | -31.03% |
| Ethereum | 2 438.3529 | 27.68% | 52.17% | -5.78% |
| Solana | 103.9487 | 40.17% | 39.17% | -13.59% |
| Bitcoin | 77 740.8005 | 20.14% | 39.06% | -5.72% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Argento (spot) | 68.2900 | 9.76% | 29.89% | -11.21% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Oro (spot) | 4 693.0000 | 9.01% | 18.86% | -4.96% |
| Nikkei 225 | 65 856.4300 | -0.67% | 18.74% | -12.83% |
| Bovespa Brasile | 172 458.6200 | -2.96% | 16.19% | -6.51% |
| Rame | 6.6680 | -1.18% | 13.57% | -4.19% |
| Hang Seng | 25 511.1000 | -1.56% | 12.71% | -3.43% |
| Shanghai Composite | 3 889.4450 | 0.28% | 11.95% | -8.47% |
| Nasdaq Composite | 26 131.7620 | -0.88% | 11.59% | -7.00% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
