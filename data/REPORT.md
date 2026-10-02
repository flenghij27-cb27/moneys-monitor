# Moneys Monitor - Report di mercato

Generato: `2026-10-02T20:24:56+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-02T20:24:26+00:00` (414 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.11% | 0.00% | **-0.11 pp** |
| 1w | -0.49% | 0.00% | **-0.49 pp** |
| 1m | 3.43% | 0.00% | **3.43 pp** |
| 3m | 16.63% | 16.04% | **0.60 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | US 5Y Treasury Yield | -1.57% |
| 2 | Indice dollaro Fed (broad) | 0.68% | | Ethereum | -1.08% |
| 3 | VIX (volatilita) | 0.31% | | US 10Y Treasury Yield | -0.95% |
| 4 | USD/JPY | 0.20% | | GBP/USD | -0.91% |
| 5 | S&P 500 | 0.19% | | Petrolio Brent | -0.81% |
| 6 | Dow Jones | 0.04% | | EUR/USD | -0.65% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | Solana | -3.37% |
| 2 | Petrolio WTI | 16.80% | | GBP/USD | -2.85% |
| 3 | Gas naturale | 13.86% | | EUR/USD | -1.56% |
| 4 | VIX (volatilita) | 10.22% | | USD/JPY | -1.28% |
| 5 | US 30Y Treasury Yield | 2.56% | | Dow Jones | -0.82% |
| 6 | Indice dollaro Fed (broad) | 1.92% | | Ethereum | -0.72% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -3.49% |
| 2 | Petrolio WTI | 16.87% | | EUR/USD | -3.36% |
| 3 | Solana | 15.44% | | GBP/USD | -1.82% |
| 4 | Gas naturale | 14.55% | | USD/JPY | -0.40% |
| 5 | VIX (volatilita) | 12.96% | | FTSE MIB | 0.00% |
| 6 | US 5Y Treasury Yield | 10.11% | | Euro Stoxx 50 | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| S&P 500 vs VIX (volatilita) | 0.156 | 0.46% | 12.96% | **-12.50 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.029 | 9.39% | 0.00% | **9.39 pp** |
| S&P 500 vs Bitcoin | 0.005 | 0.46% | 9.32% | **-8.86 pp** |
| EUR/USD vs Indice dollaro DXY | 0.011 | -3.36% | 0.00% | **-3.36 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 0.46% | 2.96% | **-2.50 pp** |
| S&P 500 vs Oro (spot) | 0.068 | 0.46% | 0.00% | **0.46 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.78 | 2026-10-01 | -0.10 |
| US 10Y Treasury Rate | 5.24 | 2026-10-01 | -0.05 |
| US 30Y Treasury Rate | 5.61 | 2026-10-01 | -0.03 |
| Spread 10Y-2Y USA | 0.46 | 2026-10-01 | 0.05 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **46.0 bp**, 30Y-10Y **37.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 16.3900 | 12.96% | 108.65% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 117.9908 | 15.44% | 59.18% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Ethereum | 2 667.1742 | 6.13% | 38.27% | -5.78% |
| Bitcoin | 84 359.9765 | 9.32% | 36.83% | -6.86% |
| US 5Y Treasury Yield | 5.0100 | 10.11% | 20.29% | -1.65% |
| US 10Y Treasury Yield | 5.2400 | 9.39% | 17.28% | -2.70% |
| Nasdaq Composite | 26 871.6000 | 2.96% | 14.22% | -7.00% |
| US 30Y Treasury Yield | 5.6100 | 6.45% | 13.61% | -1.49% |
| USD/JPY | 157.1800 | -0.40% | 13.58% | -6.19% |
| Dow Jones | 50 926.5600 | -3.49% | 11.39% | -6.34% |
| S&P 500 | 7 666.4500 | 0.46% | 10.72% | -3.42% |
| Indice dollaro Fed (broad) | 120.3300 | n/d | 10.10% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
