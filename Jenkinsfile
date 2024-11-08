pipeline {
    agent any

    environment {
        ANSIBLE_PLAYBOOK = 'setup_monitor.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run setup node exporter') {
            steps {
                script {
                    // Run the Ansible playbook
                    sh "ansible-playbook ${ANSIBLE_PLAYBOOK}"
                }
            }
        }
    }
}
