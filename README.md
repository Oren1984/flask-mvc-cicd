# Flask MVC + MySQL CI/CD Project

This project demonstrates a full CI/CD pipeline for a Flask application using the MVC pattern, integrated with a MySQL database. The pipeline is implemented with Jenkins, Docker, Trivy, Helm, and Kubernetes.

---

## 🧱 Tech Stack

- **Flask MVC** – Basic CRUD (Create implemented)
- **MySQL** – As backend database
- **Jenkins** – CI/CD Pipeline
- **Docker** – Containerization
- **Trivy** – Security image scanning
- **Helm** – Kubernetes deployment packaging
- **Kubernetes** – Deployment and service orchestration

---

## 🗂 Project Structure

flask-mvc-cicd/
├── app/ # Flask MVC application
├── Dockerfile # Build definition for the container
├── docker-compose.yml # For local development
├── helm/ # Helm chart for K8s deployment
│ └── flask-chart/
├── Jenkinsfile # Jenkins pipeline definition
├── kubernetes/ # Kubernetes YAML files (optional legacy)
├── requirements.txt # Python dependencies
└── wait-for-it.sh # MySQL wait script

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
🧪 Features Implemented
 Flask MVC architecture

 Create operation (Add users)

 SQLite/MySQL integration

 CI/CD Pipeline

 Docker build and push

 Helm deploy to K8s

 Trivy scan integration

🛠 Next Improvements
Implement Read/Update/Delete operations

Integrate proper error handling

Add monitoring & logging

🔗 Related Links
GitHub Repo: https://github.com/Oren1984/flask-mvc-cicd

Docker Hub: https://hub.docker.com/r/oren1984/flask-mvc-mysql-app

👨‍💻 Author
Oren Salami – 2025
Project submitted as part of Final Project CI/CD track (August)
