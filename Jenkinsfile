pipeline {
    agent { 
        docker {
            image 'python:3.7-alpine3.13' 
            args '-u root:root'
        }
    }
    stages {
        stage('build') {
            steps {
                // withEnv(["HOME=${env.WORKSPACE}"]) {
                //     sh 'pip install flask'
                // }
                sh 'pip install flask'
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
