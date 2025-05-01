# Démarrer Minikube
minikube start

# Configurer Docker pour utiliser le démon de Minikube
minikube -p minikube docker-env | Invoke-Expression

# Construire l'image Docker de l'application Flask
docker build -t flask-k8s-app .

# Déployer l'application avec Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Accéder au service via Minikube
minikube service flask-k8s-service
