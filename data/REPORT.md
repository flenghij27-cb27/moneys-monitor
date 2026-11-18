# Moneys Monitor - Report di mercato

Generato: `2026-11-18T03:03:39+00:00`  
Finestra: `2026-06-27T12:45:09.844913+00:00` -> `2026-11-18T03:03:04+00:00` (558 snapshot, 31 asset)

> Le change_pct salvate nello schema v1 sono errate (prev_close congelato). Questo report le ignora e ricalcola tutto dalla serie osservata.


## Appetito al rischio

| Orizzonte | Risk-on medio | Risk-off medio | Spread |
|---|---:|---:|---:|
| 1d | -0.70% | 0.00% | **-0.70 pp** |
| 1w | -2.21% | 0.00% | **-2.21 pp** |
| 1m | -8.40% | 0.00% | **-8.40 pp** |
| 3m | -7.80% | 0.00% | **-7.80 pp** |
| 6m | 0.66% | 17.52% | **-16.85 pp** |

## Outlier 1d

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 18.70% | | Petrolio Brent | -13.91% |
| 2 | Gas naturale | 14.07% | | Petrolio WTI | -10.06% |
| 3 | USD/JPY | 1.07% | | Nasdaq Composite | -2.49% |
| 4 | Indice dollaro Fed (broad) | 0.63% | | S&P 500 | -1.92% |
| 5 | FTSE MIB | 0.00% | | Dow Jones | -1.64% |
| 6 | Euro Stoxx 50 | 0.00% | | GBP/USD | -1.19% |

## Outlier 1w

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 15.01% | | Petrolio Brent | -26.55% |
| 2 | US 5Y Treasury Yield | 6.25% | | Petrolio WTI | -6.88% |
| 3 | US 10Y Treasury Yield | 5.35% | | Ethereum | -6.33% |
| 4 | US 30Y Treasury Yield | 3.80% | | Bitcoin | -5.73% |
| 5 | USD/JPY | 1.00% | | Solana | -5.31% |
| 6 | Indice dollaro Fed (broad) | 0.86% | | Nasdaq Composite | -2.94% |

## Outlier 1m

| # | Migliori | % | | Peggiori | % |
|--:|---|--:|---|---|--:|
| 1 | VIX (volatilita) | 14.61% | | Solana | -26.93% |
| 2 | Gas naturale | 9.77% | | Ethereum | -23.30% |
| 3 | Petrolio WTI | 8.76% | | Bitcoin | -20.59% |
| 4 | Petrolio Brent | 4.09% | | Nasdaq Composite | -8.18% |
| 5 | US 30Y Treasury Yield | 0.55% | | S&P 500 | -4.98% |
| 6 | USD/JPY | 0.42% | | GBP/USD | -2.37% |

## Divergenze principali (1 mese)

| Coppia | Corr. 20g | A | B | Divergenza |
|---|--:|--:|--:|--:|
| S&P 500 vs VIX (volatilita) | -0.020 | -4.98% | 14.61% | **-19.59 pp** |
| S&P 500 vs Bitcoin | -0.019 | -4.98% | -20.59% | **15.61 pp** |
| S&P 500 vs Oro (spot) | 0.013 | -4.98% | 0.00% | **-4.98 pp** |
| Petrolio WTI vs Petrolio Brent | 0.795 | 8.76% | 4.09% | **4.67 pp** |
| S&P 500 vs Nasdaq Composite | 0.082 | -4.98% | -8.18% | **3.20 pp** |
| EUR/USD vs Indice dollaro DXY | -0.036 | -2.10% | 0.00% | **-2.10 pp** |
| US 10Y Treasury Yield vs Oro (spot) | -0.017 | 0.39% | 0.00% | **0.39 pp** |
| Oro (spot) vs Argento (spot) | 0.876 | 0.00% | 0.00% | **0.00 pp** |

## Macro

| Indicatore | Valore | Data | Var. |
|---|--:|---|--:|
| Fed Funds Rate (USA) | 3.88 | 2026-10-01 | 0.13 |
| CPI USA (indice) | 337.48 | 2026-10-01 | 1.18 |
| CPI Core USA (indice) | 339.90 | 2026-10-01 | 1.00 |
| Disoccupazione USA | 4.10 | 2026-10-01 | -0.10 |
| Occupati non agricoli USA (000) | 159 293.00 | 2026-10-01 | 165.00 |
| US 2Y Treasury Rate | 4.83 | 2026-11-16 | -0.05 |
| US 10Y Treasury Rate | 5.12 | 2026-11-16 | -0.03 |
| US 30Y Treasury Rate | 5.46 | 2026-11-16 | -0.01 |
| Spread 10Y-2Y USA | 0.30 | 2026-11-17 | 0.01 |
| Bund Germania 10Y | 3.42 | 2026-10-01 | -0.06 |
| BTP Italia 10Y | 4.68 | 2026-10-01 | 0.32 |
| HICP Eurozona (indice) | 104.29 | 2026-09-01 | 0.63 |

Curva USA: 10Y-2Y **29.0 bp**, 30Y-10Y **34.0 bp**, invertita: **no**


## Volatilita' e drawdown (dalla finestra osservata)

| Asset | Ultimo | 1m | Vol 20g ann. | Max DD |
|---|--:|--:|--:|--:|
| VIX (volatilita) | 22.9100 | 14.61% | 300.43% | -37.93% |
| Petrolio Brent | 92.1400 | 4.09% | 137.80% | -29.56% |
| Gas naturale | 3.0000 | 9.77% | 89.37% | -19.84% |
| Petrolio WTI | 89.6200 | 8.76% | 87.61% | -18.71% |
| Solana | 74.5787 | -26.93% | 45.86% | -41.42% |
| Ethereum | 1 802.9256 | -23.30% | 45.52% | -34.94% |
| Bitcoin | 64 321.8548 | -20.59% | 33.72% | -25.83% |
| Nasdaq Composite | 24 509.7600 | -8.18% | 31.98% | -11.90% |
| US 5Y Treasury Yield | 4.9300 | 0.41% | 24.53% | -9.82% |
| S&P 500 | 7 416.5900 | -4.98% | 24.25% | -5.95% |
| Dow Jones | 50 759.4200 | -2.32% | 21.29% | -6.60% |
| US 10Y Treasury Yield | 5.1200 | 0.39% | 20.80% | -8.85% |
| US 30Y Treasury Yield | 5.4600 | 0.55% | 15.76% | -7.41% |
| USD/JPY | 159.9300 | 0.42% | 14.70% | -6.19% |
| GBP/USD | 1.3212 | -2.37% | 7.98% | -3.19% |

---
*Dati pubblici a scopo informativo. Non e' consulenza finanziaria.*
