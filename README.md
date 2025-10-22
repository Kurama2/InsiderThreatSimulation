# Simulation d'une Menace Interne

## Contexte
Ce projet simule une analyse d'incident interne où un employé (`user123`) exfiltre `Client_NAS.zip` à 2h vers une IP externe (172.16.xxx.x), détecté initialement par une alerte DLP de Purview. DTEX confirme une connexion via openvpn.exe. Il montre l'utilisation de Purview, Splunk, Sentinel, et DTEX.

## Structure
- `data/` : Journaux fictifs (`fake_logs.csv`).
- `scripts/` : Scripts Python (`generate_logs.py`, `test.py`, `analyze_logs.py`).
- `reports/` : Graphique (`activity_plot.png`), rapport (`incident_report.pdf`).
- `sentinel_query.txt` : Requête KQL pour Sentinel.
- `purview_rule.txt` : Règle DLP pour Purview.