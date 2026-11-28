# Moneys Monitor - Report di mercato

Generato: `2026-11-28T15:11:36+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-28T15:11:04+00:00` (584 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.26% | 0.00% | **-0.26 pp** |
| 1w | -1.75% | 0.00% | **-1.75 pp** |
| 1m | -8.19% | 0.00% | **-8.19 pp** |
| 3m | -12.46% | 0.00% | **-12.46 pp** |
| 6m | -1.65% | 16.88% | **-18.53 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.45% | | Petrolio WTI | -8.14% |
| 2 | Nasdaq Composite | 2.31% | | Solana | -2.17% |
| 3 | VIX (volatilita) | 1.67% | | Ethereum | -1.37% |
| 4 | Dow Jones | 1.18% | | Petrolio Brent | -1.23% |
| 5 | Indice dollaro Fed (broad) | 0.77% | | US 10Y Treasury Yield | -1.22% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -1.13% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 9.12% | | Petrolio WTI | -23.77% |
| 2 | Gas naturale | 6.45% | | Petrolio Brent | -20.33% |
| 3 | Dow Jones | 3.42% | | Ethereum | -6.20% |
| 4 | Indice dollaro Fed (broad) | 1.81% | | US 5Y Treasury Yield | -4.91% |
| 5 | USD/JPY | 0.48% | | Solana | -4.68% |
| 6 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -4.34% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 52.97% | | Ethereum | -26.21% |
| 2 | Gas naturale | 18.53% | | Bitcoin | -21.67% |
| 3 | Petrolio Brent | 0.87% | | Solana | -21.25% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -7.03% |
| 5 | Euro Stoxx 50 | 0.00% | | S&P 500 | -5.78% |
| 6 | Nikkei 225 | 0.00% | | US 5Y Treasury Yield | -3.93% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.230 | -5.78% | 52.97% | **-58.75 pp** |
| S&P 500 vs Bitcoin | 0.027 | -5.78% | -21.67% | **15.89 pp** |
| S&P 500 vs Oro (spot) | 0.009 | -5.78% | 0.00% | **-5.78 pp** |
| Petrolio WTI vs Petrolio Brent | 0.778 | -2.28% | 0.87% | **-3.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.093 | -3.00% | 0.00% | **-3.00 pp** |
| EUR/USD vs Indice dollaro DXY | 0.018 | -1.55% | 0.00% | **-1.55 pp** |
| S&P 500 vs Nasdaq Composite | 0.642 | -5.78% | -7.03% | **1.25 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.61 | 2026-11-25 | -0.02 |
| US 10Y Treasury Rate | 4.85 | 2026-11-25 | -0.06 |
| US 30Y Treasury Rate | 5.24 | 2026-11-25 | -0.06 |
| Spread 10Y-2Y USA | 0.25 | 2026-11-27 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **24.0 bp**, 30Y-10Y **39.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 26.8000 | 52.97% | 326.22% | -37.93% |
| Petrolio Brent | 91.8000 | 0.87% | 137.94% | -29.82% |
| Petrolio WTI | 82.2400 | -2.28% | 92.73% | -23.77% |
| Gas naturale | 3.3000 | 18.53% | 91.67% | -19.84% |
| Solana | 70.5252 | -21.25% | 60.61% | -44.65% |
| Ethereum | 1 647.6071 | -26.21% | 49.48% | -41.49% |
| Bitcoin | 59 310.7488 | -21.67% | 38.81% | -32.79% |
| Nasdaq Composite | 24 129.5000 | -7.03% | 32.51% | -14.54% |
| S&P 500 | 7 182.7800 | -5.78% | 32.43% | -11.62% |
| Dow Jones | 50 774.9400 | -3.24% | 26.56% | -11.41% |
| US 5Y Treasury Yield | 4.6500 | -3.93% | 24.01% | -9.82% |
| US 10Y Treasury Yield | 4.8500 | -3.00% | 18.89% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.2400 | -1.32% | 14.23% | -7.58% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
