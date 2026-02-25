import tensorflow as tf
import numpy as np
print(f'TensorFlow version: {tf.__version__}')

# Load CIFAR-10
print('Loading CIFAR-10...')
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

print(f'Training data shape: {x_train.shape}')
print(f'Test data shape: {x_test.shape}')
print(f'Classes: {np.unique(y_train)}')

# Verify data
print(f'First image min/max: {x_train[0].min()}, {x_train[0].max()}')

print('CIFAR-10 loaded successfully in Docker!')
