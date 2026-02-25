import tensorflow as tf

print("GPU available:", tf.config.list_physical_devices('GPU'))
print("Hello from Docker!")