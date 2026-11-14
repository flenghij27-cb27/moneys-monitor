# Moneys Monitor - Report di mercato

Generato: `2026-11-14T01:35:58+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-14T01:35:25+00:00` (546 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.25% | 0.00% | **-0.25 pp** |
| 1w | -2.24% | 0.00% | **-2.24 pp** |
| 1m | -6.71% | 0.00% | **-6.71 pp** |
| 3m | -6.72% | 0.00% | **-6.72 pp** |
| 6m | 3.37% | 13.36% | **-9.99 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 14.07% | | Petrolio Brent | -13.91% |
| 2 | VIX (volatilita) | 6.92% | | Petrolio WTI | -10.06% |
| 3 | US 5Y Treasury Yield | 2.91% | | Solana | -1.83% |
| 4 | US 10Y Treasury Yield | 2.41% | | S&P 500 | -0.40% |
| 5 | US 30Y Treasury Yield | 1.50% | | Nasdaq Composite | -0.39% |
| 6 | USD/JPY | 0.48% | | EUR/USD | -0.26% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | US 5Y Treasury Yield | 5.54% | | VIX (volatilita) | -33.64% |
| 2 | Nasdaq Composite | 4.32% | | Petrolio Brent | -26.55% |
| 3 | US 10Y Treasury Yield | 4.08% | | Solana | -10.66% |
| 4 | US 30Y Treasury Yield | 2.84% | | Ethereum | -9.56% |
| 5 | S&P 500 | 2.83% | | Bitcoin | -9.35% |
| 6 | Dow Jones | 2.07% | | Petrolio WTI | -6.88% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 10.85% | | Solana | -24.02% |
| 2 | Gas naturale | 9.77% | | Ethereum | -17.74% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -15.31% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -6.90% |
| 5 | Dow Jones | 0.33% | | S&P 500 | -3.15% |
| 6 | FTSE MIB | 0.00% | | US 30Y Treasury Yield | -2.34% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.629 | -3.15% | 10.85% | **-14.00 pp** |
| S&P 500 vs Bitcoin | -0.008 | -3.15% | -15.31% | **12.16 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.778 | -3.15% | -6.90% | **3.75 pp** |
| S&P 500 vs Oro (spot) | 0.037 | -3.15% | 0.00% | **-3.15 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.025 | -2.11% | 0.00% | **-2.11 pp** |
| EUR/USD vs Indice dollaro DXY | -0.008 | -1.39% | 0.00% | **-1.39 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.86 | 2026-11-12 | 0.13 |
| US 10Y Treasury Rate | 5.10 | 2026-11-12 | 0.12 |
| US 30Y Treasury Rate | 5.43 | 2026-11-12 | 0.08 |
| Spread 10Y-2Y USA | 0.27 | 2026-11-13 | 0.03 |
| Bund Germania 10Y | 3.47 | 2026-09-01 | 0.28 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.10 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **24.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 18.7000 | 10.85% | 304.75% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Ethereum | 1 927.8859 | -17.74% | 45.46% | -30.54% |
| Solana | 77.3229 | -24.02% | 34.97% | -36.67% |
| Bitcoin | 68 219.9555 | -15.31% | 33.35% | -21.33% |
| Nasdaq Composite | 25 366.0900 | -6.90% | 31.50% | -11.90% |
| US 5Y Treasury Yield | 4.9500 | -1.00% | 25.08% | -9.82% |
| S&P 500 | 7 561.6700 | -3.15% | 23.65% | -5.95% |
| US 10Y Treasury Yield | 5.1000 | -2.11% | 21.32% | -8.85% |
| Dow Jones | 52 347.5500 | 0.33% | 20.28% | -6.34% |
| US 30Y Treasury Yield | 5.4300 | -2.34% | 16.58% | -7.41% |
| USD/JPY | 158.2300 | -0.67% | 14.17% | -6.19% |
| Indice dollaro Fed (broad) | 121.8803 | n/d | 7.72% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
