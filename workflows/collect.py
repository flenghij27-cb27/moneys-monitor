name: Moneys Monitor - Raccolta Dati

# Solo lettura di fonti pubbliche. Nessun ordine, nessuna operazione di trading.
#
# Orari in UTC (GitHub Actions NON applica l'ora legale):
#   06:00 UTC -> 08:00 IT estate / 07:00 IT inverno  - chiusura Asia, pre-apertura Europa
#   12:00 UTC -> meta' seduta europea
#   16:00 UTC -> dopo la chiusura di Milano (17:30 IT estate)
#   21:30 UTC -> dopo la chiusura USA in ENTRAMBI i regimi (20:00 estate / 21:00 inverno)
# GitHub ritarda gli schedule sotto carico: e' normale vedere qualche minuto di drift.

on:
  schedule:
    - cron: "0 6,12,16 * * *"
    - cron: "30 21 * * *"
  workflow_dispatch:
    inputs:
      run_analysis:
        description: "Rigenera anche REPORT.md e PAC_REPORT.md"
        type: boolean
        default: true

permissions:
  contents: write

# Impedisce che due run si sovrappongano e si sovrascrivano a vicenda.
concurrency:
  group: moneys-monitor-collect
  cancel-in-progress: false

jobs:
  collect:
    runs-on: ubuntu-latest
    timeout-minutes: 20

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Raccolta dati
        env:
          FRED_API_KEY: ${{ secrets.FRED_API_KEY }}
        run: python3 scripts/collect.py

      - name: Analisi di mercato
        if: github.event_name == 'schedule' || inputs.run_analysis
        run: python3 scripts/analyze.py --top 12

      - name: Grafici
        if: github.event_name == 'schedule' || inputs.run_analysis
        run: python3 scripts/charts.py

      - name: Report PAC
        if: github.event_name == 'schedule' || inputs.run_analysis
        continue-on-error: true          # senza transactions.csv non deve rompere la raccolta
        run: python3 scripts/pac.py --json-only

      - name: Commit e push
        run: |
          set -euo pipefail
          git config user.name  "moneys-monitor-bot"
          git config user.email "actions@github.com"
          git add data/
          if git diff --staged --quiet; then
            echo "Nessuna modifica da committare."
            exit 0
          fi
          git commit -m "dati $(date -u +'%Y-%m-%d %H:%M UTC')"
          # Se un altro run ha spinto nel frattempo, riallinea invece di fallire.
          for i in 1 2 3; do
            if git push; then
              echo "push ok al tentativo $i"; exit 0
            fi
            echo "push fallito, ribasamento (tentativo $i)"
            git pull --rebase --autostash origin "${GITHUB_REF_NAME}"
            sleep $((i * 5))
          done
          echo "push fallito dopo 3 tentativi" >&2
          exit 1
