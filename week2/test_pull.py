import tensorflow as tf
print('Testing CIFAR-10 access in pulled image...')
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(f'Success! Training data shape: {x_train.shape}')
print('Image works perfectly!')
