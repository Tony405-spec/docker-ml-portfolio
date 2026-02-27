# Week 4: File Management in Docker

## What I Learned

### 1. Copying Files
`dockerfile
COPY file.txt /path/in/image/
COPY folder/ /app/folder/
### . Multiple Copy Operations
Copy config files separately

Copy scripts separately

Copy data separately
### .dockerignore
Excludes unnecessary files from the build context:

Log files

Temporary files

Large model files

Git folders
### File Permissions
RUN chmod +x /app/scripts/*.py
### This Week's Project
Created configuration file outside image

Copied it into image during build

Training script reads config at runtime

Model saved to mounted volume
### Commands Used
# Build
docker build -t tonykenga405/cifar10-file-mgmt:latest .

# Run
docker run --rm -v C:\Users\Administrator\docker-ml-portfolio\week4\file-management\cifar10-file-management/models:/app/models tonykenga405/cifar10-file-mgmt:latest
