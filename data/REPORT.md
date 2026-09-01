# Moneys Monitor - Report di mercato

Generato: `2026-09-01T11:15:38+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-01T11:15:00+00:00` (309 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.33% | 0.00% | **-0.33 pp** |
| 1w | 0.20% | 0.00% | **0.20 pp** |
| 1m | 7.69% | 7.11% | **0.58 pp** |
| 3m | 17.89% | 14.50% | **3.39 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.44% | | Petrolio WTI | -1.87% |
| 2 | US 5Y Treasury Yield | 2.28% | | Bitcoin | -1.07% |
| 3 | US 10Y Treasury Yield | 1.28% | | Solana | -1.02% |
| 4 | Indice dollaro Fed (broad) | 0.58% | | Ethereum | -0.71% |
| 5 | US 30Y Treasury Yield | 0.58% | | Dow Jones | -0.70% |
| 6 | USD/JPY | 0.47% | | GBP/USD | -0.62% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 3.97% | | Petrolio Brent | -6.60% |
| 2 | Nasdaq Composite | 0.73% | | Petrolio WTI | -5.02% |
| 3 | USD/JPY | 0.67% | | VIX (volatilita) | -4.63% |
| 4 | S&P 500 | 0.15% | | Bitcoin | -1.82% |
| 5 | Gas naturale | 0.14% | | Ethereum | -1.00% |
| 6 | FTSE MIB | 0.00% | | EUR/USD | -0.70% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 32.56% | | VIX (volatilita) | -3.15% |
| 2 | Ethereum | 27.89% | | CAC 40 Francia | -3.01% |
| 3 | Bitcoin | 19.80% | | FTSE MIB | -1.83% |
| 4 | Petrolio Brent | 10.64% | | Dow Jones | -1.57% |
| 5 | Petrolio WTI | 9.76% | | Shanghai Composite | -1.28% |
| 6 | Argento (spot) | 7.55% | | Nasdaq Composite | -1.20% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.023 | -0.92% | 19.80% | **-20.72 pp** |
| S&P 500 vs Oro (spot) | 0.091 | -0.92% | 6.67% | **-7.59 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.072 | 1.50% | 6.67% | **-5.17 pp** |
| S&P 500 vs VIX (volatilita) | -0.726 | -0.92% | -3.15% | **2.23 pp** |
| EUR/USD vs Indice dollaro DXY | 0.034 | 0.30% | -0.64% | **0.94 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 6.67% | 7.55% | **-0.88 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | -0.92% | -1.20% | **0.28 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-07-01 | 0.00 |
| CPI USA (indice) | 332.81 | 2026-07-01 | 0.24 |
| CPI Core USA (indice) | 336.79 | 2026-07-01 | 0.72 |
| Disoccupazione USA | 4.10 | 2026-07-01 | -0.10 |
| Occupati non agricoli USA (000) | 158 858.00 | 2026-07-01 | -23.00 |
| US 2Y Treasury Rate | 4.34 | 2026-08-28 | 0.14 |
| US 10Y Treasury Rate | 4.73 | 2026-08-28 | 0.06 |
| US 30Y Treasury Rate | 5.22 | 2026-08-28 | 0.03 |
| Spread 10Y-2Y USA | 0.41 | 2026-08-31 | 0.02 |
| Bund Germania 10Y | 2.97 | 2026-06-01 | -0.08 |
| BTP Italia 10Y | 3.73 | 2026-06-01 | -0.10 |
| HICP Eurozona (indice) | 103.22 | 2026-07-01 | 0.22 |

Curva USA: 10Y-2Y **39.0 bp**, 30Y-10Y **49.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.4300 | -3.15% | 61.11% | -31.03% |
| Ethereum | 2 453.6635 | 27.89% | 52.03% | -5.78% |
| Solana | 102.2442 | 32.56% | 43.01% | -13.59% |
| Bitcoin | 77 957.6604 | 19.80% | 39.03% | -5.72% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Argento (spot) | 68.2900 | 7.55% | 25.93% | -11.21% |
| Oro (spot) | 4 693.0000 | 6.67% | 17.99% | -4.96% |
| Nikkei 225 | 65 856.4300 | 0.38% | 17.09% | -12.83% |
| Bovespa Brasile | 172 458.6200 | -0.03% | 12.37% | -6.51% |
| Hang Seng | 25 511.1000 | -0.61% | 11.80% | -3.43% |
| US 10Y Treasury Yield | 4.7300 | 1.50% | 11.54% | -2.70% |
| Shanghai Composite | 3 889.4450 | -1.28% | 10.98% | -8.47% |
| Rame | 6.6680 | 1.17% | 10.72% | -4.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
