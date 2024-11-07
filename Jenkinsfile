pipeline {
    agent any

    environment {
        ANSIBLE_PLAYBOOK = 'send_ssh_key.yml'
        ANSIBLE_PLAYBOOK2 = 'setup_node_exporter.yml'
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
                    sh "ansible-playbook ${ANSIBLE_PLAYBOOK2}"
                }
            }
        }
    }
}
