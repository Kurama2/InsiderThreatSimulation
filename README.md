# Simulation d'une Menace Interne

## Contexte
Ce projet simule une analyse d'incident interne où un employé (`user123`) télécharge `Client_NAS.zip` à 2h et le partage vers une IP externe (172.16.254.1). Il montre l'utilisation de DTEX, Splunk, Sentinel, et Purview.

## Structure
- `data/` : Journaux fictifs (`fake_logs.csv`).
- `scripts/` : Scripts Python (`generate_logs.py`, `test.py`).
- `reports/` : Rapport final (en cours).
