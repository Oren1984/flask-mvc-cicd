# Deployment

## What

The app can be deployed to Kubernetes two ways: raw manifests in `kubernetes/`, or the Helm chart in `helm/flask-chart/`. Both deploy the same Flask app plus a MySQL instance.

## Why

Raw manifests are simple and transparent for learning/demo purposes; the Helm chart adds templating, configurable values, autoscaling, and ingress support — showing both approaches is part of this project's CI/CD demonstration goal.

## How

### Option A — Raw Kubernetes manifests (`kubernetes/`)

| File | Resource |
|---|---|
| `flask-deployment.yaml` | Flask app `Deployment` (1 replica, image `oren1984/flask-mvc-mysql-app:latest`, port 5000) |
| `flask-service.yaml` | `NodePort` service exposing the app on port 80 / nodePort 30080 |
| `mysql-deployment.yaml` | MySQL 5.7 `Deployment` with an `emptyDir` volume (ephemeral — data is lost if the pod is recreated) |
| `mysql-service.yaml` | Service exposing MySQL to the Flask deployment |

Both deployments reference a `mysql-secret` (key `mysql-root-password`) that is **not included in the repo** (it's excluded via `.gitignore`) and must be created manually before applying, e.g.:

```bash
kubectl create secret generic mysql-secret \
  --from-literal=mysql-root-password=<your-password>
```

Then:

```bash
kubectl apply --dry-run=client -f kubernetes/   # validate
kubectl apply -f kubernetes/                    # deploy
kubectl get pods deployments services           # check status
```

### Option B — Helm chart (`helm/flask-chart/`)

```text
helm/flask-chart/
├── Chart.yaml
├── values.yaml
├── .helmignore
└── templates/
    ├── deployment.yaml         # Flask deployment (waits for MySQL via an initContainer)
    ├── service.yaml
    ├── flask-service.yaml
    ├── hpa.yaml                # HorizontalPodAutoscaler (disabled by default)
    ├── ingress.yaml            # disabled by default
    ├── mysql-deployment.yaml
    ├── mysql-service.yaml
    ├── mysql-secret.yaml       # generated from values.mysql.rootPassword
    ├── serviceaccount.yaml
    ├── _helpers.tpl
    ├── NOTES.txt
    └── tests/test-connection.yaml
```

Key values in `values.yaml`:

| Key | Default | Purpose |
|---|---|---|
| `replicaCount` | `1` | Flask pod replicas |
| `image.repository` / `image.tag` | `oren1984/flask-mvc-mysql-app` / `latest` | Container image |
| `service.type` / `service.port` / `service.nodePort` | `NodePort` / `80` / `30080` | Flask service exposure |
| `ingress.enabled` | `false` | Optional ingress |
| `autoscaling.enabled` | `false` | Optional HPA |
| `mysql.image` | `mysql:5.7` | MySQL image used by the chart |
| `mysql.rootPassword` | `mysql` | Used to generate the `mysql-secret` — override this for anything beyond local testing |

Unlike the raw manifests, the Helm chart **generates its own `mysql-secret`** from `values.mysql.rootPassword`, so no manual secret creation is required.

```bash
helm install flask-release ./helm/flask-chart      # install
helm upgrade flask-release ./helm/flask-chart      # upgrade
helm list                                           # list releases
helm status flask-release                           # check status
helm uninstall flask-release                        # remove
```

### Accessing the app

```bash
kubectl get svc
```

Use the service's ClusterIP/NodePort address according to your cluster environment (e.g. `http://<node-ip>:30080` for the default NodePort).

### Known inconsistency

`helm/flask-chart/` contains a nested `helm/flask-chart/helm/flask-chart/` directory (with its own `values.yaml`, a `templates/mysql-deployment.yaml`, and `files/init.sql`) that is not referenced by `Chart.yaml` or any template — it appears to be leftover/stray content rather than part of the active chart. It is documented here as-is; no files were changed as part of this documentation update.
