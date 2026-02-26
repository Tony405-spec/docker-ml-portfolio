# ⚡ QUICK START GUIDE - CIFAR-10 Environment

## Step 1: Get the Image
`powershell
docker pull tonykenga405/cifar10-env:tf2.13
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "import tensorflow as tf; print(tf.__version__)"
docker run --rm tonykenga405/cifar10-env:tf2.13 python -c "
from tensorflow.keras.datasets import cifar10
(x_train, _), _ = cifar10.load_data()
print(f'✅ Loaded {len(x_train)} CIFAR-10 images')
"
# Create a test file
echo 'import tensorflow as tf
(x_train, _), _ = tf.keras.datasets.cifar10.load_data()
print(f"Ready to train on {len(x_train)} images!")' > test.py

# Run it
docker run --rm -v C:\Users\Administrator\docker-ml-portfolio\week2\week2-project:/workspace -w /workspace tonykenga405/cifar10-env:tf2.13 python test.py
