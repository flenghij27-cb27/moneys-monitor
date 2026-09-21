# Moneys Monitor - Report di mercato

Generato: `2026-09-21T20:18:04+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-09-21T20:17:28+00:00` (380 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 1.94% | 0.00% | **1.94 pp** |
| 1w | 4.94% | 0.00% | **4.94 pp** |
| 1m | 3.87% | 0.00% | **3.87 pp** |
| 3m | 16.17% | 19.01% | **-2.84 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 19.44% | | VIX (volatilita) | -4.08% |
| 2 | Petrolio WTI | 10.03% | | GBP/USD | -1.12% |
| 3 | Solana | 7.01% | | Dow Jones | -0.18% |
| 4 | Bitcoin | 6.79% | | FTSE MIB | 0.00% |
| 5 | Gas naturale | 5.69% | | Euro Stoxx 50 | 0.00% |
| 6 | Ethereum | 5.04% | | Nikkei 225 | 0.00% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 42.20% | | VIX (volatilita) | -6.50% |
| 2 | Petrolio WTI | 25.85% | | GBP/USD | -1.91% |
| 3 | Solana | 20.16% | | Dow Jones | -1.69% |
| 4 | Ethereum | 14.67% | | USD/JPY | -1.43% |
| 5 | Bitcoin | 13.94% | | EUR/USD | -0.53% |
| 6 | Gas naturale | 5.51% | | US 30Y Treasury Yield | -0.19% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 56.55% | | VIX (volatilita) | -2.24% |
| 2 | Petrolio WTI | 36.89% | | Dow Jones | -2.04% |
| 3 | Solana | 14.70% | | EUR/USD | -1.61% |
| 4 | Ethereum | 12.13% | | GBP/USD | -0.89% |
| 5 | Gas naturale | 11.57% | | USD/JPY | -0.55% |
| 6 | Bitcoin | 10.04% | | FTSE MIB | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.942 | 36.89% | 56.55% | **-19.66 pp** |
| S&P 500 vs Bitcoin | -0.007 | 0.12% | 10.04% | **-9.92 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.146 | 5.74% | 0.00% | **5.74 pp** |
| S&P 500 vs VIX (volatilita) | -0.190 | 0.12% | -2.24% | **2.36 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 0.12% | 1.75% | **-1.63 pp** |
| EUR/USD vs Indice dollaro DXY | 0.049 | -1.61% | 0.00% | **-1.61 pp** |
| S&P 500 vs Oro (spot) | -0.090 | 0.12% | 0.00% | **0.12 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.63 | 2026-08-01 | 0.00 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.10 | 2026-08-01 | 0.00 |
| Occupati non agricoli USA (000) | 159 075.00 | 2026-08-01 | 162.00 |
| US 2Y Treasury Rate | 4.76 | 2026-09-18 | 0.09 |
| US 10Y Treasury Rate | 5.01 | 2026-09-18 | 0.07 |
| US 30Y Treasury Rate | 5.34 | 2026-09-18 | 0.05 |
| Spread 10Y-2Y USA | 0.25 | 2026-09-18 | -0.02 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **25.0 bp**, 30Y-10Y **33.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 14.8100 | -2.24% | 100.57% | -31.03% |
| Petrolio Brent | 130.8000 | 56.55% | 90.72% | -21.50% |
| Solana | 118.4904 | 14.70% | 60.33% | -13.59% |
| Petrolio WTI | 107.0200 | 36.89% | 60.14% | -18.71% |
| Ethereum | 2 770.9867 | 12.13% | 42.26% | -5.78% |
| Bitcoin | 86 718.0627 | 10.04% | 41.38% | -6.86% |
| Gas naturale | 2.9700 | 11.57% | 39.73% | -18.87% |
| US 5Y Treasury Yield | 4.8600 | n/d | 17.20% | -1.65% |
| USD/JPY | 156.8700 | -0.55% | 14.02% | -6.19% |
| US 10Y Treasury Yield | 5.0100 | 5.74% | 13.84% | -2.70% |
| Nasdaq Composite | 26 522.5500 | 1.75% | 12.97% | -7.00% |
| Indice dollaro Fed (broad) | 119.5133 | n/d | 11.25% | -0.57% |
| Dow Jones | 51 682.6400 | -2.04% | 10.54% | -5.31% |
| US 30Y Treasury Yield | 5.3400 | n/d | 10.21% | -1.49% |
| S&P 500 | 7 650.5000 | 0.12% | 9.29% | -3.42% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
