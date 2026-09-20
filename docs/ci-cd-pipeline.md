# CI/CD Pipeline

## What

`Jenkinsfile` defines a four-stage declarative pipeline: build the Docker image, scan it with Trivy, push it to Docker Hub, and deploy to Kubernetes via Helm.

## Why

Running a vulnerability scan before publishing and gating deployment behind Helm gives the pipeline a realistic build → verify → publish → deploy flow, which is the CI/CD practice this project is built to demonstrate.

## How

Pipeline agent: label `oren-worker`. Image name: `oren1984/flask-mvc-mysql-app` (`DOCKER_IMAGE` env var).

### 1. Build Docker Image

```bash
docker build -t $DOCKER_IMAGE .
```

### 2. Security Scan with Trivy

```bash
trivy image --severity HIGH,CRITICAL --no-progress --scanners vuln --format table $DOCKER_IMAGE > trivy-summary.txt || true
trivy image --no-progress --scanners vuln --format table $DOCKER_IMAGE > trivy-report.txt || true
```

Both reports are archived as Jenkins build artifacts (`trivy-*.txt`). The scan does not currently fail the build on findings (`|| true`) — a failed or interrupted scan should be investigated and rerun manually before trusting the published image.

### 3. Push to Docker Hub

Uses the Jenkins credential `dockerhub-creds` (username/password) to log in and push:

```bash
echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
docker push $DOCKER_IMAGE
```

This credential must exist in the Jenkins credentials store before the pipeline can run this stage.

### 4. Deploy to Kubernetes with Helm

```bash
helm upgrade --install flask-release ./helm/flask-chart --values ./helm/flask-chart/values.yaml
```

Requires the Jenkins agent to have `kubectl`/`helm` configured with access to the target cluster.

### Post actions

- `always`: logs pipeline completion.
- `failure`: logs a reminder to check logs and scan results.

### Prerequisites summary

- A Jenkins agent labeled `oren-worker` with Docker, Trivy, and Helm/kubectl installed and configured.
- Jenkins credential `dockerhub-creds` (Docker Hub username/password).
- Cluster access configured for the agent running the Helm stage.
