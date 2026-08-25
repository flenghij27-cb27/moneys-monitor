# moneys-monitor

Raccolta automatica di dati finanziari pubblici e analisi di un PAC su Trade Republic.
**Solo lettura. Nessun ordine, nessuna connessione al broker, nessuna credenziale.**

---

## Cosa fa

| Script | Cosa produce |
|---|---|
| `scripts/collect.py` | Raccoglie prezzi (Yahoo), macro (FRED), news (RSS). Gira via GitHub Actions. |
| `scripts/analyze.py` | Ricalcola i rendimenti dalla serie osservata, trova outlier e divergenze. |
| `scripts/pac.py` | Analizza il PAC: MWR, TWR, confronto con benchmark, drift, fisco. |
| `scripts/charts.py` | Dashboard HTML con grafici SVG inline, zero dipendenze. |

### File generati in `data/`

| File | Contenuto |
|---|---|
| `latest.json` | Snapshot corrente completo (news incluse) |
| `history.jsonl` | Storico append-only, senza news (~3 KB per riga) |
| `prices.csv` | Serie tidy: 1 riga = 1 ticker x 1 raccolta |
| `prices_daily.csv` | Serie giornaliera per ticker (input di `pac.py`) |
| `news.jsonl` | Notizie deduplicate: ogni titolo scritto una volta sola |
| `analysis.json` / `REPORT.md` | Analisi di mercato |
| `pac_report.json` / `PAC_REPORT.md` | Analisi del PAC |
| `dashboard.html` | Grafici: piccoli multipli, heatmap, rischio/rendimento, drawdown |

---

## Setup

### 1. Chiave FRED (gratuita, per i dati macro)

1. Registrati su <https://fredaccount.stlouisfed.org/apikeys>
2. Repo -> **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**
3. Nome: `FRED_API_KEY`, valore: la tua chiave

Senza chiave i prezzi e le news funzionano lo stesso; manca solo la sezione macro.

### 2. Configura il PAC

```bash
cp pac/config.example.json      pac/config.json
cp pac/transactions.example.csv pac/transactions.csv
```

Poi:

- in `pac/config.json` metti i **tuoi** ETF, ISIN, pesi target e TER;
- assicurati che ogni `ticker` esista anche in `scripts/collect.py` -> `YAHOO_TICKERS`
  (altrimenti manca il prezzo e la posizione non viene valorizzata);
- in `pac/transactions.csv` inserisci le tue operazioni.

> `pac/transactions.csv` e `pac/config.json` sono in `.gitignore`: sono dati personali
> e la repo e' pubblica. Se li vuoi versionare, togli le due righe dal `.gitignore`
> sapendo che diventano visibili a chiunque.

### 3. Da dove prendere le transazioni

Trade Republic **non ha API pubbliche**. Due strade:

1. **App -> Profilo -> Documenti -> Estratti conto**: scarichi il PDF e trascrivi le operazioni.
2. **App -> export CSV** (funzione introdotta da TR): scarichi lo storico e lo riadatti
   alle colonne qui sotto.

In entrambi i casi il file finale deve avere queste colonne:

| Colonna | Obbligatoria | Note |
|---|---|---|
| `date` | si | `2026-08-24`, `24/08/2026` o `24.08.2026` |
| `type` | si | `BUY`, `SELL`, `SAVEBACK`, `DIVIDEND`, `FEE`, `TAX` |
| `isin` | consigliata | identificativo stabile |
| `ticker` | si | deve combaciare con `config.json` e `collect.py` |
| `name` | no | descrizione |
| `quantity` | si per BUY/SELL | quote |
| `price` | si per BUY/SELL | prezzo unitario |
| `fees` | no | commissioni |
| `currency` | no | default EUR |
| `amount_eur` | consigliata | se manca viene calcolata da `quantity x price` |
| `note` | no | libero |

Accetta separatore `,` `;` o tab e numeri in formato italiano (`1.234,56`).

---

## Uso locale

```bash
FRED_API_KEY=xxxx python3 scripts/collect.py   # raccoglie
python3 scripts/analyze.py --top 12            # analisi di mercato
python3 scripts/charts.py                      # dashboard.html
python3 scripts/pac.py                         # report PAC a schermo
python3 scripts/analyze.py --backfill          # ricostruisce prices_daily.csv dallo storico
```

Nessuna dipendenza esterna: solo libreria standard di Python 3.9+.

---

## Le metriche del PAC, in breve

**MWR (XIRR)** — il rendimento del *tuo* capitale. Tiene conto di **quando** hai versato:
se hai versato molto poco prima di un rialzo, il MWR sale. E' la metrica che risponde a
"quanto ho guadagnato io".

**TWR** — il rendimento dello *strumento*, neutro rispetto ai versamenti. Risponde a
"come e' andato il portafoglio", ed e' l'unico numero confrontabile con un indice.

I due divergono sempre in un PAC. Se MWR > TWR hai versato nei momenti giusti; se
MWR < TWR hai versato nei momenti sbagliati. Non e' bravura: e' quasi sempre caso.

**Confronto con benchmark** — prende i tuoi versamenti reali, alle date reali, e li mette
tutti su un solo ETF. Risponde alla sola domanda che conta: *il mio mix e' servito a
qualcosa, rispetto a comprare e basta un World?*

**Ribilanciamento senza vendere** — vendere in guadagno costa il 26%. Se sei fuori target,
la mossa efficiente e' indirizzare i **prossimi versamenti** sugli strumenti sottopesati.
Il report calcola le percentuali esatte.

---

## Fisco (Italia) — sintesi operativa

- Trade Republic e' **sostituto d'imposta in Italia dal 30 gennaio 2025** per i conti con
  IBAN italiano: applica il regime amministrato e trattiene le imposte alla fonte.
  I conti con vecchio IBAN tedesco (DE) restano in regime dichiarativo.
- Plusvalenze e dividendi da ETF UCITS: **26%**. Titoli di Stato white list: **12,5%**.
- Cripto: **33%** sui realizzi dal 1 gennaio 2026 (era 26% fino al 2025).
- **Imposta di bollo titoli: 0,20% annuo** sul controvalore del dossier.
- **Asimmetria da conoscere**: sugli ETF UCITS le plusvalenze sono *redditi di capitale*,
  le minusvalenze sono *redditi diversi*. Una minusvalenza su ETF **non** compensa una
  plusvalenza su ETF. Si recupera solo con plusvalenze da azioni singole, ETC/ETN,
  obbligazioni, certificati o derivati, **entro 4 anni**.

Il calcolo di `pac.py` e' una **simulazione**. Il report fiscale di Trade Republic e'
il documento ufficiale e prevale sempre.

---

## Nota sui dati storici

Le righe di `history.jsonl` precedenti allo schema v2 contengono un campo `change_pct`
**sbagliato**: veniva usato `chartPreviousClose`, che e' la chiusura *precedente alla
finestra richiesta* (circa 5 sedute prima), non la chiusura del giorno prima.
`analyze.py` ignora quel campo e ricalcola tutto dalla serie dei prezzi osservati,
quindi i dati gia' raccolti restano utilizzabili.

---

*Progetto personale a scopo informativo. Non e' consulenza finanziaria.*
