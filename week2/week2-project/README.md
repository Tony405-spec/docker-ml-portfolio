# 🎯 CIFAR-10 Training Environment
### Complete Shareable Package for Image Classification

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Python](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge&logo=python&logoColor=ffdd54)

## 📋 Overview
This package provides a **completely reproducible environment** for CIFAR-10 image classification using TensorFlow 2.13.0.

## 🚀 Quick Start

### Pull from Docker Hub
`ash
docker pull tonykenga405/cifar10-env:tf2.13
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "import tensorflow as tf; print(f'TensorFlow {tf.__version__} ready!')"
docker run --rm -v \C:\Users\Administrator\docker-ml-portfolio\week2\week2-project:/workspace -w /workspace tonykenga405/cifar10-env:tf2.13 python verify.py
docker run --rm -v \C:\Users\Administrator\docker-ml-portfolio\week2\week2-project:/workspace -w /workspace tonykenga405/cifar10-env:tf2.13 python quick_test.py
Author
Tony Kenga - @tonykenga405
Project Link: https://github.com/tonykenga405/docker-ml-portfolio
