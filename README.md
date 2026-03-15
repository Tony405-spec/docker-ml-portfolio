<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=28&duration=3000&pause=1000&color=FF073A&center=true&vCenter=true&width=1000&lines=%23+Day2+:+Container+Run+Modes;docker+run+-d+--name+tf-background;tensorflow%2Ftensorflow%3A2.13.0+sleep+300;docker+exec+tf-background+python+-c;import+tensorflow+as+tf;+print(tf.__version__)" alt="Typing SVG" />
</p>

# Docker ML Portfolio

This repository captures a four-week learning journey focused on Docker fundamentals and ML workflows using TensorFlow and the CIFAR-10 dataset. Each week includes project notes, Dockerfiles, and scripts that build toward reproducible containerized training.

## Recommended Workflow

1. **Pick the week you want to work on**
   - Week 1: Fundamentals recap (`WEEK1_SUMMARY.md`)
   - Week 2: Image management (`week2/`)
   - Week 3: CIFAR-10 training (`week3/cifar10-training/`)
   - Week 4: File management patterns (`week4/file-management/`)

2. **Set up a local Python environment (optional)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   If you prefer to avoid local TensorFlow installs, run tests and training inside the Docker images described below.

3. **Run quick validation checks**
   ```bash
   python test_tf.py
   python test_cifar10.py
   ```

4. **Build and run Docker images for hands-on work**
   ```bash
   # Week 3: training image
   cd week3/cifar10-training
   docker build -t cifar10-trainer:local .
   docker run --rm cifar10-trainer:local python train.py --epochs 1

   # Week 4: file management image
   cd ../../week4/file-management/cifar10-file-management
   docker build -t cifar10-file-mgmt:local .
   docker run --rm cifar10-file-mgmt:local python scripts/train_with_config.py
   ```

5. **Document outcomes and tag images**
   - Record weekly outcomes in the relevant `WEEK*_SUMMARY.md` or week README.
   - Apply consistent tags when pushing to Docker Hub (see `week2/TAGGING_STRATEGY.md`).
