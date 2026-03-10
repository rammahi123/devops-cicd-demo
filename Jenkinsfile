pipeline {
  agent any

  stages {

    stage('Clone Repositary') {
      steps {
        git 'https://github.com/rammahi123/devops-cicd-demo.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t rammahi123/devops-demo:v4 .'
      }
    }

    stage('Push Image') {
      steps {
        sh 'docker push rammahi123/devops-demo:v4'
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl set image deployment/devops-demo devops-demo=rammahi123/devopsdemo:v4'
      }
    }
  }
