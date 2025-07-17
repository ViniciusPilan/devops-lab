kind create cluster --config=../../kind-cluster-config.yaml --name=devops-lab

kind load docker-image metrics-vis:1.0.0 --name=devops-lab
