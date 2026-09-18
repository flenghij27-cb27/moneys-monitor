# Moneys Monitor - Report di mercato

Generato: `2026-09-18T10:43:52+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-18T10:43:21+00:00` (367 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 1.30% | 0.00% | **1.30 pp** |
| 1w | 1.25% | 0.00% | **1.25 pp** |
| 1m | 0.55% | 0.00% | **0.55 pp** |
| 3m | 10.00% | 16.43% | **-6.44 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | USD/JPY | -1.54% |
| 2 | Petrolio WTI | 10.03% | | EUR/USD | -0.49% |
| 3 | Gas naturale | 5.69% | | US 30Y Treasury Yield | -0.19% |
| 4 | Solana | 4.98% | | FTSE MIB | 0.00% |
| 5 | VIX (volatilita) | 2.97% | | Euro Stoxx 50 | 0.00% |
| 6 | Ethereum | 2.84% | | Nikkei 225 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | USD/JPY | -3.32% |
| 2 | Petrolio WTI | 25.85% | | EUR/USD | -1.16% |
| 3 | VIX (volatilita) | 7.59% | | GBP/USD | -0.76% |
| 4 | Solana | 6.97% | | Dow Jones | -0.55% |
| 5 | Gas naturale | 5.51% | | FTSE MIB | 0.00% |
| 6 | US 5Y Treasury Yield | 5.42% | | Euro Stoxx 50 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | Dow Jones | -3.15% |
| 2 | Petrolio WTI | 36.89% | | USD/JPY | -2.56% |
| 3 | VIX (volatilita) | 19.10% | | EUR/USD | -1.70% |
| 4 | Gas naturale | 11.57% | | S&P 500 | -0.91% |
| 5 | US 10Y Treasury Yield | 7.67% | | FTSE MIB | 0.00% |
| 6 | Ethereum | 3.14% | | Euro Stoxx 50 | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.569 | -0.91% | 19.10% | **-20.01 pp** |
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.113 | 7.67% | 0.00% | **7.67 pp** |
| EUR/USD vs Indice dollaro DXY | -0.019 | -1.70% | 0.00% | **-1.70 pp** |
| S&P 500 vs Bitcoin | 0.002 | -0.91% | 0.53% | **-1.44 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | -0.91% | 0.33% | **-1.24 pp** |
| S&P 500 vs Oro (spot) | -0.173 | -0.91% | 0.00% | **-0.91 pp** |
| Oro (spot) vs Argento (spot) | 0.875 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.74 | 2026-09-16 | 0.07 |
| US 10Y Treasury Rate | 5.01 | 2026-09-16 | 0.01 |
| US 30Y Treasury Rate | 5.35 | 2026-09-16 | -0.01 |
| Spread 10Y-2Y USA | 0.27 | 2026-09-17 | 0.00 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **27.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| VIX (volatilita) | 17.7100 | 19.10% | 89.31% | -31.03% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Solana | 106.4501 | 2.41% | 45.77% | -13.59% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| Ethereum | 2 514.7974 | 3.14% | 35.11% | -5.78% |
| Bitcoin | 78 155.4454 | 0.53% | 29.57% | -6.86% |
| US 5Y Treasury Yield | 4.8600 | n/d | 14.67% | -0.66% |
| Nasdaq Composite | 26 418.3000 | 0.33% | 12.98% | -7.00% |
| US 10Y Treasury Yield | 5.0100 | 7.67% | 11.94% | -2.70% |
| USD/JPY | 153.7100 | -2.56% | 11.68% | -6.19% |
| Dow Jones | 51 778.0400 | -3.15% | 11.28% | -5.31% |
| S&P 500 | 7 637.7600 | -0.91% | 9.41% | -3.42% |
| US 30Y Treasury Yield | 5.3500 | n/d | 8.68% | -0.57% |
| GBP/USD | 1.3524 | 0.25% | 3.59% | -1.82% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
