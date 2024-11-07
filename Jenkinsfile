pipeline {
    agent any

    environment {
        ANSIBLE_PLAYBOOK = 'setup_node_exporter.yml'
        INVENTORY = 'inventory.ini' // Định nghĩa file inventory Ansible nếu cần
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Ansible Playbook') {
            steps {
                script {
                    // Run the Ansible playbook
                    sh "ansible-playbook -i ${INVENTORY} ${ANSIBLE_PLAYBOOK}"
                }
            }
        }
    }
}
