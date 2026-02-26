#!/usr/bin/env python3
\"\"\"CIFAR-10 Environment Verification Script for tonykenga405\"\"\"

import tensorflow as tf
import sys
import platform
from datetime import datetime

def print_header(text):
    print("\n" + "="*60)
    print(f" {text}")
    print("="*60)

def main():
    print_header("CIFAR-10 ENVIRONMENT VERIFICATION")
    
    # System info
    print(f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 System: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    
    # TensorFlow
    print_header("TENSORFLOW")
    print(f"✅ Version: {tf.__version__}")
    
    # GPU Check
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"✅ GPU: Found {len(gpus)} GPU(s)")
        for i, gpu in enumerate(gpus):
            print(f"   GPU {i}: {gpu.name}")
    else:
        print("ℹ️  GPU: Not found (CPU mode)")
    
    # CIFAR-10
    print_header("CIFAR-10 DATASET")
    try:
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
        print(f"✅ Training images: {x_train.shape[0]:,}")
        print(f"✅ Test images: {x_test.shape[0]:,}")
        print(f"✅ Image shape: {x_train.shape[1:]}")
        print(f"✅ Classes: {len(set(y_train.flatten()))}")
        print(f"✅ Data range: [{x_train.min()}, {x_train.max()}]")
    except Exception as e:
        print(f"❌ Failed to load CIFAR-10: {e}")
        return 1
    
    # Quick computation test
    print_header("COMPUTATION TEST")
    try:
        a = tf.constant([[1., 2.], [3., 4.]])
        b = tf.constant([[1., 1.], [0., 1.]])
        c = tf.matmul(a, b)
        print(f"✅ Matrix multiplication successful")
        print(f"   Result:\n{c.numpy()}")
    except Exception as e:
        print(f"❌ Computation failed: {e}")
        return 1
    
    print_header("✅ ENVIRONMENT READY FOR CIFAR-10 TRAINING!")
    print("\n🚀 You can now run: python sample_train.py")
    print("="*60 + "\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
