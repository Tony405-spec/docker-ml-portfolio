import tensorflow as tf
import numpy as np
import argparse
import os

print("="*60)
print("CIFAR-10 TRAINING - Week 3")
print("="*60)

# Parse arguments
parser = argparse.ArgumentParser(description='Train CIFAR-10 model')
parser.add_argument('--epochs', type=int, default=1, help='number of epochs')
args = parser.parse_args()

print(f"\n📋 Configuration:")
print(f"   Epochs: {args.epochs}")
print(f"   TensorFlow: {tf.__version__}")

# Load CIFAR-10
print("\n📦 Loading CIFAR-10 dataset...")
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Normalize
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

print(f"✅ Training images: {x_train.shape[0]}")
print(f"✅ Test images: {x_test.shape[0]}")
print(f"✅ Image shape: {x_train.shape[1]}x{x_train.shape[2]}")

# Build simple model
print("\n🔧 Building model...")
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# Train
print(f"\n🚀 Training for {args.epochs} epoch(s)...")
history = model.fit(
    x_train, y_train,
    batch_size=32,
    epochs=args.epochs,
    validation_data=(x_test, y_test),
    verbose=1
)
# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\n📊 Test accuracy: {test_acc:.4f}")

print("\n" + "="*60)
print("✅ TRAINING COMPLETE!")
print("="*60)
