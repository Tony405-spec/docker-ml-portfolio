# Docker Tagging Strategy for CIFAR-10 Project

## Tags Available for tonykenga405/cifar10-env

| Tag | Purpose | When to Use |
|-----|---------|-------------|
| 	f2.13 | Exact TensorFlow 2.13.0 | Research, reproducibility |
| latest | Most recent build | Development, quick tests |
| stable | Production-ready | Deployment, sharing |

## Commands to Create Tags
`ash
docker tag tonykenga405/cifar10-env:tf2.13 tonykenga405/cifar10-env:latest
docker tag tonykenga405/cifar10-env:tf2.13 tonykenga405/cifar10-env:stable
docker push tonykenga405/cifar10-env:latest
docker push tonykenga405/cifar10-env:stable
# Research (reproducible)
docker run --rm tonykenga405/cifar10-env:tf2.13 python train.py

# Development (easiest to type)
docker run --rm tonykenga405/cifar10-env:latest python test.py

# Production (tested version)
docker run --rm tonykenga405/cifar10-env:stable python serve.py
