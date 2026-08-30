# Moneys Monitor - Report di mercato

Generato: `2026-08-30T16:13:33+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-08-30T16:12:59+00:00` (304 snapshot, 30 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.19% | 0.00% | **0.19 pp** |
| 1w | 1.84% | -0.76% | **2.60 pp** |
| 1m | 9.41% | 6.97% | **2.44 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 7.79% | | Petrolio WTI | -1.87% |
| 2 | Gas naturale | 3.44% | | Petrolio Brent | -0.57% |
| 3 | Ethereum | 1.25% | | Nasdaq Composite | -0.52% |
| 4 | Solana | 0.76% | | US 10Y Treasury Yield | -0.49% |
| 5 | Bitcoin | 0.70% | | S&P 500 | -0.25% |
| 6 | US 5Y Treasury Yield | 0.23% | | Dow Jones | -0.02% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 11.94% | | Petrolio Brent | -6.60% |
| 2 | VIX (volatilita) | 3.37% | | Petrolio WTI | -5.02% |
| 3 | Bitcoin | 1.96% | | US 10Y Treasury Yield | -1.92% |
| 4 | Ethereum | 1.83% | | Hang Seng | -1.92% |
| 5 | Rame | 1.23% | | Argento (spot) | -1.78% |
| 6 | Bovespa Brasile | 1.18% | | Shanghai Composite | -0.40% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 44.02% | | CAC 40 Francia | -3.01% |
| 2 | Ethereum | 29.79% | | FTSE MIB | -1.83% |
| 3 | Bitcoin | 21.36% | | Dow Jones | -1.45% |
| 4 | Petrolio Brent | 10.64% | | Shanghai Composite | -1.28% |
| 5 | Petrolio WTI | 9.76% | | Euro Stoxx 50 | -0.96% |
| 6 | Argento (spot) | 7.25% | | Russell 2000 | -0.90% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs Bitcoin | -0.280 | -0.15% | 21.36% | **-21.51 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.139 | -0.28% | 6.69% | **-6.97 pp** |
| S&P 500 vs Oro (spot) | -0.065 | -0.15% | 6.69% | **-6.84 pp** |
| S&P 500 vs VIX (volatilita) | 0.037 | -0.15% | 4.97% | **-5.12 pp** |
| EUR/USD vs Indice dollaro DXY | -0.116 | 0.84% | -0.65% | **1.49 pp** |
| Petrolio WTI vs Petrolio Brent | 0.984 | 9.76% | 10.64% | **-0.88 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 6.69% | 7.25% | **-0.56 pp** |
| S&P 500 vs Nasdaq Composite | 0.954 | -0.15% | 0.15% | **-0.30 pp** |

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
| Ethereum | 2 484.9184 | 29.79% | 51.96% | -5.78% |
| Bitcoin | 78 774.0255 | 21.36% | 38.88% | -5.72% |
| Solana | 106.3896 | 44.02% | 38.51% | -13.59% |
| Petrolio Brent | 87.7400 | 10.64% | 32.54% | -21.50% |
| Gas naturale | 2.7930 | 4.53% | 30.21% | -18.87% |
| Petrolio WTI | 82.3300 | 9.76% | 29.67% | -18.71% |
| Argento (spot) | 68.2900 | 7.25% | 28.87% | -11.21% |
| Nikkei 225 | 65 856.4300 | 0.38% | 18.73% | -12.83% |
| Oro (spot) | 4 693.0000 | 6.69% | 18.18% | -4.96% |
| Hang Seng | 25 511.1000 | -0.61% | 12.46% | -3.43% |
| Bovespa Brasile | 172 458.6200 | -0.03% | 12.40% | -6.51% |
| Shanghai Composite | 3 889.4450 | -1.28% | 11.32% | -8.47% |
| Rame | 6.6680 | 1.37% | 10.94% | -4.19% |
| US 10Y Treasury Yield | 4.6470 | -0.28% | 10.77% | -2.70% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
