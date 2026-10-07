# Moneys Monitor - Report di mercato

Generato: `2026-10-07T00:55:09+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-10-07T00:54:35+00:00` (428 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | 0.12% | 0.00% | **0.12 pp** |
| 1w | 0.91% | 0.00% | **0.91 pp** |
| 1m | 5.10% | 0.00% | **5.10 pp** |
| 3m | 16.08% | 15.52% | **0.57 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Gas naturale | 9.66% | | Petrolio Brent | -0.81% |
| 2 | VIX (volatilita) | 1.37% | | Solana | -0.31% |
| 3 | Nasdaq Composite | 1.05% | | Petrolio WTI | -0.26% |
| 4 | Indice dollaro Fed (broad) | 0.88% | | Bitcoin | -0.14% |
| 5 | S&P 500 | 0.58% | | GBP/USD | -0.12% |
| 6 | EUR/USD | 0.58% | | Ethereum | -0.01% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.88% | | VIX (volatilita) | -3.42% |
| 2 | Petrolio WTI | 16.80% | | GBP/USD | -2.37% |
| 3 | Gas naturale | 13.86% | | USD/JPY | -1.35% |
| 4 | Nasdaq Composite | 2.45% | | EUR/USD | -0.76% |
| 5 | Solana | 2.24% | | FTSE MIB | 0.00% |
| 6 | Indice dollaro Fed (broad) | 2.22% | | Euro Stoxx 50 | 0.00% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | Petrolio Brent | 29.68% | | Dow Jones | -3.54% |
| 2 | Solana | 22.34% | | EUR/USD | -3.04% |
| 3 | Petrolio WTI | 16.87% | | GBP/USD | -2.02% |
| 4 | Gas naturale | 14.55% | | USD/JPY | -0.95% |
| 5 | Bitcoin | 12.37% | | FTSE MIB | 0.00% |
| 6 | US 5Y Treasury Yield | 11.95% | | Euro Stoxx 50 | 0.00% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| Petrolio WTI vs Petrolio Brent | 0.949 | 16.87% | 29.68% | **-12.81 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.031 | 11.32% | 0.00% | **11.32 pp** |
| S&P 500 vs Bitcoin | -0.083 | 1.30% | 12.37% | **-11.07 pp** |
| EUR/USD vs Indice dollaro DXY | -0.072 | -3.04% | 0.00% | **-3.04 pp** |
| S&P 500 vs VIX (volatilita) | -0.050 | 1.30% | 4.02% | **-2.72 pp** |
| S&P 500 vs Nasdaq Composite | 0.127 | 1.30% | 3.36% | **-2.06 pp** |
| S&P 500 vs Oro (spot) | -0.160 | 1.30% | 0.00% | **1.30 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.75 | 2026-09-01 | 0.12 |
| CPI USA (indice) | 334.13 | 2026-08-01 | 1.32 |
| CPI Core USA (indice) | 337.76 | 2026-08-01 | 0.98 |
| Disoccupazione USA | 4.20 | 2026-09-01 | 0.10 |
| Occupati non agricoli USA (000) | 159 044.00 | 2026-09-01 | 29.00 |
| US 2Y Treasury Rate | 4.84 | 2026-10-05 | 0.01 |
| US 10Y Treasury Rate | 5.31 | 2026-10-05 | 0.03 |
| US 30Y Treasury Rate | 5.66 | 2026-10-05 | 0.03 |
| Spread 10Y-2Y USA | 0.48 | 2026-10-06 | 0.01 |
| Bund Germania 10Y | 3.18 | 2026-08-01 | 0.11 |
| BTP Italia 10Y | 3.99 | 2026-08-01 | 0.11 |
| HICP Eurozona (indice) | 103.66 | 2026-08-01 | 0.44 |

Curva USA: 10Y-2Y **47.0 bp**, 30Y-10Y **35.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 15.5200 | 4.02% | 106.06% | -31.22% |
| Petrolio Brent | 113.9600 | 29.68% | 104.00% | -21.50% |
| Petrolio WTI | 96.1600 | 16.87% | 71.26% | -18.71% |
| Solana | 120.6308 | 22.34% | 53.31% | -13.59% |
| Gas naturale | 3.1800 | 14.55% | 50.64% | -18.87% |
| Bitcoin | 85 527.0506 | 12.37% | 33.69% | -6.86% |
| Ethereum | 2 697.3625 | 11.62% | 32.43% | -5.78% |
| US 5Y Treasury Yield | 5.0600 | 11.95% | 20.14% | -1.65% |
| US 10Y Treasury Yield | 5.3100 | 11.32% | 16.95% | -2.70% |
| Nasdaq Composite | 27 477.3100 | 3.36% | 14.29% | -7.00% |
| USD/JPY | 157.8100 | -0.95% | 13.67% | -6.19% |
| US 30Y Treasury Yield | 5.6600 | 7.81% | 13.21% | -1.49% |
| S&P 500 | 7 818.9300 | 1.30% | 10.42% | -3.42% |
| Dow Jones | 51 521.2800 | -3.54% | 10.18% | -6.34% |
| Indice dollaro Fed (broad) | 121.3848 | n/d | 9.58% | -0.57% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
