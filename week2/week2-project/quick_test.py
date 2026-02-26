import tensorflow as tf
import time

print('Quick CIFAR-10 Test')
print('-'*30)

start = time.time()
(x_train, _), _ = tf.keras.datasets.cifar10.load_data()
load_time = time.time() - start

print(f'Loaded {len(x_train)} images in {load_time:.2f} seconds')
print(f'Image shape: {x_train[0].shape}')
print('-'*30)
print('CIFAR-10 is ready!')
