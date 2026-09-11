import configparser
import os
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_CONFIG_PATH = Path("/app/config/training.conf")
DEFAULT_MODEL_PATH = Path("/app/models/cifar10_model.h5")


@dataclass(frozen=True)
class TrainingConfig:
    epochs: int
    batch_size: int
    dropout: float


def load_training_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> TrainingConfig:
    """Load and validate CIFAR-10 training configuration."""
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")

    config = configparser.ConfigParser()
    config.read(config_path)

    try:
        epochs = config.getint("training", "epochs")
        batch_size = config.getint("training", "batch_size")
        dropout = config.getfloat("model", "dropout_rate")
    except (configparser.Error, ValueError) as exc:
        raise ValueError("training.conf must define numeric training and model settings") from exc

    if epochs < 1:
        raise ValueError("training.epochs must be at least 1")
    if batch_size < 1:
        raise ValueError("training.batch_size must be at least 1")
    if not 0 <= dropout < 1:
        raise ValueError("model.dropout_rate must be greater than or equal to 0 and less than 1")

    return TrainingConfig(epochs=epochs, batch_size=batch_size, dropout=dropout)


def train(config: TrainingConfig, model_path: str | Path = DEFAULT_MODEL_PATH) -> None:
    """Train the CIFAR-10 model using a validated configuration."""
    import tensorflow as tf

    print("\nLoading CIFAR-10...")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    print(f"Training: {x_train.shape[0]} images")
    print(f"Test: {x_test.shape[0]} images")

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(32, 32, 3)),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(64, 3, activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dropout(config.dropout),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    print("\nTraining...")
    model.fit(
        x_train,
        y_train,
        batch_size=config.batch_size,
        epochs=config.epochs,
        validation_data=(x_test, y_test),
        verbose=1,
    )

    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    model.save(model_path)
    print(f"\nModel saved to {model_path}")

    print(f"\nFiles in {model_path.parent}:")
    os.system(f"ls -la {model_path.parent}")


def main() -> int:
    print("=" * 60)
    print("CIFAR-10 Training with Config File")
    print("=" * 60)

    try:
        config = load_training_config()
    except (FileNotFoundError, ValueError) as exc:
        print(f"Config error: {exc}")
        return 1

    print(f"Loaded config from {DEFAULT_CONFIG_PATH}")
    print("Configuration:")
    print(f"   Epochs: {config.epochs}")
    print(f"   Batch size: {config.batch_size}")
    print(f"   Dropout: {config.dropout}")

    train(config)
    print("\nTraining complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
