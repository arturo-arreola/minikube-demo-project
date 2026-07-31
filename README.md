# ArgoCD Password 

`djm4rjOYowhUHhVS`



# Arrancar todo el ambiente

1. Verificar que Docker este inicializado

2. Iniciar Minikube

`minikube start`

3. Iniciar contenedor de Jenkins

`docker start jenkins`

4. Conectarse al servicio de ArgoCD 

`kubectl port-forward svc/argocd-server -n argocd 8081:443`

5. Abrir la aplicacion en el navegador

`minikube service mi-app-service`