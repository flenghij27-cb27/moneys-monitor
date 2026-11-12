# Moneys Monitor - Report di mercato

Generato: `2026-11-12T14:46:42+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-12T14:46:05+00:00` (541 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.80% | 0.00% | **-0.80 pp** |
| 1w | -2.59% | 0.00% | **-2.59 pp** |
| 1m | -5.93% | 0.00% | **-5.93 pp** |
| 3m | -4.99% | 0.00% | **-4.99 pp** |
| 6m | 4.25% | 13.53% | **-9.27 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Nasdaq Composite | 1.60% | | Petrolio Brent | -13.05% |
| 2 | S&P 500 | 1.31% | | VIX (volatilita) | -10.12% |
| 3 | US 5Y Treasury Yield | 0.65% | | Gas naturale | -4.71% |
| 4 | Dow Jones | 0.49% | | Solana | -3.94% |
| 5 | USD/JPY | 0.48% | | Petrolio WTI | -3.61% |
| 6 | US 10Y Treasury Yield | 0.41% | | Bitcoin | -3.54% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 5.30% | | Gas naturale | -17.30% |
| 2 | Petrolio WTI | 3.62% | | Ethereum | -10.54% |
| 3 | GBP/USD | 1.04% | | Solana | -9.56% |
| 4 | S&P 500 | 0.67% | | Petrolio Brent | -6.08% |
| 5 | Indice dollaro Fed (broad) | 0.41% | | Bitcoin | -5.41% |
| 6 | USD/JPY | 0.27% | | Dow Jones | -1.63% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 20.92% | | Solana | -22.24% |
| 2 | Petrolio Brent | 20.91% | | Ethereum | -16.24% |
| 3 | VIX (volatilita) | 14.54% | | Bitcoin | -12.01% |
| 4 | Dow Jones | 1.58% | | Nasdaq Composite | -6.94% |
| 5 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -6.51% |
| 6 | Euro Stoxx 50 | 0.00% | | US 5Y Treasury Yield | -6.41% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.024 | -1.88% | 14.54% | **-16.42 pp** |
| S&P 500 vs Bitcoin | -0.016 | -1.88% | -12.01% | **10.13 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.034 | -6.51% | 0.00% | **-6.51 pp** |
| S&P 500 vs Nasdaq Composite | 0.037 | -1.88% | -6.94% | **5.06 pp** |
| S&P 500 vs Oro (spot) | 0.036 | -1.88% | 0.00% | **-1.88 pp** |
| EUR/USD vs Indice dollaro DXY | -0.006 | -0.55% | 0.00% | **-0.55 pp** |
| Petrolio WTI vs Petrolio Brent | 0.771 | 20.92% | 20.91% | **0.01 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.56 | 2026-11-09 | 0.05 |
| US 10Y Treasury Rate | 4.88 | 2026-11-09 | 0.02 |
| US 30Y Treasury Rate | 5.26 | 2026-11-09 | 0.00 |
| Spread 10Y-2Y USA | 0.25 | 2026-11-10 | -0.07 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **32.0 bp**, 30Y-10Y **38.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 17.4900 | 14.54% | 304.57% | -37.93% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 1 997.6779 | -16.24% | 44.05% | -27.91% |
| Solana | 80.9931 | -22.24% | 34.74% | -33.67% |
| Nasdaq Composite | 25 466.1900 | -6.94% | 31.50% | -11.90% |
| Bitcoin | 71 620.7098 | -12.01% | 29.92% | -17.41% |
| S&P 500 | 7 619.3800 | -1.88% | 23.62% | -5.95% |
| Dow Jones | 52 486.4900 | 1.58% | 20.60% | -6.34% |
| US 5Y Treasury Yield | 4.6700 | -6.41% | 19.14% | -9.82% |
| US 10Y Treasury Yield | 4.8800 | -6.51% | 17.24% | -8.85% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| US 30Y Treasury Yield | 5.2600 | -6.07% | 14.01% | -7.41% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
