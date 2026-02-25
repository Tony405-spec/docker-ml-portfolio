# ML Image Tagging Strategy

## Tag Convention for CIFAR-10 Project
- :tf2.13 - Specific TensorFlow version (most reproducible)
- :2.13 - Short version (convenient)
- :latest - Most recent stable build
- :stable - Production-ready version
- :gpu-2.13 - GPU-enabled version (future)

## Best Practices
1. Always pin specific versions for reproducibility
2. Use 'latest' only for development
3. Document what each tag means
4. Never overwrite published tags (immutable tags)

## Industry Standard
Companies like Google use:
- tensorflow/tensorflow:2.13.0-gpu
- tensorflow/tensorflow:2.13.0
- tensorflow/tensorflow:nightly
