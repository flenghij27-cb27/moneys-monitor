# Moneys Monitor - Report di mercato

Generato: `2026-11-26T03:42:31+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-26T03:41:55+00:00` (579 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 1.12% | 0.00% | **1.12 pp** |
| 1w | -0.60% | 0.00% | **-0.60 pp** |
| 1m | -8.38% | 0.00% | **-8.38 pp** |
| 3m | -12.01% | 0.00% | **-12.01 pp** |
| 6m | -2.63% | 15.23% | **-17.86 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.45% | | Petrolio WTI | -8.14% |
| 2 | Solana | 4.97% | | Petrolio Brent | -1.23% |
| 3 | Bitcoin | 3.98% | | US 5Y Treasury Yield | -1.05% |
| 4 | Ethereum | 3.37% | | VIX (volatilita) | -0.98% |
| 5 | Indice dollaro Fed (broad) | 0.77% | | GBP/USD | -0.82% |
| 6 | Dow Jones | 0.33% | | USD/JPY | -0.73% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.45% | | Petrolio WTI | -23.77% |
| 2 | VIX (volatilita) | 3.53% | | Petrolio Brent | -20.33% |
| 3 | Indice dollaro Fed (broad) | 1.81% | | Nasdaq Composite | -5.58% |
| 4 | Solana | 0.64% | | US 5Y Treasury Yield | -4.29% |
| 5 | USD/JPY | 0.48% | | US 10Y Treasury Yield | -3.73% |
| 6 | Ethereum | 0.46% | | US 30Y Treasury Yield | -2.93% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 43.34% | | Ethereum | -24.18% |
| 2 | Gas naturale | 18.53% | | Solana | -21.17% |
| 3 | Petrolio Brent | 0.87% | | Bitcoin | -20.13% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -11.12% |
| 5 | Euro Stoxx 50 | 0.00% | | S&P 500 | -7.17% |
| 6 | Nikkei 225 | 0.00% | | Dow Jones | -4.19% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.230 | -7.17% | 43.34% | **-50.51 pp** |
| S&P 500 vs Bitcoin | 0.030 | -7.17% | -20.13% | **12.96 pp** |
| S&P 500 vs Oro (spot) | 0.030 | -7.17% | 0.00% | **-7.17 pp** |
| S&P 500 vs Nasdaq Composite | -0.106 | -7.17% | -11.12% | **3.95 pp** |
| Petrolio WTI vs Petrolio Brent | 0.778 | -2.28% | 0.87% | **-3.15 pp** |
| EUR/USD vs Indice dollaro DXY | 0.018 | -1.93% | 0.00% | **-1.93 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.116 | -1.80% | 0.00% | **-1.80 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.63 | 2026-11-24 | 0.00 |
| US 10Y Treasury Rate | 4.91 | 2026-11-24 | -0.01 |
| US 30Y Treasury Rate | 5.30 | 2026-11-24 | 0.01 |
| Spread 10Y-2Y USA | 0.24 | 2026-11-25 | -0.04 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **28.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 26.3600 | 43.34% | 327.23% | -37.93% |
| Petrolio Brent | 91.8000 | 0.87% | 137.94% | -29.82% |
| Petrolio WTI | 82.2400 | -2.28% | 92.73% | -23.77% |
| Gas naturale | 3.3000 | 18.53% | 91.67% | -19.84% |
| Solana | 70.9436 | -21.17% | 60.08% | -44.65% |
| Ethereum | 1 692.6472 | -24.18% | 50.56% | -41.49% |
| Bitcoin | 60 599.5891 | -20.13% | 39.84% | -32.79% |
| S&P 500 | 7 201.0900 | -7.17% | 32.63% | -11.62% |
| Nasdaq Composite | 23 733.5400 | -11.12% | 31.29% | -14.01% |
| Dow Jones | 50 182.9500 | -4.19% | 26.10% | -11.41% |
| US 5Y Treasury Yield | 4.6900 | -2.70% | 23.90% | -9.82% |
| US 10Y Treasury Yield | 4.9100 | -1.80% | 18.45% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.3000 | -0.56% | 13.66% | -7.41% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
