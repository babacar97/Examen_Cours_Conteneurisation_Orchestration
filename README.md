Sujets d'examen (Semestre 3, Master 2 MICDA)

1. Sujet Session normale :

Le déploiement d’une application avec Kubernetes permettant d'automatiser la gestion, le
déploiement et la mise à l’échelle des pods.

Description

L'objectif est de créer un cluster Kubernetes et de déployer une application conteneurisée avec
Kubernetes.

Travail à réaliser :

 Écrire un fichier manifest pour objet kubernetes à déployer.

Utiliser des images docker officielles ou customiser l'image si nécessaire.

Externaliser la configuration avec des ConfigMaps/Secrets.

Faire persister les données de l'application à travers les PV/PVC.

Exposer le service en le rendant accessible hors du cluster Kubernetes.

Activer l'auto scaling des pods (HPA) basé sur l’utilisation du CPU avec minReplicas:2
           maxReplicas: 10.

Sauvegarder tous les objets Kubernetes déployés dans un fichier backup.yaml .

Partie Kubernetes :

Avoir une application conteneurisée (Docker).

Installer Kubectl (l'outil de ligne de commande Kubernetes).

Un cluster Kubernetes opérationnel (Minikube, Kind, k3s, AKS, GKE, EKS, etc.).
