pipeline {
    agent { 
        node {
            label 'dev'
            }
      }
      environment {
        MYSQL_ROOT_LOGIN = credentials('mysql-root-login')
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build with Maven') {
            steps {
                sh '''
                mvn --version
                java -version
                mvn clean package -Dmaven.test.failure.igore=true
                '''
            }
        }
        stage('Packaging/Pushing image') {
            steps {
                withDockerRegistry(credentialsID: 'dockerhub' url: 'https://index.docker.io/v1/',  )
            
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}