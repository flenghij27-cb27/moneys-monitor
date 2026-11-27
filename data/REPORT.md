# Moneys Monitor - Report di mercato

Generato: `2026-11-27T03:43:53+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-27T03:43:18+00:00` (581 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.65% | 0.00% | **0.65 pp** |
| 1w | -0.04% | 0.00% | **-0.04 pp** |
| 1m | -7.68% | 0.00% | **-7.68 pp** |
| 3m | -11.88% | 0.00% | **-11.88 pp** |
| 6m | -1.85% | 13.65% | **-15.50 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.45% | | Petrolio WTI | -8.14% |
| 2 | Solana | 3.14% | | Petrolio Brent | -1.23% |
| 3 | Ethereum | 2.65% | | US 5Y Treasury Yield | -1.05% |
| 4 | Bitcoin | 1.86% | | VIX (volatilita) | -0.98% |
| 5 | Indice dollaro Fed (broad) | 0.77% | | GBP/USD | -0.82% |
| 6 | EUR/USD | 0.37% | | USD/JPY | -0.73% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 6.45% | | Petrolio WTI | -23.77% |
| 2 | Solana | 3.79% | | Petrolio Brent | -20.33% |
| 3 | VIX (volatilita) | 3.53% | | US 5Y Treasury Yield | -4.29% |
| 4 | Indice dollaro Fed (broad) | 1.81% | | Nasdaq Composite | -3.77% |
| 5 | Bitcoin | 1.05% | | US 10Y Treasury Yield | -3.73% |
| 6 | USD/JPY | 0.48% | | US 30Y Treasury Yield | -2.93% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 43.34% | | Ethereum | -22.44% |
| 2 | Gas naturale | 18.53% | | Solana | -19.00% |
| 3 | Petrolio Brent | 0.87% | | Bitcoin | -18.88% |
| 4 | FTSE MIB | 0.00% | | Nasdaq Composite | -9.32% |
| 5 | Euro Stoxx 50 | 0.00% | | S&P 500 | -7.17% |
| 6 | Nikkei 225 | 0.00% | | Dow Jones | -4.19% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.230 | -7.17% | 43.34% | **-50.51 pp** |
| S&P 500 vs Bitcoin | 0.021 | -7.17% | -18.88% | **11.71 pp** |
| S&P 500 vs Oro (spot) | 0.008 | -7.17% | 0.00% | **-7.17 pp** |
| Petrolio WTI vs Petrolio Brent | 0.778 | -2.28% | 0.87% | **-3.15 pp** |
| S&P 500 vs Nasdaq Composite | 0.657 | -7.17% | -9.32% | **2.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.091 | -1.80% | 0.00% | **-1.80 pp** |
| EUR/USD vs Indice dollaro DXY | 0.019 | -1.42% | 0.00% | **-1.42 pp** |
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
| Solana | 72.8856 | -19.00% | 61.43% | -44.65% |
| Ethereum | 1 728.5821 | -22.44% | 51.67% | -41.49% |
| Bitcoin | 61 503.9638 | -18.88% | 40.49% | -32.79% |
| S&P 500 | 7 201.0900 | -7.17% | 32.63% | -11.62% |
| Nasdaq Composite | 23 585.8000 | -9.32% | 31.29% | -14.54% |
| Dow Jones | 50 182.9500 | -4.19% | 26.10% | -11.41% |
| US 5Y Treasury Yield | 4.6900 | -2.70% | 23.90% | -9.82% |
| US 10Y Treasury Yield | 4.9100 | -1.80% | 18.45% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.3000 | -0.56% | 13.66% | -7.41% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
