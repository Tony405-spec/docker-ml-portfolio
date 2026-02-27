# Week 4: CIFAR-10 with File Management
FROM tensorflow/tensorflow:2.13.0

# Set working directory
WORKDIR /app

# Create directory structure
RUN mkdir -p /app/models /app/outputs /app/data /app/config /app/scripts

# Copy configuration files
COPY config/training.conf /app/config/

# Copy scripts
COPY scripts/train_with_config.py /app/scripts/

# Copy any additional data files
COPY data/ /app/data/

# Install configparser (for reading .conf files)
RUN pip install configparser

# Make scripts executable
RUN chmod +x /app/scripts/*.py

# Set Python path
ENV PYTHONPATH="/app:"

# Default command
CMD ["python", "/app/scripts/train_with_config.py"]

# Metadata
LABEL maintainer="tonykenga405" \
      description="CIFAR-10 with configuration file management"
