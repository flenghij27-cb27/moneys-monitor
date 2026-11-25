# Moneys Monitor - Report di mercato

Generato: `2026-11-25T16:54:54+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-25T16:54:20+00:00` (578 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.65% | 0.00% | **-0.65 pp** |
| 1w | -0.98% | 0.00% | **-0.98 pp** |
| 1m | -10.64% | 0.00% | **-10.64 pp** |
| 3m | -12.66% | 0.00% | **-12.66 pp** |
| 6m | -2.56% | 18.74% | **-21.30 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 3.33% | | Solana | -1.94% |
| 2 | Petrolio Brent | 0.87% | | Ethereum | -1.74% |
| 3 | Dow Jones | 0.85% | | Bitcoin | -1.67% |
| 4 | Indice dollaro Fed (broad) | 0.77% | | VIX (volatilita) | -0.98% |
| 5 | US 5Y Treasury Yield | 0.64% | | GBP/USD | -0.82% |
| 6 | FTSE MIB | 0.00% | | USD/JPY | -0.73% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 3.53% | | Petrolio Brent | -26.56% |
| 2 | Indice dollaro Fed (broad) | 1.81% | | Petrolio WTI | -12.15% |
| 3 | Ethereum | 1.00% | | Nasdaq Composite | -5.58% |
| 4 | USD/JPY | 0.48% | | US 10Y Treasury Yield | -3.91% |
| 5 | FTSE MIB | 0.00% | | US 5Y Treasury Yield | -3.85% |
| 6 | Euro Stoxx 50 | 0.00% | | Gas naturale | -3.73% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 43.34% | | Ethereum | -32.30% |
| 2 | Gas naturale | 14.73% | | Solana | -28.56% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -27.29% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -11.12% |
| 5 | FTSE MIB | 0.00% | | S&P 500 | -7.17% |
| 6 | Euro Stoxx 50 | 0.00% | | Dow Jones | -4.47% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.230 | -7.17% | 43.34% | **-50.51 pp** |
| S&P 500 vs Bitcoin | -0.021 | -7.17% | -27.29% | **20.12 pp** |
| S&P 500 vs Oro (spot) | 0.052 | -7.17% | 0.00% | **-7.17 pp** |
| S&P 500 vs Nasdaq Composite | -0.106 | -7.17% | -11.12% | **3.95 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| EUR/USD vs Indice dollaro DXY | 0.028 | -1.93% | 0.00% | **-1.93 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.115 | -0.81% | 0.00% | **-0.81 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.63 | 2026-11-23 | 0.00 |
| US 10Y Treasury Rate | 4.92 | 2026-11-23 | 0.00 |
| US 30Y Treasury Rate | 5.29 | 2026-11-23 | -0.02 |
| Spread 10Y-2Y USA | 0.28 | 2026-11-24 | -0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 26.3600 | 43.34% | 327.23% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Solana | 67.5866 | -28.56% | 55.85% | -44.65% |
| Ethereum | 1 637.5345 | -32.30% | 47.69% | -41.49% |
| Bitcoin | 58 280.0431 | -27.29% | 35.35% | -32.79% |
| S&P 500 | 7 201.0900 | -7.17% | 32.63% | -11.62% |
| Nasdaq Composite | 23 733.5400 | -11.12% | 31.29% | -14.01% |
| Dow Jones | 50 018.7000 | -4.47% | 26.06% | -11.41% |
| US 5Y Treasury Yield | 4.7400 | -0.84% | 23.72% | -9.82% |
| US 10Y Treasury Yield | 4.9200 | -0.81% | 18.45% | -8.85% |
| USD/JPY | 158.7600 | -0.45% | 14.93% | -6.19% |
| US 30Y Treasury Yield | 5.2900 | 0.00% | 13.70% | -7.41% |
| GBP/USD | 1.3104 | -3.25% | 8.35% | -3.99% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
