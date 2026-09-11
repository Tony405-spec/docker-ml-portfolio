import argparse
import random

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Train CIFAR-10 model")
    parser.add_argument("--epochs", type=int, default=1, help="number of epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="training batch size")
    parser.add_argument("--seed", type=int, default=42, help="random seed for reproducible runs")
    return parser.parse_args(argv)


def validate_args(args):
    if args.epochs < 1:
        raise ValueError("--epochs must be at least 1")
    if args.batch_size < 1:
        raise ValueError("--batch-size must be at least 1")


def configure_seed(seed, tf):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def build_model(tf):
    return tf.keras.Sequential(
        [
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


def main(argv=None):
    args = parse_args(argv)
    validate_args(args)

    import tensorflow as tf

    configure_seed(args.seed, tf)

    print("=" * 60)
    print("CIFAR-10 TRAINING - Week 3")
    print("=" * 60)
    print("\nConfiguration:")
    print(f"   Epochs: {args.epochs}")
    print(f"   Batch size: {args.batch_size}")
    print(f"   Seed: {args.seed}")
    print(f"   TensorFlow: {tf.__version__}")

    print("\nLoading CIFAR-10 dataset...")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    print(f"Training images: {x_train.shape[0]}")
    print(f"Test images: {x_test.shape[0]}")
    print(f"Image shape: {x_train.shape[1]}x{x_train.shape[2]}")

    print("\nBuilding model...")
    model = build_model(tf)

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.summary()

    print(f"\nTraining for {args.epochs} epoch(s)...")
    model.fit(
        x_train,
        y_train,
        batch_size=args.batch_size,
        epochs=args.epochs,
        validation_data=(x_test, y_test),
        verbose=1,
    )

    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"\nTest accuracy: {test_acc:.4f}")

    print("\n" + "=" * 60)
    print("TRAINING COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
