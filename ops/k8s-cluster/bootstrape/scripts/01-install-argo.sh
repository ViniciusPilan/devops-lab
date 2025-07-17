#!/bin/bash

kubectl apply -n argocd -f ../../../argo

# kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
# kubectl -n argocd port-forward svc/argocd-server 8080:80