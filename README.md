<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Kubernetes_logo_without_workmark.svg/1234px-Kubernetes_logo_without_workmark.svg.png" alt="Logo" width="80" height="80">
  <h1>Kubernetes Lab Deployment</h1>
  <p>This repository contains configurations to deploy a Kubernetes lab environment, including a vulnerable RCE application and other services.</p>
</div>


## Contents
- `pods.yaml`: Pod definitions, including the RCE app and additional services.
- `service.yaml`: Service definition to expose the RCE app.
## Requirements
- Kubernetes Cluster
- `kubectl` installed and configured
## Architecture
​![IMG_1725](https://github.com/user-attachments/assets/88d094fd-e0f3-4464-923c-6ac0323cc795)
## (Optional) Setup Local Kubernetes Cluster

### 0.1 Create Kubernetes Cluster
```bash
limactl create --name=k8s template://k8s
```
### 0.2 Set Environment Variable
- Fish Shell
```fish
set -x LIMA_INSTANCE k8s
```
- Bash Shell
```bash
export LIMA_INSTANCE=k8s
```
### 0.3 Access Kubernetes Cluster
```bash
limactl shell k8s
```
## Deploy Infrastructure
### 1. Deploy Pods
This command deploys the pods defined in pods.yaml, including the RCE app and other services.
```bash
kubectl apply -f pods.yaml
```
### 2. Create Service
This creates a service to expose the RCE app internally within the cluster, enabling communication between pods.
```bash
kubectl apply -f service.yaml
```
### 3. Access the Service
This command forwards the local port 8080 to the service's port 80, allowing access to the RCE app through http://localhost:8080.
To access the RCE app, use port forwarding:
```bash
kubectl port-forward service/rce-app-service 8080:80
```
## Testing App
### 1. Execute commands through known vulnerability
This command sends a request to the rce-app and execute commands on the running pod-1 in which the app is running. Due to open vulnerability created in the app, we can use use this as a starting point into our pentest journey
```bash
curl http://localhost:8080/rce?cmd=whoami
```
## Cleanup
### 1. To remove all resources
```bash
kubectl delete -f service.yaml
kubectl delete -f pods.yaml
```
## Notes
This lab is for educational purposes and should be used in a controlled environment. Do not expose the infrastructure to production environments without proper security measures.
Each section explains the purpose of the respective commands, providing a clear rationale for executing each step in the deployment process.
