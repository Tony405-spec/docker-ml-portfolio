# My ML Docker Image Inventory

## Images I Have
- postgres:13 (618MB) - python:3.9-slim (183MB) - tensorflow/tensorflow:latest (2.85GB) - codewars-scraper:latest (255MB) - tensorflow/serving:latest (915MB) - hello-world:latest (20.4kB) - python:3.8-slim (189MB) - jupyter/datascience-notebook:latest (8.31GB) - jupyter/tensorflow-notebook:latest (7.93GB) - jupyter/scipy-notebook:latest (5.76GB) - tensorflow/tensorflow:2.13.0-gpu (9.98GB) - tensorflow/tensorflow:2.13.0 (2.25GB) - tonykenga405/cifar10-env:2.13 (2.25GB) - tonykenga405/cifar10-env:latest (2.25GB) - tonykenga405/cifar10-env:stable (2.25GB) - tonykenga405/cifar10-env:tf2.13 (2.25GB) - tensorflow/tensorflow:2.12.0 (2.42GB) - bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8 (2.05GB) - bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8 (2.05GB)

## Images I Want to Try
- [ ] pytorch/pytorch:latest (PyTorch)
- [ ] nvcr.io/nvidia/tensorflow:latest (NVIDIA optimized)
- [ ] huggingface/transformers-pytorch-gpu (Transformers)

## For CIFAR-10 Project
- Base: YOUR_USERNAME/cifar10-env:tf2.13 ✅
- Jupyter: jupyter/tensorflow-notebook:latest ✅
- Serving: tensorflow/serving:latest (for Week 7-8)

## Notes
- Always pin versions for reproducibility
- GPU images are larger but faster training
- Jupyter images great for exploration
