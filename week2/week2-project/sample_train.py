import tensorflow as tf
import time

print('Mini Training Test')
print('='*40)

# Load small subset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train[:1000]/255.0, x_test[:200]/255.0
y_train, y_test = y_train[:1000], y_test[:200]

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, 3, activation='relu', input_shape=(32,32,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
start = time.time()
model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test), verbose=1)
train_time = time.time() - start

print(f'Training completed in {train_time:.2f} seconds')
print('Environment works!')
