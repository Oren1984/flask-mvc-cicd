# Local Development

## What

Two ways to run the app locally: Docker Compose (recommended — matches the containerized deployment), or natively against a MySQL instance you provide.

## Why

Docker Compose reproduces the same container image and MySQL version used further down the pipeline, so behavior seen locally is representative of what CI/CD will build and deploy.

## How

### Option A — Docker Compose (recommended)

```bash
docker compose up --build -d
```

This starts two services (`docker-compose.yml`):

- `db` — MySQL 8.0, with a persistent `db_data` volume, exposed on `3306`.
- `web` — the Flask app, built from the local `Dockerfile`, exposed on `5000`. It runs `wait-for-it.sh db 3306 -- python run.py` so it waits for MySQL to accept connections before starting.

Useful commands:

```bash
docker compose ps          # check running containers
docker compose logs -f     # tail application logs
docker compose down        # stop and remove containers
```

The app is then available at `http://localhost:5000`.

### Option B — Native Python

Requires Python 3.10+ and a reachable MySQL server.

```bash
pip install -r requirements.txt
```

Set the database environment variables (see [configuration.md](configuration.md)) either in your shell or in a `.env` file, then run:

```bash
python run.py
```

The dev server listens on `0.0.0.0:5000` with `debug=True`.

### Notes

- Tables are created automatically on startup via `db.create_all()` — no separate migration step is needed for a fresh database.
- `wait-for-it.sh` is only used by the Compose `web` command; it is not invoked when running `python run.py` directly, so make sure MySQL is already reachable in that case.
