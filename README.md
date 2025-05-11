
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
   git clone [https://github.com/yourusername/shnms.git](https://github.com/jaspreet1388/shnms/blob/3886162b60e08e591c175a0e01c8fe973053b2da/README.md)
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

![image](https://github.com/user-attachments/assets/ba34d68c-c74b-4175-b8fe-8fd010f5461f)


# Remove latency
./scripts/remove_latency.sh
![image](https://github.com/user-attachments/assets/129fa6fe-e5cc-4385-b824-8bbd2c9413a0)

# delpoyments

![image](https://github.com/user-attachments/assets/c872b3e6-e559-4983-b71a-fc60008ed45c)

![image](https://github.com/user-attachments/assets/45f8f87a-7194-44fb-866f-129947f51b8a)


# Network Testing

![image](https://github.com/user-attachments/assets/92b136b9-5795-403d-a913-01c9f7ecfb0d)

![image](https://github.com/user-attachments/assets/635e7143-7875-47f0-8d2a-52df51e10324)

