# MLOps GitOps - Sentiment Analysis on OpenShift 
 
End-to-end MLOps pipeline deploying a Sentiment Analysis API across dev/test/prod namespaces on OpenShift using GitOps principles. 
 
## Tech Stack 
 
- ML Model: HuggingFace Transformers DistilBERT 
- API Framework: FastAPI 
- Containerization: Docker 
- GitOps Controller: ArgoCD 
- Config Management: Kustomize 
- CI Pipeline: GitHub Actions 
- Platform: OpenShift Local CRC 
 
## Project Structure 
 
- app/ - FastAPI ML serving app + Dockerfile 
- manifests/base/ - Common Kubernetes manifests 
- manifests/overlays/dev/ - Dev environment config 
- manifests/overlays/test/ - Test environment config 
- manifests/overlays/prod/ - Prod environment config 
- argocd/ - ArgoCD Application CRs 
- .github/workflows/ - GitHub Actions CI pipeline 
 
## Environments 
 
- dev: 1 replica, DEBUG logs, ocp-dev-1 namespace 
- test: 2 replicas, INFO logs, ocp-test-1 namespace 
- prod: 3 replicas, WARNING logs, ocp-prod-1 namespace 
 
## API Endpoints 
 
- GET / - App info 
- GET /health - Liveness check 
- GET /ready - Readiness check 
- POST /predict - Run sentiment prediction 
 
## Author 
 
Vardhaa - MLOps and DevOps portfolio project 
