import tensorflow as tf
import time

print("🔍 Quick CIFAR-10 Test")
print("-" * 40)

start = time.time()
print("Loading CIFAR-10...")
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
load_time = time.time() - start

print(f"✅ Loaded {len(x_train):,} training images")
print(f"✅ Loaded {len(x_test):,} test images")
print(f"⏱️  Load time: {load_time:.2f} seconds")
print(f"📊 Sample shape: {x_train[0].shape}")
print(f"🏷️  Sample label: {y_train[0][0]}")
print("-" * 40)
print("✨ CIFAR-10 is ready for training!")
