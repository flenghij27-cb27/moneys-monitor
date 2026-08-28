# Moneys Monitor - Report di mercato

Generato: `2026-08-28T09:32:55+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-08-28T09:25:49+00:00` (296 snapshot, 28 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.86% | 0.00% | **0.86 pp** |
| 1w | 2.26% | -0.57% | **2.82 pp** |
| 1m | 9.20% | 9.38% | **-0.18 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 8.10% | | Bitcoin | -0.01% |
| 2 | Ethereum | 0.53% | | S&P 500 | 0.00% |
| 3 | S&P 500 | 0.00% | | Dow Jones | 0.00% |
| 4 | Dow Jones | 0.00% | | Nasdaq Composite | 0.00% |
| 5 | Nasdaq Composite | 0.00% | | FTSE MIB | 0.00% |
| 6 | FTSE MIB | 0.00% | | Euro Stoxx 50 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 16.22% | | Petrolio Brent (futures) | -6.60% |
| 2 | VIX (volatilita) | 3.23% | | Petrolio WTI (futures) | -5.02% |
| 3 | Ethereum | 2.58% | | US 10Y Treasury Yield | -1.92% |
| 4 | Bitcoin | 2.54% | | Hang Seng | -1.92% |
| 5 | Rame (futures) | 1.34% | | Argento (futures) | -1.54% |
| 6 | Bovespa Brasile | 0.84% | | Shanghai Composite | -0.40% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 43.35% | | Bovespa Brasile | -2.96% |
| 2 | Ethereum | 30.47% | | CAC 40 Francia | -2.50% |
| 3 | Bitcoin | 22.70% | | Dow Jones | -1.65% |
| 4 | Petrolio Brent (futures) | 10.64% | | Hang Seng | -1.56% |
| 5 | Petrolio WTI (futures) | 9.76% | | FTSE MIB | -1.34% |
| 6 | Argento (futures) | 9.76% | | Rame (futures) | -1.18% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | 0.098 | -0.68% | 22.70% | **-23.38 pp** |
| S&P 500 vs Oro (futures) | 0.104 | -0.68% | 9.01% | **-9.69 pp** |
| US 10Y Treasury Yield vs Oro (futures) | -0.141 | 0.65% | 9.01% | **-8.36 pp** |
| EUR/USD vs Indice dollaro DXY | -0.911 | 1.00% | -0.74% | **1.74 pp** |
| Petrolio WTI (futures) vs Petrolio Brent (futures) | 0.991 | 9.76% | 10.64% | **-0.88 pp** |
| Oro (futures) vs Argento (futures) | 0.875 | 9.01% | 9.76% | **-0.75 pp** |
| S&P 500 vs VIX (volatilita) | -0.743 | -0.68% | -1.08% | **0.40 pp** |
| S&P 500 vs Nasdaq Composite | 0.953 | -0.68% | -0.88% | **0.20 pp** |

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
| VIX (volatilita) | 15.6400 | -1.08% | 61.87% | -31.03% |
| Ethereum | 2 491.6984 | 30.47% | 51.14% | -5.78% |
| Solana | 106.3066 | 43.35% | 43.11% | -13.59% |
| Bitcoin | 79 395.1470 | 22.70% | 37.58% | -5.72% |
| Petrolio Brent (futures) | 87.7400 | 10.64% | 33.42% | -21.50% |
| Petrolio WTI (futures) | 82.3300 | 9.76% | 30.73% | -18.71% |
| Argento (futures) | 68.2900 | 9.76% | 29.89% | -11.21% |
| Gas naturale (futures) | 2.7930 | 4.53% | 23.29% | -18.87% |
| Oro (futures) | 4 693.0000 | 9.01% | 18.86% | -4.96% |
| Nikkei 225 | 65 856.4300 | -0.67% | 18.74% | -12.83% |
| Bovespa Brasile | 172 458.6200 | -2.96% | 16.19% | -6.51% |
| Rame (futures) | 6.6680 | -1.18% | 13.57% | -4.19% |
| Hang Seng | 25 511.1000 | -1.56% | 12.71% | -3.43% |
| Shanghai Composite | 3 889.4450 | 0.28% | 11.95% | -8.47% |
| US 10Y Treasury Yield | 4.6470 | 0.65% | 11.06% | -2.70% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
