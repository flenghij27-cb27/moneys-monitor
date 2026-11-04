# Moneys Monitor - Report di mercato

Generato: `2026-11-04T13:54:42+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-04T13:54:06+00:00` (517 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.08% | 0.00% | **0.08 pp** |
| 1w | -0.10% | 0.00% | **-0.10 pp** |
| 1m | -2.62% | 0.00% | **-2.62 pp** |
| 3m | -1.63% | 0.00% | **-1.63 pp** |
| 6m | 13.63% | 16.34% | **-2.70 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 8.91% | | Gas naturale | -10.97% |
| 2 | Petrolio Brent | 6.84% | | Petrolio WTI | -4.19% |
| 3 | Ethereum | 0.97% | | Solana | -0.98% |
| 4 | Nasdaq Composite | 0.83% | | US 10Y Treasury Yield | -0.61% |
| 5 | Bitcoin | 0.50% | | US 30Y Treasury Yield | -0.56% |
| 6 | USD/JPY | 0.38% | | S&P 500 | -0.51% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.01% | | Gas naturale | -4.83% |
| 2 | Petrolio WTI | 7.22% | | Nasdaq Composite | -3.05% |
| 3 | Petrolio Brent | 7.15% | | US 5Y Treasury Yield | -2.89% |
| 4 | Ethereum | 3.51% | | Solana | -2.22% |
| 5 | Bitcoin | 1.84% | | US 10Y Treasury Yield | -1.80% |
| 6 | GBP/USD | 1.12% | | Dow Jones | -1.13% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 38.92% | | Solana | -10.89% |
| 2 | VIX (volatilita) | 38.15% | | US 10Y Treasury Yield | -6.30% |
| 3 | Petrolio WTI | 25.40% | | US 5Y Treasury Yield | -6.19% |
| 4 | Gas naturale | 1.55% | | US 30Y Treasury Yield | -5.88% |
| 5 | Dow Jones | 1.01% | | Nasdaq Composite | -5.58% |
| 6 | FTSE MIB | 0.00% | | Ethereum | -4.24% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.457 | -1.44% | 38.15% | **-39.59 pp** |
| Petrolio WTI vs Petrolio Brent | 0.776 | 25.40% | 38.92% | **-13.52 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.011 | -6.30% | 0.00% | **-6.30 pp** |
| S&P 500 vs Nasdaq Composite | 0.102 | -1.44% | -5.58% | **4.14 pp** |
| S&P 500 vs Bitcoin | 0.122 | -1.44% | -4.10% | **2.66 pp** |
| S&P 500 vs Oro (spot) | -0.014 | -1.44% | 0.00% | **-1.44 pp** |
| EUR/USD vs Indice dollaro DXY | -0.136 | -0.22% | 0.00% | **-0.22 pp** |
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
| Spread 10Y-2Y USA | 0.34 | 2026-11-03 | 0.02 |
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
| Solana | 92.8082 | -10.89% | 31.48% | -24.92% |
| Ethereum | 2 316.5385 | -4.24% | 30.62% | -19.23% |
| Bitcoin | 78 242.1457 | -4.10% | 24.05% | -11.51% |
| Nasdaq Composite | 25 372.0100 | -5.58% | 21.15% | -8.82% |
| US 10Y Treasury Yield | 4.9100 | -6.30% | 16.75% | -7.53% |
| US 5Y Treasury Yield | 4.7000 | -6.19% | 16.63% | -7.66% |
| US 30Y Treasury Yield | 5.2800 | -5.88% | 14.30% | -6.88% |
| USD/JPY | 157.4700 | -1.17% | 14.04% | -6.19% |
| S&P 500 | 7 541.4000 | -1.44% | 13.40% | -3.55% |
| Dow Jones | 51 786.7200 | 1.01% | 9.90% | -6.34% |
| Indice dollaro Fed (broad) | 121.6656 | n/d | 8.11% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
