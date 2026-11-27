# Moneys Monitor - Report di mercato

Generato: `2026-11-27T16:17:48+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-27T16:17:16+00:00` (582 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.03% | 0.00% | **-0.03 pp** |
| 1w | -0.74% | 0.00% | **-0.74 pp** |
| 1m | -8.09% | 0.00% | **-8.09 pp** |
| 3m | -12.37% | 0.00% | **-12.37 pp** |
| 6m | -2.64% | 13.65% | **-16.29 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.45% | | Petrolio WTI | -8.14% |
| 2 | Solana | 2.02% | | Petrolio Brent | -1.23% |
| 3 | VIX (volatilita) | 1.67% | | US 5Y Treasury Yield | -1.05% |
| 4 | Indice dollaro Fed (broad) | 0.77% | | GBP/USD | -0.82% |
| 5 | Dow Jones | 0.33% | | Ethereum | -0.80% |
| 6 | US 30Y Treasury Yield | 0.19% | | USD/JPY | -0.73% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 9.12% | | Petrolio WTI | -23.77% |
| 2 | Gas naturale | 6.45% | | Petrolio Brent | -20.33% |
| 3 | Solana | 2.66% | | US 5Y Treasury Yield | -4.29% |
| 4 | Indice dollaro Fed (broad) | 1.81% | | Nasdaq Composite | -3.77% |
| 5 | USD/JPY | 0.48% | | US 10Y Treasury Yield | -3.73% |
| 6 | FTSE MIB | 0.00% | | Ethereum | -2.96% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 52.97% | | Ethereum | -25.05% |
| 2 | Gas naturale | 18.53% | | Bitcoin | -20.90% |
| 3 | Petrolio Brent | 0.87% | | Solana | -19.88% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -9.32% |
| 5 | Euro Stoxx 50 | 0.00% | | S&P 500 | -5.78% |
| 6 | Nikkei 225 | 0.00% | | Dow Jones | -4.19% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.230 | -5.78% | 52.97% | **-58.75 pp** |
| S&P 500 vs Bitcoin | 0.032 | -5.78% | -20.90% | **15.12 pp** |
| S&P 500 vs Oro (spot) | 0.031 | -5.78% | 0.00% | **-5.78 pp** |
| S&P 500 vs Nasdaq Composite | -0.104 | -5.78% | -9.32% | **3.54 pp** |
| Petrolio WTI vs Petrolio Brent | 0.778 | -2.28% | 0.87% | **-3.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.091 | -1.80% | 0.00% | **-1.80 pp** |
| EUR/USD vs Indice dollaro DXY | 0.029 | -1.55% | 0.00% | **-1.55 pp** |
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
| VIX (volatilita) | 26.8000 | 52.97% | 326.22% | -37.93% |
| Petrolio Brent | 91.8000 | 0.87% | 137.94% | -29.82% |
| Petrolio WTI | 82.2400 | -2.28% | 92.73% | -23.77% |
| Gas naturale | 3.3000 | 18.53% | 91.67% | -19.84% |
| Solana | 72.0909 | -19.88% | 60.56% | -44.65% |
| Ethereum | 1 670.4651 | -25.05% | 49.65% | -41.49% |
| Bitcoin | 59 971.4293 | -20.90% | 39.09% | -32.79% |
| S&P 500 | 7 182.7800 | -5.78% | 32.43% | -11.62% |
| Nasdaq Composite | 23 585.8000 | -9.32% | 31.29% | -14.54% |
| Dow Jones | 50 182.9500 | -4.19% | 26.10% | -11.41% |
| US 5Y Treasury Yield | 4.6900 | -2.70% | 23.90% | -9.82% |
| US 10Y Treasury Yield | 4.9100 | -1.80% | 18.45% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.3000 | -0.56% | 13.66% | -7.41% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
