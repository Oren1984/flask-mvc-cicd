# Flask MVC CI/CD Project

A Flask MVC CRUD application backed by MySQL, with a complete CI/CD pipeline that builds, scans, publishes, and deploys it to Kubernetes.

---

## What

This repository contains:

- A Flask application structured with the MVC pattern (`app/`), providing CRUD management of `User` records via a MySQL-backed data model.
- A Jenkins pipeline (`Jenkinsfile`) that builds a Docker image, scans it with Trivy, pushes it to Docker Hub, and deploys it to Kubernetes with Helm.
- Two Kubernetes deployment paths: raw manifests (`kubernetes/`) and a Helm chart (`helm/flask-chart/`).
- A Docker Compose setup (`docker-compose.yml`) for running the app and MySQL locally.

## Why

This is a portfolio/learning project demonstrating an end-to-end DevOps workflow: containerized application delivery, automated vulnerability scanning, image publishing, and Kubernetes deployment through both raw manifests and Helm — rather than just the application code on its own.

## How

### Quick start (Docker Compose)

```bash
docker compose up --build -d
```

The app is then available at `http://localhost:5000`. See [docs/local-development.md](docs/local-development.md) for details, other commands, and running natively without Docker.

### Deploying to Kubernetes

```bash
kubectl apply -f kubernetes/
# or
helm install flask-release ./helm/flask-chart
```

See [docs/deployment.md](docs/deployment.md) for the full walkthrough, including secret setup and configurable values.

### CI/CD pipeline

Push to GitHub → Jenkins builds the image → Trivy scan → Docker Hub push → Kubernetes deploy via Helm. See [docs/ci-cd-pipeline.md](docs/ci-cd-pipeline.md) for the stage-by-stage breakdown.

---

## Technology Stack

- Python / Flask
- MySQL
- Docker / Docker Compose
- Jenkins
- Trivy
- Kubernetes
- Helm

## Project Structure

```text
flask-mvc-cicd/
├── app/                 # Flask MVC application
├── docs/                # Detailed documentation (architecture, deployment, CI/CD, etc.)
├── helm/                # Helm chart and deployment values
├── kubernetes/          # Raw Kubernetes manifests
├── config.py            # Application configuration
├── docker-compose.yml   # Local multi-container environment
├── Dockerfile            # Application container definition
├── Jenkinsfile           # CI/CD pipeline definition
├── requirements.txt      # Python dependencies
├── run.py                # Application entry point
└── wait-for-it.sh        # Service readiness helper
```

## Documentation

Detailed reference docs live in [`docs/`](docs/README.md):

| Page | Covers |
|---|---|
| [docs/architecture.md](docs/architecture.md) | MVC structure, request flow, data model |
| [docs/configuration.md](docs/configuration.md) | Environment variables, `config.py`, secrets |
| [docs/local-development.md](docs/local-development.md) | Running locally with Docker Compose or natively |
| [docs/deployment.md](docs/deployment.md) | Kubernetes manifests and the Helm chart |
| [docs/ci-cd-pipeline.md](docs/ci-cd-pipeline.md) | Jenkins pipeline stages and the Trivy scan |

## Security Scanning

The CI/CD pipeline uses Trivy to scan the Docker image for known vulnerabilities before it is pushed and deployed. A failed or interrupted scan should be investigated and rerun before continuing the pipeline. See [docs/ci-cd-pipeline.md](docs/ci-cd-pipeline.md#2-security-scan-with-trivy) for details.

## Cleanup

```bash
docker compose down                 # stop the local environment
helm uninstall flask-release        # remove the Helm release
kubectl delete -f kubernetes/       # remove raw-manifest resources
```

---

## Notes

- Includes a complete Flask MVC structure with CRUD functionality.
- Built for practical CI/CD and Kubernetes workflow demonstration.
- Kubernetes deployments can be managed through raw manifests or Helm.
- Local databases, secrets, environment files, caches, and generated artifacts are excluded from version control.
