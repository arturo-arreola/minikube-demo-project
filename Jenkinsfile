pipeline {
  agent any
  environment {
    DOCKERHUB_CREDS = credentials('dockerhub-credenciales')
  }
  
  stages {
    stage('Construir imagen') {
      steps {
        echo 'Construyendo la imagen de Docker...'
        sh 'docker build -t harreolarubio/mi-app-k8s:v2.0 .'
      }
    }
    stage('Subir a Docker Hub (Push)') {
      steps {
        echo 'Iniciando sesion en Docker Hub...'
        sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'

        echo 'Subiendo la imagen a Docker Hub...'
        sh 'docker push harreolarubio/mi-app-k8s:v2.0'
      }
    }
  }
}