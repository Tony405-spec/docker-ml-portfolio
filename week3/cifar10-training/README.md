# Week 3: Custom Docker Image for CIFAR-10 Training

## 👤 Author
**tonykenga405**

## 📦 Docker Image
	tonykenga405/cifar10-trainer:latest

## 🚀 Quick Start

### Pull the image
`ash
docker pull tonykenga405/cifar10-trainer:latest
docker run --rm tonykenga405/cifar10-trainer:latest
docker run --rm tonykenga405/cifar10-trainer:latest python train.py --epochs 5 --batch-size 64 --seed 123
docker build -t tonykenga405/cifar10-trainer:latest .
