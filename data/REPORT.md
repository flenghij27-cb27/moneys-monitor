# Moneys Monitor - Report di mercato

Generato: `2026-11-03T21:34:25+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-03T21:33:37+00:00` (515 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.12% | 0.00% | **0.12 pp** |
| 1w | -0.70% | 0.00% | **-0.70 pp** |
| 1m | -3.54% | 0.00% | **-3.54 pp** |
| 3m | -1.88% | 0.00% | **-1.88 pp** |
| 6m | 15.10% | 14.50% | **0.60 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 8.91% | | Gas naturale | -10.97% |
| 2 | Petrolio Brent | 6.84% | | Petrolio WTI | -4.19% |
| 3 | Solana | 2.23% | | Nasdaq Composite | -3.90% |
| 4 | Ethereum | 1.94% | | US 10Y Treasury Yield | -0.61% |
| 5 | Bitcoin | 1.45% | | US 30Y Treasury Yield | -0.56% |
| 6 | Dow Jones | 0.41% | | S&P 500 | -0.51% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.01% | | Gas naturale | -4.83% |
| 2 | Petrolio WTI | 7.22% | | Nasdaq Composite | -3.05% |
| 3 | Petrolio Brent | 7.15% | | Solana | -2.96% |
| 4 | Ethereum | 1.51% | | US 5Y Treasury Yield | -2.89% |
| 5 | GBP/USD | 1.12% | | US 10Y Treasury Yield | -1.80% |
| 6 | Indice dollaro Fed (broad) | 1.11% | | Bitcoin | -1.45% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -12.44% |
| 2 | VIX (volatilita) | 38.15% | | Ethereum | -8.56% |
| 3 | Petrolio WTI | 25.40% | | Bitcoin | -6.59% |
| 4 | Dow Jones | 1.58% | | Nasdaq Composite | -6.32% |
| 5 | Gas naturale | 1.55% | | US 10Y Treasury Yield | -6.30% |
| 6 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -6.19% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.457 | -1.44% | 38.15% | **-39.59 pp** |
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.020 | -6.30% | 0.00% | **-6.30 pp** |
| S&P 500 vs Bitcoin | -0.109 | -1.44% | -6.59% | **5.15 pp** |
| S&P 500 vs Nasdaq Composite | 0.814 | -1.44% | -6.32% | **4.88 pp** |
| S&P 500 vs Oro (spot) | -0.107 | -1.44% | 0.00% | **-1.44 pp** |
| EUR/USD vs Indice dollaro DXY | 0.031 | -0.22% | 0.00% | **-0.22 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 336.30 | 2026-09-01 | 2.17 |
| CPI Core USA (indice) | 338.90 | 2026-09-01 | 1.13 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.59 | 2026-11-02 | 0.03 |
| US 10Y Treasury Rate | 4.91 | 2026-11-02 | -0.03 |
| US 30Y Treasury Rate | 5.28 | 2026-11-02 | -0.03 |
| Spread 10Y-2Y USA | 0.32 | 2026-11-02 | -0.06 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 21.1500 | 38.15% | 124.65% | -31.22% |
| Petrolio Brent | 123.1000 | 38.92% | 115.48% | -21.50% |
| Petrolio WTI | 103.3700 | 25.40% | 76.78% | -18.71% |
| Gas naturale | 2.7600 | 1.55% | 72.11% | -18.87% |
| Solana | 93.7232 | -12.44% | 32.00% | -24.92% |
| Ethereum | 2 294.2414 | -8.56% | 30.53% | -19.23% |
| Bitcoin | 77 855.4218 | -6.59% | 24.11% | -11.51% |
| Nasdaq Composite | 25 164.3600 | -6.32% | 21.46% | -8.82% |
| US 10Y Treasury Yield | 4.9100 | -6.30% | 16.75% | -7.53% |
| US 5Y Treasury Yield | 4.7000 | -6.19% | 16.63% | -7.66% |
| US 30Y Treasury Yield | 5.2800 | -5.88% | 14.30% | -6.88% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| S&P 500 | 7 541.4000 | -1.44% | 13.40% | -3.55% |
| Dow Jones | 51 983.9800 | 1.58% | 9.91% | -6.34% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
