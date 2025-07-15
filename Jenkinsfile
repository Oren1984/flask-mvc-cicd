pipeline {
    agent { label 'oren-worker' }

    environment {
        DOCKER_IMAGE = 'oren1984/flask-mvc-mysql-app'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Security Scan with Trivy') {
            steps {
                echo 'Running Trivy security scan...'
                sh '''
                trivy image --severity HIGH,CRITICAL --no-progress --scanners vuln --format table $DOCKER_IMAGE > trivy-summary.txt || true
                trivy image --no-progress --scanners vuln --format table $DOCKER_IMAGE > trivy-report.txt || true
                '''
                archiveArtifacts artifacts: 'trivy-*.txt', fingerprint: true
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes with Helm') {
            steps {
                echo 'Deploying to Kubernetes with Helm...'
                sh '''
                helm upgrade --install flask-release ./helm/flask-chart --values ./helm/flask-chart/values.yaml
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Pipeline failed. Check logs and scan results.'
        }
    }
}
