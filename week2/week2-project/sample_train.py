import tensorflow as tf
import time
import numpy as np

print("🧪 CIFAR-10 Mini Training Test")
print("=" * 50)

# Load data
print("📦 Loading CIFAR-10...")
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# Take small subset for quick test
x_train_small = x_train[:1000]
y_train_small = y_train[:1000]
x_test_small = x_test[:200]
y_test_small = y_test[:200]

print(f"Training on {len(x_train_small)} samples")
print(f"Testing on {len(x_test_small)} samples")

# Build tiny model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, 3, activation='relu', input_shape=(32,32,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# Train
print("\n🚀 Starting training (1 epoch)...")
start = time.time()
history = model.fit(x_train_small, y_train_small, 
                    epochs=1, 
                    validation_data=(x_test_small, y_test_small),
                    verbose=1)
train_time = time.time() - start

# Results
print("=" * 50)
print(f"✅ Training complete in {train_time:.2f} seconds")
print(f"📈 Training accuracy: {history.history['accuracy'][0]:.4f}")
print(f"📊 Validation accuracy: {history.history['val_accuracy'][0]:.4f}")
print("=" * 50)
print("🎯 Environment is ready for full CIFAR-10 training!")
