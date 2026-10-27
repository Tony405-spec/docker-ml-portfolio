# Docker ML Portfolio

A four-week learning repository exploring Docker basics and containerized TensorFlow training with CIFAR-10. The work covers image builds and tagging, running training commands in containers, and passing configuration and files through mounted volumes.

This is an educational exercise, not a production MLOps platform. It does not include a deployed service, model performance report, orchestration, or production security controls.

## Learning modules

| Module | Focus | Reference |
|---|---|---|
| Week 1 | Container lifecycle and Docker fundamentals | `WEEK1_SUMMARY.md` |
| Week 2 | Image naming and tagging | `week2/TAGGING_STRATEGY.md` |
| Week 3 | CIFAR-10 training in a TensorFlow container | `week3/cifar10-training/` |
| Week 4 | Configuration and file management | `week4/file-management/` |

## Requirements

- Docker Engine for the container examples
- Python 3.9+ for local scripts
- TensorFlow 2.13 in examples that use TensorFlow; Docker images manage their own dependencies

## Run an example

Build and run the Week 3 example:

```bash
cd week3/cifar10-training
docker build -t cifar10-trainer:local .
docker run --rm cifar10-trainer:local python train.py --epochs 1
```

Build and run the Week 4 configuration example:

```bash
cd week4/file-management/cifar10-file-management
docker build -t cifar10-file-mgmt:local .
docker run --rm cifar10-file-mgmt:local python scripts/train_with_config.py
```

The first CIFAR-10 run may download data from TensorFlow. Check each module's Dockerfile and script for its specific paths and configuration options.

## Validation scripts

`test_tf.py` checks TensorFlow availability and `test_cifar10.py` checks dataset access. These scripts require TensorFlow and may download CIFAR-10. The repository's broader pytest suite also imports TensorFlow in several test modules; it cannot be collected in environments where TensorFlow is absent.

## Repository layout

```text
week2/  image tagging notes
week3/  containerized CIFAR-10 training
week4/  configuration and volume examples
assets/ screenshots and walkthrough media
```

## Limitations

The examples demonstrate local Docker workflows only. They do not establish model quality or deployment readiness. GPU support depends on the host's Docker and NVIDIA runtime configuration. Image optimization and security hardening are not comprehensively benchmarked.
