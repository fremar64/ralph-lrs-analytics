# Ralph LRS Analytics Stack

Stack complète de Learning Record Store (LRS) avec analytics et visualisations avancées pour xAPI.

## Services

- **Ralph** : LRS xAPI moderne et performant (https://lrs.ceredis.net)
- **ClickHouse** : Base de données analytique columnar
- **Grafana** : Dashboards temps réel (https://analytics.ceredis.net)
- **Apache Superset** : Analytics avancés (https://reports.ceredis.net)

## Déploiement via Coolify

### 1. Configuration

1. Créez les fichiers secrets :
```bash
cp auth.json.example auth.json
cp .env.example .env
```

2. Générez les hash bcrypt pour auth.json :
```bash
python3 -m venv venv
source venv/bin/activate
pip install bcrypt
python3 generate-password-hash.py "VotreMotDePasseMoodle"
python3 generate-password-hash.py "VotreMotDePasseAdmin"
```

3. Mettez à jour `auth.json` avec les hash générés

4. Configurez `.env` avec vos valeurs

### 2. Déploiement

Dans Coolify :
1. New Resource → Git Based Application
2. Repository : votre dépôt GitHub
3. Build Pack : Docker Compose
4. Ajoutez toutes les variables d'environnement depuis `.env`
5. Déployez !

## Configuration Moodle

Endpoint xAPI : `https://lrs.ceredis.net/xAPI/statements`
Username : `moodle`
Password : Celui que vous avez hashé dans auth.json

## Monitoring

- Grafana : Dashboards temps réel des activités d'apprentissage
- Superset : Rapports analytiques avancés

## Documentation

Voir la documentation Ralph : https://openfun.github.io/ralph/