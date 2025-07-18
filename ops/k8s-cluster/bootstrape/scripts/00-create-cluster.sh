#!/bin/bash

kind create cluster --config=../../kind-cluster-config.yaml --name=devops-lab

kind load docker-image metrics-visualizer:1.0.0 --name=devops-lab
kind load docker-image web-scraper:1.0.0 --name=devops-lab
