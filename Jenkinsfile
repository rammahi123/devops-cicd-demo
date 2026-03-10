pipeline {
  agent any

  stages {
    stage('Clone Repositary') {
      steps {
        echo 'Cloning Repositary'
        git branch: 'main', url: 'https://github.com/rammahi123/devops-cicd-demo.git'
      }
    }

    stage('Build docker image') {
      steps {
        echo 'Building Docker image...'
        sh 'docker build -t rammahi123/devops-demo:v3 .'
      }
    }

    stage('Push Docker image') {
      steps {
        echo 'Push Docker image to DockerHub...'
        sh 'docker push rammahi123/devops-demo:v3'
      }
    }

    stage ('Run Container') {
      steps {
        echo 'Running container...'
        sh '''
        docker rm -f devops-demo || true
        docker run -d -p 9090:80 --name devops-demo rammahi123/devops-demo:v3
        '''
      }
    }
  }
}
        
