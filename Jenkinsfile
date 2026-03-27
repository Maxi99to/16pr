pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your_repo.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest -q'
            }
        }

        stage('Package') {
            steps {
                sh '''
                mkdir build
                cp -r src app.py requirements.txt build/
                cd build
                zip -r app.zip .
                '''
            }
        }
    }
}
