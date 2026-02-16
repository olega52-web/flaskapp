pipeline {
    agent any

    environment {
        APP_NAME = "flask-app"
        IMAGE_NAME = "flask-ci-cd"
        IMAGE_TAG = "latest"
        HOST_PORT = "8081"
        CONTAINER_PORT = "5000"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Build Docker image") {
            steps {
                sh """
                  docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage("Run tests") {
            steps {
                sh """
                  docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} pytest -q
                """
            }
        }

        stage("Deploy container") {
            steps {
                sh """
                  if docker ps -a --format '{{.Names}}' | grep -w ${APP_NAME}; then
                      docker rm -f ${APP_NAME}
                  fi

                  docker run -d --name ${APP_NAME} \
                    -p ${HOST_PORT}:${CONTAINER_PORT} \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage("Smoke test") {
            steps {
                sh """
                  sleep 2
                  curl -s http://localhost:${HOST_PORT}/health | grep healthy
                """
            }
        }
    }

    post {
        always {
            sh "docker images | head -n 5 || true"
        }
    }
}
