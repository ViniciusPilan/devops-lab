#!/bin/bash

kubectl apply -n argocd -f ../../../argo/00-install.yaml
sleep 120
kubectl apply -n argocd -f ../../../argo/01-all-applications.yaml

# kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
# kubectl -n argocd port-forward svc/argocd-server 8080:80