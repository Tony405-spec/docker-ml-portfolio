# Week 4: File Management Demo
FROM alpine:latest

# Create directories in image
RUN mkdir -p /app/scripts /app/config /app/data /app/output

# Copy single file
COPY scripts/hello.py /app/scripts/

# Copy entire folders
COPY config/ /app/config/
COPY data/ /app/data/

# Copy with rename
COPY scripts/hello.py /app/hello_world.py

# Set working directory
WORKDIR /app

# List files to verify (during build)
RUN ls -la /app/
RUN ls -la /app/scripts/
RUN ls -la /app/config/
RUN ls -la /app/data/

# Default command
CMD ["sh", "-c", "echo 'Files in image:' && ls -la /app/ && python /app/scripts/hello.py 2>/dev/null || echo 'Python not available'"]
