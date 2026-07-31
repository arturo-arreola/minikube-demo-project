# Mini Proyecto GitOps: Minikube, Jenkins y ArgoCD

Este repositorio contiene un laboratorio práctico de una arquitectura CI/CD basada en GitOps.

## Arquitectura y Herramientas

* **Aplicacion:** Python (Flask)
* **Contenerización:** Docker & Docker Hub
* **Cluster Local:** Minikube
* **Integración Continúa:** Jenkins (Contenedor de Docker)
* **Despliegue Continuo:** ArgoCD (Dentro del clúster)
* **Versionado de Código:** GitHub

---

## Estructura del Proyecto

* `app.py`: Código fuente de la aplicación web de Python.
* `requirements.txt`: Dependencias de la aplicación (Flask).
* `Dockerfile`: Instrucciones para empaquetar la aplicación.
* `Jenkinsfile`: Pipeline declarativo de CI/CD para automatizar la construcción de la imagen y el despliegue.
* `k8s.yaml`: Manifiestos de Kubernetes (Deployment y Service).

---

## Flujo de trabajo

1. Se ejecutan cambios en `app.py` y sube los cambios a GitHub.
2. Se ejecuta el job en Jenkins.
3. Jenkins construye una nueva imagen Docker usando la variable `${BUILD_NUMBER}` y la sube a Docker Hub.
4. Jenkins modifica el archivo `k8s.yaml` inyectando la nueva versión de la imagen y hace un `git push` a ese repositorio.
5. ArgoCD se mantiene en constante vigilancia del repositorio, detecta un cambio en `k8s.yaml`.
6. ArgoCD actualiza los pods en Minikube a través de un Rolling Update.

---

## Instrucciones para levantar el entorno en local

1. Iniciar **Docker Desktop** y esperar a que el motor de Docker este corriendo.

2. Iniciar **Minikube**:
   ```powershell
   minikube start
   ```

3. Levantar el contenedor de **Jenkins**:
   ```powershell
   docker start jenkins
   ```
   (Acceso en http://localhost:8080)

4. Abrir el acceso a **ArgoCD**:
   ```powershell
   kubectl port-forward svc/argocd-server -n argocd 8081:443
   ```
   (Acceso en http://localhost:8081)
   
   Credeciales:
   
   **User**: `admin`
   
   **Password**: `djm4rjOYowhUHhVS`

5. Abrir la aplicación en el navegador:
   ```powershell
   minikube service mi-app-service
   ```