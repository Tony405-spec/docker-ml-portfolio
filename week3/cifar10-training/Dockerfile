# ============================================
# CIFAR-10 Training Dockerfile
# Author: tonykenga405
# Date: 2026-02-27
# ============================================

# Use official TensorFlow image
FROM tensorflow/tensorflow:2.13.0

# Create an unprivileged runtime user
RUN useradd --create-home --shell /bin/bash appuser

# Set working directory
WORKDIR /app
RUN chown appuser:appuser /app

# Copy requirements first (for better caching)
COPY --chown=appuser:appuser requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy training script
COPY --chown=appuser:appuser train.py .

# Run training as an unprivileged user
USER appuser

# Default command
CMD ["python", "train.py", "--epochs", "1"]

# Metadata
LABEL maintainer="tonykenga405" \
      version="1.0" \
      description="CIFAR-10 training environment"
