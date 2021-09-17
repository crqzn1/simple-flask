pipeline {
    agent { 
        docker {
            image 'python:3.7.3' 
            // args '-u root:root'
        }
    }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install flask --user'
                }
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
