# 🚀 DevOps CI/CD Pipeline Project

<p align="center">
  <img src="https://img.shields.io/badge/Jenkins-CI/CD-red?style=for-the-badge&logo=jenkins"/>
  <img src="https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker"/>
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-blue?style=for-the-badge&logo=kubernetes"/>
  <img src="https://img.shields.io/badge/Python-Flask-yellow?style=for-the-badge&logo=python"/>
</p>

<p align="center">
  <b>Automated Build • Containerization • Kubernetes Deployment</b>
</p>

---

## 📌 Overview

This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, and Kubernetes.  
The application is automatically built, containerized, and deployed on a Kubernetes cluster.

---

## 🏗️ Architecture

<p align="center">
  <img src="downloads/flow.png" width="700"/>
</p>

---

## 🔄 Workflow


GitHub → Jenkins → Docker → Kubernetes → Application


---

## 📁 Project Structure


app.py

requirements.txt

Dockerfile

Jenkinsfile

deployment.yaml

service.yaml

README.md


---

## 🚀 Getting Started

### Clone Repository

git clone https://github.com/varshpawar/devops-project.git

cd devops-project


### Build Docker Image

docker build -t my-app .


### Run Container

docker run -p 3000:3000 my-app


---

## ☸️ Kubernetes Deployment


kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl get pods


---

## 🌐 Application Access


http://<node-ip>:3000

---

## ✨ Key Features

- Automated CI pipeline using Jenkins  
- Docker containerization  
- Kubernetes deployment  
- Webhook-based automation  
- Scalable architecture  
