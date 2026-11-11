# Moneys Monitor - Report di mercato

Generato: `2026-11-11T22:31:20+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-11T22:30:20+00:00` (539 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.12% | 0.00% | **0.12 pp** |
| 1w | -1.70% | 0.00% | **-1.70 pp** |
| 1m | -6.36% | 0.00% | **-6.36 pp** |
| 3m | -4.71% | 0.00% | **-4.71 pp** |
| 6m | 4.36% | 10.40% | **-6.04 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Solana | 1.19% | | Petrolio Brent | -13.05% |
| 2 | US 5Y Treasury Yield | 0.65% | | Gas naturale | -4.71% |
| 3 | Ethereum | 0.62% | | Petrolio WTI | -3.61% |
| 4 | Bitcoin | 0.55% | | VIX (volatilita) | -2.31% |
| 5 | USD/JPY | 0.48% | | EUR/USD | -0.78% |
| 6 | US 10Y Treasury Yield | 0.41% | | Nasdaq Composite | -0.74% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio WTI | 3.62% | | Gas naturale | -17.30% |
| 2 | GBP/USD | 1.04% | | Ethereum | -7.15% |
| 3 | Dow Jones | 0.86% | | VIX (volatilita) | -6.58% |
| 4 | Indice dollaro Fed (broad) | 0.41% | | Solana | -6.29% |
| 5 | USD/JPY | 0.27% | | Petrolio Brent | -6.08% |
| 6 | FTSE MIB | 0.00% | | Bitcoin | -2.07% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 27.94% | | Solana | -22.24% |
| 2 | Petrolio WTI | 20.92% | | Ethereum | -17.70% |
| 3 | Petrolio Brent | 20.91% | | Bitcoin | -12.25% |
| 4 | Dow Jones | 0.74% | | Nasdaq Composite | -7.82% |
| 5 | FTSE MIB | 0.00% | | US 10Y Treasury Yield | -6.51% |
| 6 | Euro Stoxx 50 | 0.00% | | US 5Y Treasury Yield | -6.41% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | 0.040 | -3.60% | 27.94% | **-31.54 pp** |
| S&P 500 vs Bitcoin | 0.010 | -3.60% | -12.25% | **8.65 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.086 | -6.51% | 0.00% | **-6.51 pp** |
| S&P 500 vs Nasdaq Composite | 0.019 | -3.60% | -7.82% | **4.22 pp** |
| S&P 500 vs Oro (spot) | 0.039 | -3.60% | 0.00% | **-3.60 pp** |
| EUR/USD vs Indice dollaro DXY | -0.129 | -0.55% | 0.00% | **-0.55 pp** |
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
| VIX (volatilita) | 19.4600 | 27.94% | 302.84% | -31.22% |
| Petrolio Brent | 107.0300 | 20.91% | 127.06% | -21.50% |
| Petrolio WTI | 99.6400 | 20.92% | 78.60% | -18.71% |
| Gas naturale | 2.6300 | -3.77% | 74.14% | -19.84% |
| Ethereum | 2 069.4684 | -17.70% | 43.01% | -25.77% |
| Solana | 84.3181 | -22.24% | 33.17% | -31.76% |
| Nasdaq Composite | 25 065.8700 | -7.82% | 30.68% | -11.90% |
| Bitcoin | 74 248.8162 | -12.25% | 27.84% | -14.85% |
| S&P 500 | 7 520.9300 | -3.60% | 23.18% | -5.95% |
| Dow Jones | 52 231.8900 | 0.74% | 20.56% | -6.34% |
| US 5Y Treasury Yield | 4.6700 | -6.41% | 19.14% | -9.82% |
| US 10Y Treasury Yield | 4.8800 | -6.51% | 17.24% | -8.85% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| US 30Y Treasury Yield | 5.2600 | -6.07% | 14.01% | -7.41% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
