# Moneys Monitor - Report di mercato

Generato: `2026-11-20T22:32:01+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-20T22:31:26+00:00` (566 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -2.27% | 0.00% | **-2.27 pp** |
| 1w | -3.58% | 0.00% | **-3.58 pp** |
| 1m | -9.39% | 0.00% | **-9.39 pp** |
| 3m | -11.94% | 0.00% | **-11.94 pp** |
| 6m | -3.56% | 16.43% | **-20.00 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.80% | | Ethereum | -7.86% |
| 2 | Gas naturale | 3.33% | | Solana | -5.48% |
| 3 | USD/JPY | 1.07% | | Bitcoin | -5.07% |
| 4 | Petrolio Brent | 0.87% | | Nasdaq Composite | -2.25% |
| 5 | Indice dollaro Fed (broad) | 0.63% | | Dow Jones | -2.19% |
| 6 | FTSE MIB | 0.00% | | S&P 500 | -2.02% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 52.09% | | Petrolio Brent | -26.56% |
| 2 | USD/JPY | 1.00% | | Petrolio WTI | -12.15% |
| 3 | Indice dollaro Fed (broad) | 0.86% | | Ethereum | -11.24% |
| 4 | FTSE MIB | 0.00% | | Bitcoin | -9.24% |
| 5 | Euro Stoxx 50 | 0.00% | | Dow Jones | -6.12% |
| 6 | Nikkei 225 | 0.00% | | Nasdaq Composite | -5.86% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 70.50% | | Ethereum | -27.56% |
| 2 | Gas naturale | 14.73% | | Solana | -27.24% |
| 3 | Petrolio WTI | 5.78% | | Bitcoin | -23.20% |
| 4 | Petrolio Brent | 2.35% | | Nasdaq Composite | -9.63% |
| 5 | USD/JPY | 0.42% | | Dow Jones | -7.11% |
| 6 | FTSE MIB | 0.00% | | S&P 500 | -6.31% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.061 | -6.31% | 70.50% | **-76.81 pp** |
| S&P 500 vs Bitcoin | 0.035 | -6.31% | -23.20% | **16.89 pp** |
| S&P 500 vs Oro (spot) | -0.061 | -6.31% | 0.00% | **-6.31 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 5.78% | 2.35% | **3.43 pp** |
| S&P 500 vs Nasdaq Composite | 0.120 | -6.31% | -9.63% | **3.32 pp** |
| EUR/USD vs Indice dollaro DXY | 0.057 | -1.92% | 0.00% | **-1.92 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.055 | -1.56% | 0.00% | **-1.56 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.76 | 2026-11-19 | -0.04 |
| US 10Y Treasury Rate | 5.04 | 2026-11-19 | -0.03 |
| US 30Y Treasury Rate | 5.40 | 2026-11-19 | -0.01 |
| Spread 10Y-2Y USA | 0.29 | 2026-11-20 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.77 | 2026-10-01 | 0.47 |

Curva USA: 10Y-2Y **28.0 bp**, 30Y-10Y **36.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 28.4400 | 70.50% | 300.96% | -37.93% |
| Petrolio Brent | 92.9400 | 2.35% | 137.81% | -29.56% |
| Gas naturale | 3.1000 | 14.73% | 89.48% | -19.84% |
| Petrolio WTI | 89.5300 | 5.78% | 87.56% | -18.71% |
| Ethereum | 1 621.2546 | -27.56% | 52.22% | -41.49% |
| Solana | 69.0618 | -27.24% | 48.60% | -43.44% |
| Bitcoin | 59 002.7384 | -23.20% | 37.60% | -31.96% |
| Nasdaq Composite | 23 879.2000 | -9.63% | 32.22% | -13.48% |
| S&P 500 | 7 175.8300 | -6.31% | 24.84% | -8.22% |
| US 5Y Treasury Yield | 4.8600 | -1.62% | 24.42% | -9.82% |
| Dow Jones | 49 097.0600 | -7.11% | 22.35% | -9.66% |
| US 10Y Treasury Yield | 5.0400 | -1.56% | 20.47% | -8.85% |
| US 30Y Treasury Yield | 5.4000 | -0.37% | 15.27% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
