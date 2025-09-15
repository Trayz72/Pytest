pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'                    
                sh './venv/bin/pip install -r requirements.txt' 
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh './venv/bin/pytest tests/'  
            }
        }
        
    }
    
}