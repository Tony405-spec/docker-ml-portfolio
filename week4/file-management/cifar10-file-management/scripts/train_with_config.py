import tensorflow as tf
import configparser
import os
import sys

print("="*60)
print("CIFAR-10 Training with Config File")
print("="*60)

# Read config file
config = configparser.ConfigParser()
config_path = '/app/config/training.conf'

if os.path.exists(config_path):
    config.read(config_path)
    print(f"✅ Loaded config from {config_path}")
    
    # Get values
    epochs = config.getint('training', 'epochs')
    batch_size = config.getint('training', 'batch_size')
    dropout = config.getfloat('model', 'dropout_rate')
    
    print(f"📋 Configuration:")
    print(f"   Epochs: {epochs}")
    print(f"   Batch size: {batch_size}")
    print(f"   Dropout: {dropout}")
else:
    print(f"❌ Config file not found at {config_path}")
    sys.exit(1)

# Load CIFAR-10
print("\n📦 Loading CIFAR-10...")
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(f"✅ Training: {x_train.shape[0]} images")
print(f"✅ Test: {x_test.shape[0]} images")

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(32,32,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(dropout),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train
print("\n🚀 Training...")
history = model.fit(
    x_train, y_train,
    batch_size=batch_size,
    epochs=epochs,
    validation_data=(x_test, y_test),
    verbose=1
)

# Save model
model_path = '/app/models/cifar10_model.h5'
model.save(model_path)
print(f"\n💾 Model saved to {model_path}")

# List files in models directory
print("\n📁 Files in /app/models:")
os.system('ls -la /app/models/')

print("\n✅ Training complete!")
