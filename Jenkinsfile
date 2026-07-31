pipeline {
  agent any
  environment {
    DOCKERHUB_CREDS = credentials('dockerhub-credenciales')
    GITHUB_CREDS = credentials('github-credenciales')
  }

  stages {
    stage('Construir imagen y subir a Docker Hub (Build & Push)') {
      steps {
        echo 'Construyendo la imagen con version 1.0.${BUILD_NUMBER}...'
        sh 'docker build -t harreolarubio/mi-app-k8s:1.0.${BUILD_NUMBER} .'

        echo 'Subiendo la imagen a Docker Hub...'
        sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'
        sh 'docker push harreolarubio/mi-app-k8s:1.0.${BUILD_NUMBER}'

      }
    }
    stage('Actualizar GitOps (CD)'){
      steps{
        echo 'Actualizando el manifiesto k8s.yaml con la nueva version de la imagen...'

        // 1. Se utiliza un editor de texto interno de jenkins para reemplazar la version de la imagen en el manifiesto k8s.yaml
        sh "sed -i 's|image: harreolarubio/mi-app-k8s:.*|image: harreolarubio/mi-app-k8s:1.0.${BUILD_NUMBER}|g' k8s.yaml"

        // 2. Configura a Jenkins como un usuario de Git
        sh 'git config --global user.email "jenkins@company.com"'
        sh 'git config --global user.name "Jenkins"'

        // 3. Agrega los cambios al repositorio Git
        sh """
          git add k8s.yaml
          git commit -m 'Actualizando la version de la imagen a 1.0.${BUILD_NUMBER} en el archivo k8s.yaml desde Jenkins'
          git push https://${GITHUB_CREDS_USR}:${GITHUB_CREDS_PSW}@github.com/harreolarubio/mi-app-k8s.git HEAD:main
        """
      }
    }
  }
}