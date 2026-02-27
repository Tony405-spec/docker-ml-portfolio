# ============================================
# CIFAR-10 Training Dockerfile
# Author: tonykenga405
# Date: 2026-02-27
# ============================================

# Use official TensorFlow image
FROM tensorflow/tensorflow:2.13.0

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy training script
COPY train.py .

# Default command
CMD ["python", "train.py", "--epochs", "1"]

# Metadata
LABEL maintainer="tonykenga405" \
      version="1.0" \
      description="CIFAR-10 training environment"
