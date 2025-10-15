pipeline {
    agent any

    triggers {
        // Optional: equivalent to GitHub 'on: push/pull_request'
        pollSCM('* * * * *') // Checks every minute — adjust as needed
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                script {
                    BRANCH_NAME = env.GIT_BRANCH.replaceFirst(/^origin\//, '')
                    ENVIRONMENT = (BRANCH_NAME == 'release') ? 'production' : 'dev'
                    echo "Branch: ${BRANCH_NAME}"
                    echo "Active Environment: ${ENVIRONMENT}"
                }
            }
        }

        stage('Build Application') {
            agent { label 'ubuntu' }
            steps {
                echo "Building Python app for environment: ${ENVIRONMENT}"
                dir('Assignment1') {
                    sh '''
                        python3 -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
                echo "Build completed successfully for branch ${BRANCH_NAME}"
            }
        }

        stage('Run Unit Tests') {
            agent { label 'ubuntu' }
            steps {
                dir('Assignment1') {
                    echo "Running unit tests in ${ENVIRONMENT} environment"
                    sh 'python3 -m unittest discover -s Unit_Test -p "test_*.py"'
                }
            }
        }
    }

    post {
        failure {
            echo "Build failed for branch ${env.GIT_BRANCH}"
        }
        success {
            echo "===================================="
                echo "CI/CD Completed Successfully"
                echo "Branch: ${BRANCH_NAME}"
                echo "Environment: ${ENVIRONMENT}"
                echo "===================================="
        }
    }
}