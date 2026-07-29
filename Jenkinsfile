pipeline {
  agent any
  stages {
    stage('Construir imagen') {
      steps {
        echo 'Construyendo la imagen de Docker...'
        sh 'docker build -t harreolarubio/mi-app-k8s:v2.0 .'
      }
    }
  }
}