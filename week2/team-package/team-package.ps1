# team-package.ps1
# Script to create complete team sharing package

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Creating Team Sharing Package" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan

# Configuration
\ = "tonykenga405"
\ = "cifar10-env"
\ = "tf2.13"
\ = "\/\:\"

Write-Host "
📦 Creating package for: \" -ForegroundColor Yellow

# Step 1: Save image to tar
Write-Host "
Step 1: Saving image to tar file..." -ForegroundColor Green
docker save -o "\-\.tar" \
Write-Host "✅ Image saved: \-\.tar" -ForegroundColor Green

# Step 2: Create verification script
Write-Host "
Step 2: Creating verification script..." -ForegroundColor Green

# Use single-quoted string for Python content
\ = @'
import tensorflow as tf
import sys

print('='*50)
print('CIFAR-10 Environment Verification')
print('='*50)

print(f'✅ TensorFlow: {tf.__version__}')
print(f'✅ Python: {sys.version}')

print('📦 Loading CIFAR-10...')
(x_train, _), _ = tf.keras.datasets.cifar10.load_data()
print(f'✅ Found {len(x_train)} training images')

print('='*50)
print('Environment is ready! 🚀')
'@

\ | Out-File -FilePath verify.py -Encoding UTF8
Write-Host "✅ Verification script created: verify.py" -ForegroundColor Green

# Step 3: Create quick start guide
Write-Host "
Step 3: Creating quick start guide..." -ForegroundColor Green
\ = @'
# QUICK START GUIDE

## 1. Load the image
docker load -i -.tar

## 2. Verify it works
docker run --rm -v C:\Users\Administrator\docker-ml-portfolio\week2\team-package.Path:/workspace -w /workspace  python verify.py

## 3. Start coding!
'@

\ | Out-File -FilePath QUICKSTART.txt -Encoding UTF8
Write-Host "✅ Quick start guide created: QUICKSTART.txt" -ForegroundColor Green

# Step 4: Show package contents
Write-Host "
📋 Package Contents:" -ForegroundColor Cyan
Get-ChildItem | Format-Table Name, Length

Write-Host "
====================================" -ForegroundColor Cyan
Write-Host "✅ PACKAGE CREATED SUCCESSFULLY!" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "
Share these files with your team:"
Write-Host "  1. -.tar (the image)"
Write-Host "  2. verify.py (test script)"
Write-Host "  3. QUICKSTART.txt (one-page guide)"
Write-Host "
Total size: 0 MB"

