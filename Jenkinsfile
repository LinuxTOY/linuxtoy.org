pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                rocketSend avatar: 'https://ci.unixkoans.com/static/ff676c77/images/headshot.png', channel: 'general', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})", rawMessage: true
                sh 'sudo pelican --ignore-cache -o /var/www/linuxtoy.org'
            }
        }
    }
    post {
        success {
            slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
            rocketSend avatar: 'https://ci.unixkoans.com/static/ff676c77/images/headshot.png', channel: 'general', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})", rawMessage: true
        }
        failure {
            slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
            rocketSend avatar: 'https://ci.unixkoans.com/static/ff676c77/images/headshot.png', channel: 'general', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})", rawMessage: true
        }
    }
}
