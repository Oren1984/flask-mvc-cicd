pipeline {
    agent any

    environment {
        // Docker image name for this app
        DOCKER_IMAGE = 'oren1984/flask-mvc-mysql-app'
    }

    stages {

        stage('Clone Repository') {
            steps {
                // Step 1: Pull code from GitHub repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                //  Step 2: Build Docker image from Dockerfile
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Security Scan with Trivy') {
            steps {
                //  Step 3: Scan image with Trivy and save report
                sh '''
                trivy image --severity HIGH,CRITICAL --exit-code 1 --no-progress --format table $DOCKER_IMAGE > trivy-summary.txt
                trivy image --no-progress --format table $DOCKER_IMAGE > trivy-report.txt
                '''
                archiveArtifacts artifacts: 'trivy-*.txt', fingerprint: true
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Step 4: Login and push image to Docker Hub
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
                // Step 5: Deploy app using Helm upgrade
                sh '''
                helm upgrade --install flask-release ./helm/flask-chart --values ./helm/flask-chart/values.yaml
                '''
            }
        }
    }

    post {
        always {
            // Final cleanup or report
            echo 'Pipeline completed (success or failure).'
        }
        failure {
            //  On failure
            echo 'Pipeline failed. Check logs and scan results.'
        }
    }
}
