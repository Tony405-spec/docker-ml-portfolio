import sys
from pathlib import Path

import pytest


SCRIPT_DIR = (
    Path(__file__).resolve().parent
    / "week4"
    / "file-management"
    / "cifar10-file-management"
    / "scripts"
)
sys.path.insert(0, str(SCRIPT_DIR))

from train_with_config import load_training_config


def write_config(tmp_path, training="epochs = 5\nbatch_size = 32", model="dropout_rate = 0.5"):
    config_path = tmp_path / "training.conf"
    config_path.write_text(f"[training]\n{training}\n\n[model]\n{model}\n", encoding="utf-8")
    return config_path


def test_load_training_config_accepts_valid_values(tmp_path):
    config = load_training_config(write_config(tmp_path))

    assert config.epochs == 5
    assert config.batch_size == 32
    assert config.dropout == 0.5


def test_load_training_config_rejects_zero_epochs(tmp_path):
    with pytest.raises(ValueError, match="training.epochs must be at least 1"):
        load_training_config(write_config(tmp_path, training="epochs = 0\nbatch_size = 32"))


def test_load_training_config_rejects_invalid_dropout(tmp_path):
    with pytest.raises(ValueError, match="model.dropout_rate"):
        load_training_config(write_config(tmp_path, model="dropout_rate = 1.2"))


def test_load_training_config_requires_file():
    with pytest.raises(FileNotFoundError, match="Config file not found"):
        load_training_config("missing-training.conf")
