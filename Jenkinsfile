pipeline {
    agent any

    parameters {
        choice(
            name: 'APP_ENV',
            choices: ['dev', 'test'],
            description: 'Uygulama ortamı'
        )
    }

    environment {
        APP_ENV = "${params.APP_ENV}"
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker compose -p env-logger build'
            }
        }

        stage('DB') {
            steps {
                sh 'docker compose -p env-logger up -d db'
            }
        }

        stage('Run App') {
            steps {
                sh 'docker compose -p env-logger run --rm app || true'
            }
        }
    }
}
