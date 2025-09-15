pipeline {
    agent any
    
    stages {
        stage('Setup & Test') {
            steps {
                sh 'python3 -m venv venv'
                // This one command installs everything
                sh './venv/bin/pip install -e .'
                // Run tests
                sh './venv/bin/pytest tests/'  
            }
        }
    }
}