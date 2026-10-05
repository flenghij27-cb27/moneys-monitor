# Moneys Monitor - Report di mercato

Generato: `2026-10-05T22:21:10+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-05T22:20:37+00:00` (424 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.34% | 0.00% | **0.34 pp** |
| 1w | 0.75% | 0.00% | **0.75 pp** |
| 1m | 4.10% | 0.00% | **4.10 pp** |
| 3m | 17.79% | 16.23% | **1.57 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | VIX (volatilita) | -6.59% |
| 2 | Nasdaq Composite | 1.19% | | Petrolio Brent | -0.81% |
| 3 | US 5Y Treasury Yield | 1.00% | | Petrolio WTI | -0.26% |
| 4 | Indice dollaro Fed (broad) | 0.88% | | EUR/USD | -0.19% |
| 5 | Bitcoin | 0.86% | | GBP/USD | -0.12% |
| 6 | US 10Y Treasury Yield | 0.76% | | Solana | -0.06% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | GBP/USD | -2.37% |
| 2 | Petrolio WTI | 16.80% | | EUR/USD | -1.53% |
| 3 | Gas naturale | 13.86% | | USD/JPY | -1.35% |
| 4 | VIX (volatilita) | 7.74% | | Dow Jones | -0.41% |
| 5 | Solana | 2.98% | | S&P 500 | -0.27% |
| 6 | Bitcoin | 2.84% | | FTSE MIB | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -4.50% |
| 2 | Solana | 18.49% | | EUR/USD | -3.60% |
| 3 | Petrolio WTI | 16.87% | | GBP/USD | -2.02% |
| 4 | Gas naturale | 14.55% | | USD/JPY | -0.95% |
| 5 | US 5Y Treasury Yield | 11.45% | | FTSE MIB | 0.00% |
| 6 | US 10Y Treasury Yield | 10.23% | | Euro Stoxx 50 | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.075 | 10.23% | 0.00% | **10.23 pp** |
| S&P 500 vs Bitcoin | -0.076 | 0.73% | 10.00% | **-9.27 pp** |
| S&P 500 vs VIX (volatilita) | 0.138 | 0.73% | 6.10% | **-5.37 pp** |
| EUR/USD vs Indice dollaro DXY | 0.096 | -3.60% | 0.00% | **-3.60 pp** |
| S&P 500 vs Nasdaq Composite | 0.949 | 0.73% | 3.71% | **-2.98 pp** |
| S&P 500 vs Oro (spot) | -0.158 | 0.73% | 0.00% | **0.73 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.83 | 2026-10-02 | 0.05 |
| US 10Y Treasury Rate | 5.28 | 2026-10-02 | 0.04 |
| US 30Y Treasury Rate | 5.63 | 2026-10-02 | 0.02 |
| Spread 10Y-2Y USA | 0.47 | 2026-10-05 | 0.02 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **45.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.3100 | 6.10% | 111.31% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 121.4914 | 18.49% | 53.23% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Bitcoin | 85 992.6850 | 10.00% | 33.38% | -6.86% |
| Ethereum | 2 718.8669 | 8.06% | 32.06% | -5.78% |
| US 5Y Treasury Yield | 5.0600 | 11.45% | 20.04% | -1.65% |
| US 10Y Treasury Yield | 5.2800 | 10.23% | 16.99% | -2.70% |
| Nasdaq Composite | 27 190.8600 | 3.71% | 13.99% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6300 | 6.83% | 13.36% | -1.49% |
| Dow Jones | 51 267.9000 | -4.50% | 10.57% | -6.34% |
| S&P 500 | 7 722.7200 | 0.73% | 10.35% | -3.42% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
