# Moneys Monitor - Report di mercato

Generato: `2026-09-24T11:16:59+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-24T11:16:29+00:00` (388 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.55% | 0.00% | **-0.55 pp** |
| 1w | 1.12% | 0.00% | **1.12 pp** |
| 1m | 2.14% | 0.00% | **2.14 pp** |
| 3m | 12.21% | 15.23% | **-3.03 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | USD/JPY | 2.06% | | Petrolio Brent | -12.16% |
| 2 | Indice dollaro Fed (broad) | 1.10% | | Petrolio WTI | -9.91% |
| 3 | FTSE MIB | 0.00% | | VIX (volatilita) | -4.44% |
| 4 | Euro Stoxx 50 | 0.00% | | Gas naturale | -2.36% |
| 5 | Nikkei 225 | 0.00% | | Solana | -1.32% |
| 6 | Oro (spot) | 0.00% | | Ethereum | -1.25% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 30.20% | | VIX (volatilita) | -17.38% |
| 2 | Petrolio WTI | 14.91% | | GBP/USD | -1.91% |
| 3 | Gas naturale | 7.41% | | USD/JPY | -1.43% |
| 4 | Nasdaq Composite | 3.69% | | US 30Y Treasury Yield | -1.31% |
| 5 | Bitcoin | 2.77% | | EUR/USD | -1.09% |
| 6 | Solana | 2.19% | | US 10Y Treasury Yield | -0.80% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 37.51% | | VIX (volatilita) | -6.08% |
| 2 | Petrolio WTI | 23.32% | | Dow Jones | -3.31% |
| 3 | Solana | 9.11% | | EUR/USD | -2.19% |
| 4 | Gas naturale | 8.94% | | GBP/USD | -0.89% |
| 5 | Ethereum | 6.10% | | USD/JPY | -0.55% |
| 6 | US 10Y Treasury Yield | 4.69% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 23.32% | 37.51% | **-14.19 pp** |
| S&P 500 vs VIX (volatilita) | -0.534 | 0.41% | -6.08% | **6.49 pp** |
| US 10Y Treasury Yield vs Oro (spot) | 0.042 | 4.69% | 0.00% | **4.69 pp** |
| S&P 500 vs Nasdaq Composite | 0.952 | 0.41% | 2.89% | **-2.48 pp** |
| S&P 500 vs Bitcoin | -0.009 | 0.41% | 2.86% | **-2.45 pp** |
| EUR/USD vs Indice dollaro DXY | 0.107 | -2.19% | 0.00% | **-2.19 pp** |
| S&P 500 vs Oro (spot) | -0.088 | 0.41% | 0.00% | **0.41 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.71 | 2026-09-22 | -0.05 |
| US 10Y Treasury Rate | 4.96 | 2026-09-22 | 0.00 |
| US 30Y Treasury Rate | 5.29 | 2026-09-22 | 0.00 |
| Spread 10Y-2Y USA | 0.26 | 2026-09-23 | 0.01 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **25.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| Petrolio Brent | 114.8900 | 37.51% | 103.66% | -21.50% |
| VIX (volatilita) | 14.2100 | -6.08% | 100.28% | -31.22% |
| Petrolio WTI | 96.4100 | 23.32% | 71.17% | -18.71% |
| Solana | 113.3627 | 9.11% | 60.34% | -13.59% |
| Ethereum | 2 649.3855 | 6.10% | 40.33% | -5.78% |
| Gas naturale | 2.9000 | 8.94% | 38.49% | -18.87% |
| Bitcoin | 83 520.7863 | 2.86% | 38.13% | -6.86% |
| US 5Y Treasury Yield | 4.8300 | n/d | 17.00% | -1.65% |
| Nasdaq Composite | 26 936.0400 | 2.89% | 15.49% | -7.00% |
| US 10Y Treasury Yield | 4.9600 | 4.69% | 14.14% | -2.70% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| S&P 500 | 7 706.0300 | 0.41% | 11.05% | -3.42% |
| Dow Jones | 51 511.5900 | -3.31% | 11.05% | -5.31% |
| US 30Y Treasury Yield | 5.2900 | n/d | 10.49% | -1.49% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
