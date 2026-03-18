# Flask MVC CI/CD Project

Full CI/CD pipeline for a Flask MVC application with MySQL, deployed to Kubernetes.

---

## Overview

A complete DevOps project demonstrating build, scan, push, and deployment of a Flask MVC app using Jenkins, Docker, Trivy, Helm, and Kubernetes.

---

## Tech Stack

- Flask (MVC)
- MySQL
- Jenkins
- Docker
- Trivy
- Kubernetes
- Helm

---

## Quick Start

Run locally with Docker Compose:

```bash
docker compose up -d

Deploy to Kubernetes with Helm:

helm install flask-release ./helm/flask-chart
```

---

## Usage

Pipeline flow:

- Code pushed to GitHub

- Jenkins pipeline runs automatically

- Docker image is built

- Trivy scans for vulnerabilities

- Image is pushed to Docker Hub

- App is deployed to Kubernetes via Helm

Access the app:

```bash
kubectl get svc
```

Or via NodePort (if configured).

---

## Cleanup

```bash
helm uninstall flask-release
```

---

## Notes

- Includes full MVC structure with CRUD support

- QA documentation available under QA_Docs/

- Built for learning CI/CD and Kubernetes workflows

- Trivy scan may require re-run if timeout occurs

---
