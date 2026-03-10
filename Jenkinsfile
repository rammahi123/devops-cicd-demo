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
        sh 'docker build -t rammahi123/devops-demo:v2 .'
      }
    }

    stage('Push Docker image') {
      steps {
        echo 'Push Docker image to DockerHub...'
        sh 'docker push rammahi123/devops-demo:v2'
      }
    }

    stage ('Run Container') {
      steps {
        echo 'Running container...'
        sh 'docker run rammahi123/docker-demo:v2'
      }
    }
  }
}
        
