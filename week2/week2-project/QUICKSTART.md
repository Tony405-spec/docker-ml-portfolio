# QUICK START GUIDE

## 1. Get the Image
docker pull tonykenga405/cifar10-env:tf2.13

## 2. Test It
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "import tensorflow as tf; print(tf.__version__)"

## 3. Load CIFAR-10
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "from tensorflow.keras.datasets import cifar10; cifar10.load_data(); print('CIFAR-10 ready!')"
