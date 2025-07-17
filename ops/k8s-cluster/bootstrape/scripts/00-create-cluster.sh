kind create cluster --config=../../kind-cluster-config.yaml --name=devops-lab

kind load docker-image metrics-visualizer:1.0.1 --name=devops-lab
