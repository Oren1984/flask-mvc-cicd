# Flask MVC + MySQL CI/CD Project

This project demonstrates a full CI/CD pipeline for a Flask application using the MVC pattern, integrated with a MySQL database. The pipeline is implemented with Jenkins, Docker, Trivy, Helm, and Kubernetes.

---

## 🧱 Tech Stack

- [**Flask MVC**](https://flask.palletsprojects.com/) – Basic CRUD
- [**MySQL**](https://www.mysql.com/) – As backend database
- [**Jenkins**](https://www.jenkins.io/) – CI/CD Pipeline
- [**Docker**](https://www.docker.com/) – Containerization
- [**Trivy**](https://aquasecurity.github.io/trivy/) – Security image scanning
- [**Helm**](https://helm.sh/) – Kubernetes deployment packaging
- [**Kubernetes**](https://kubernetes.io/) – Deployment and service orchestration

---

## 🗂 Project Structure

```text
flask-mvc-cicd/
├── app/                      # Flask MVC application
│   ├── models/               # Database models
│   ├── templates/            # HTML templates
│   └── static/               # Static files (CSS, JS)
├── Dockerfile                # Build definition for the container
├── docker-compose.yml        # For local development
├── helm/                     # Helm chart for K8s deployment
│   └── flask-chart/          # Helm chart details
├── Jenkinsfile               # Jenkins pipeline definition
├── kubernetes/               # Kubernetes YAML files (optional legacy)
├── requirements.txt          # Python dependencies
└── wait-for-it.sh            # MySQL wait script
└── QA_Docs/ # QA documentation and Jenkins logs
```

---

##  Deployment Pipeline (Jenkins)

### Pipeline Stages:

1. **Checkout Git repository**  
   https://github.com/Oren1984/flask-mvc-cicd.git

2. **Build Docker image**  
   `oren1984/flask-mvc-mysql-app`

3. **Run Trivy security scan**  
   High/Critical vulnerabilities scanned (errors ignored on timeout)

4. **Push to Docker Hub**  
   DockerHub Repo:  
   `docker pull oren1984/flask-mvc-mysql-app`

5. **Deploy with Helm to Kubernetes**  
   Release name: `flask-release`  
   Values file: `helm/flask-chart/values.yaml`

---

## ✅ Jenkins Pipeline Output

See full successful execution log in:  
📄 [`jenkins-pipeline-log.txt`](jenkins-pipeline-log.txt)

---

## 🌐 Accessing the Application

After deployment, run:

```bash
export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services flask-release-flask-chart)
export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT
```

---

## 🧪 Features Implemented

- Flask MVC architecture  
- Full CRUD operations  
- SQLite/MySQL integration  
- CI/CD Pipeline  
- Docker build and push  
- Helm deploy to K8s  
- Trivy scan integration

---

🧾 Quality Assurance (QA)

Comprehensive QA documentation is included under the QA_Docs/ folder.
It provides validation for all pipeline stages, Trivy scan results, and deployment verification.

Document	Description
01_STP_Test_Plan.xlsx	Test plan covering CI/CD flow and environment setup
02_STD_Test_Cases.xlsx	Step-by-step execution cases for build, scan, push, deploy
03_STR_Test_Report.xlsx	Pipeline results and verification summary
04_Bug_Report.xlsx	Documented Trivy timeout and scan findings
Jenkins_Logs/	Original Jenkins logs for reference and traceability

✅ All build and deployment stages completed successfully.
⚠️ Trivy scan encountered a temporary timeout; re-scan recommended.

---

## 🔗 Related Links

- GitHub Repo: https://github.com/Oren1984/flask-mvc-cicd  
- Docker Hub: https://hub.docker.com/r/oren1984/flask-mvc-mysql-app

---

## 👨‍💻 Author

Oren Salami – 2025  
Project submitted as part of Final Project CI/CD track (August)

