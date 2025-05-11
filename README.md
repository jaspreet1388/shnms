
# SHNMS: Self-Healing Network Monitoring System

SHNMS is a Kubernetes-based system that monitors application health using Prometheus and automatically remediates issues through Alertmanager and custom webhooks. It includes a FastAPI application, Grafana dashboards, and supports network fault injection using `tc`.

## Features

- **FastAPI** application exposing `/health` and `/metrics` endpoints
- **Prometheus** for scraping metrics and triggering alerts
- **Alertmanager** for routing alerts to remediation services
- **Grafana** dashboards for visualizing metrics
- **`tc`** scripts for simulating network latency and packet loss

## Prerequisites

- Kubernetes cluster
- Helm 3
- kubectl configured for your cluster

##  Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/shnms.git
   cd shnms


## Deploy the monitoring stack:

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack

## Deploy SHNMS components:
kubectl apply -f k8s/


## Accessing Dashboards
Prometheus: http://localhost:9090

Grafana: http://localhost:3000


## Simulating Network Latency
Use the provided scripts to inject and remove network latency:

# Inject 800ms latency
./scripts/inject_latency.sh

# Remove latency
./scripts/remove_latency.sh
📄 License
