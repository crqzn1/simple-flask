pipeline {
    agent { docker { image 'python:3.7.3' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install flask --user'
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
