# 🚀 CIFAR-10 Training Environment - Team Package

## Quick Start (2 minutes)

### Option 1: Pull from Docker Hub (Internet required)
`powershell
docker pull tonykenga405/cifar10-env:tf2.13
# If you received the .tar file
docker load -i cifar10-env-tf2.13.tar
# Test TensorFlow
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "import tensorflow as tf; print(tf.__version__)"

# Should output: 2.13.0
# Quick test
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "
import tensorflow as tf
(x_train, _), _ = tf.keras.datasets.cifar10.load_data()
print(f'✅ CIFAR-10 ready! {len(x_train)} images')
"
import tensorflow as tf
print('TensorFlow version:', tf.__version__)
print('CIFAR-10 loading...')
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(f'Training samples: {len(x_train)}')
print(f'Test samples: {len(x_test)}')
print('✅ Environment ready!')
docker run --rm -v C:\Users\Administrator\docker-ml-portfolio\week2\team-package.Path:/workspace -w /workspace tonykenga405/cifar10-env:tf2.13 python test.py
