# Flask MVC CI/CD Project

A complete CI/CD implementation for a Flask MVC application backed by MySQL and deployed to Kubernetes.

The project demonstrates an end-to-end DevOps workflow covering application containerization, automated vulnerability scanning, Docker image publishing, Kubernetes deployment, and Helm-based release management.

---

## Overview

This project contains a Flask application structured according to the MVC pattern, with CRUD functionality and a complete CI/CD pipeline.

The pipeline performs the following stages:

1. Retrieves the source code from GitHub
2. Installs and validates application dependencies
3. Builds the Docker image
4. Scans the image for vulnerabilities with Trivy
5. Pushes the approved image to Docker Hub
6. Deploys the application to Kubernetes
7. Manages the Kubernetes release through Helm

---

## Technology Stack

- Python
- Flask
- MySQL
- Jenkins
- Docker
- Docker Compose
- Trivy
- Kubernetes
- Helm

---

## Project Structure

```text
flask-mvc-cicd/
├── app/                 # Flask MVC application
├── helm/                # Helm chart and deployment values
├── kubernetes/          # Kubernetes manifests
├── config.py            # Application configuration
├── docker-compose.yml   # Local multi-container environment
├── Dockerfile           # Application container definition
├── Jenkinsfile          # CI/CD pipeline definition
├── requirements.txt     # Python dependencies
├── run.py               # Application entry point
└── wait-for-it.sh       # Service readiness helper
Local Deployment

Build and start the application with Docker Compose:

docker compose up --build -d

Check the running containers:

docker compose ps

View application logs:

docker compose logs -f

Stop the local environment:

docker compose down
CI/CD Pipeline

The Jenkins pipeline is defined in the Jenkinsfile.

GitHub Push
    ↓
Jenkins Pipeline
    ↓
Dependency Validation
    ↓
Docker Image Build
    ↓
Trivy Vulnerability Scan
    ↓
Docker Hub Push
    ↓
Kubernetes Deployment
    ↓
Helm Release

Jenkins and Docker Hub credentials must be configured in the Jenkins credentials store before running the complete pipeline.

Kubernetes Deployment

Validate the Kubernetes manifests:

kubectl apply --dry-run=client -f kubernetes/

Deploy the application:

kubectl apply -f kubernetes/

Check the deployed resources:

kubectl get pods
kubectl get deployments
kubectl get services
Helm Deployment

Install the application:

helm install flask-release ./helm/flask-chart

Upgrade an existing release:

helm upgrade flask-release ./helm/flask-chart

Check the release status:

helm list
helm status flask-release

Remove the release:

helm uninstall flask-release
Application Access

Inspect the Kubernetes service:

kubectl get svc

Use the exposed service address or NodePort according to the active Kubernetes environment and service configuration.

Security Scanning

The CI/CD pipeline uses Trivy to scan the Docker image for known vulnerabilities before publishing and deployment.

A failed or interrupted scan should be investigated and rerun before continuing the pipeline.

Cleanup

Stop the Docker Compose environment:

docker compose down

Remove the Helm release:

helm uninstall flask-release

Remove resources deployed through Kubernetes manifests:

kubectl delete -f kubernetes/
Project Purpose

This repository is a portfolio and learning project demonstrating:

Flask MVC application architecture
Containerized application delivery
Jenkins pipeline automation
Docker image vulnerability scanning
Docker Hub image publishing
Kubernetes workload deployment
Helm-based release management
Notes
Includes a complete Flask MVC structure with CRUD functionality
Built for practical CI/CD and Kubernetes workflow demonstration
Kubernetes deployments can be managed through raw manifests or Helm
Local databases, secrets, environment files, caches, and generated artifacts are excluded from version control
