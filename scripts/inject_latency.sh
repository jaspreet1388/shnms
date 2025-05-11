#!/bin/bash
POD_NAME=$(kubectl get pods -l app=shnms -o jsonpath="{.items[0].metadata.name}")
kubectl exec -it $POD_NAME -- tc qdisc add dev eth0 root netem delay 800ms
