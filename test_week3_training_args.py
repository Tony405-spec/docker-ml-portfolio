import sys
from argparse import Namespace
from pathlib import Path

import pytest


SCRIPT_DIR = Path(__file__).resolve().parent / "week3" / "cifar10-training"
sys.path.insert(0, str(SCRIPT_DIR))

from train import parse_args, validate_args


def test_parse_args_includes_batch_size_and_seed():
    args = parse_args(["--epochs", "3", "--batch-size", "64", "--seed", "123"])

    assert args.epochs == 3
    assert args.batch_size == 64
    assert args.seed == 123


def test_parse_args_defaults_are_reproducible():
    args = parse_args([])

    assert args.epochs == 1
    assert args.batch_size == 32
    assert args.seed == 42


def test_validate_args_rejects_invalid_epochs():
    with pytest.raises(ValueError, match="--epochs must be at least 1"):
        validate_args(Namespace(epochs=0, batch_size=32))


def test_validate_args_rejects_invalid_batch_size():
    with pytest.raises(ValueError, match="--batch-size must be at least 1"):
        validate_args(Namespace(epochs=1, batch_size=0))
