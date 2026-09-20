# Configuration

## What

Runtime configuration lives in `config.py` and is populated from environment variables, loaded via `python-dotenv` if a `.env` file is present.

## Why

Keeping database credentials and the secret key out of source code lets the same image run against different databases (local Docker Compose, Kubernetes, Helm) without code changes — only the environment differs.

## How

### `config.Config`

| Variable | Default (if unset) | Purpose |
|---|---|---|
| `SECRET_KEY` | `dev-key-please-change` | Flask session/signing key. Should be overridden outside local development. |
| `DB_HOST` | `localhost` | MySQL host. |
| `DB_USER` | `root` | MySQL user. |
| `DB_PASSWORD` | *(empty)* | MySQL password. |
| `DB_NAME` | `flask_mvc_db` | MySQL database name. |

These are combined into `SQLALCHEMY_DATABASE_URI` as `mysql://<user>:<password>@<host>/<name>`. `SQLALCHEMY_TRACK_MODIFICATIONS` is always `False`.

An alternative local SQLite URI is present in `config.py` as a commented-out block; it is not active — MySQL is the only configuration path currently in effect.

### Where each variable is set

| Environment | Source |
|---|---|
| Local (native `python run.py`) | `.env` file (via `python-dotenv`) or shell environment |
| Docker Compose | `environment:` block for the `web` service in `docker-compose.yml` |
| Kubernetes (raw manifests) | `env:` block in `kubernetes/flask-deployment.yaml`, plus `mysql-secret` for the password |
| Helm | `env:` block in `helm/flask-chart/templates/deployment.yaml`, sourced from `values.yaml` (`mysql.rootPassword`) and the generated `mysql-secret` |

### Secrets

- `.gitignore` excludes `.env`, `.env.*` (with an explicit exception for `.env.example`) and `kubernetes/mysql-secret.yaml`, so real credentials are not meant to be committed.
- No `.env.example` file currently exists in the repository — see the environment variable table above for the values to set if you create one.
- The Helm chart generates its own `mysql-secret` from `values.mysql.rootPassword` (base64-encoded). The raw Kubernetes manifests instead expect a pre-created `kubernetes/mysql-secret.yaml` with a `mysql-root-password` key — it is not included in the repo and must be created before applying the manifests.
