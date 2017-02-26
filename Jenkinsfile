pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                checkout scm
                sh 'pelican --ignore-cache'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo mv output /var/www/linuxtoy.org'
            }
        }
    }
}
