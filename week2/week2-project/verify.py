import tensorflow as tf
import sys

print('='*50)
print('CIFAR-10 Environment Verification')
print('='*50)

# Check TensorFlow
print(f'TensorFlow version: {tf.__version__}')

# Check Python
print(f'Python version: {sys.version.split()[0]}')

# Load CIFAR-10
print('Loading CIFAR-10...')
(x_train, _), _ = tf.keras.datasets.cifar10.load_data()
print(f'Success! {len(x_train)} training images')
print('='*50)
print('Environment ready!')
