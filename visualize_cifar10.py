import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Load CIFAR-10
(x_train, y_train), _ = tf.keras.datasets.cifar10.load_data()

# Class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Plot first 9 images
plt.figure(figsize=(10,10))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(x_train[i])
    plt.title(class_names[y_train[i][0]])
    plt.axis('off')

plt.savefig('/workspace/cifar10_samples.png')
print('Image saved as cifar10_samples.png')
