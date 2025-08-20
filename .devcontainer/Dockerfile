# Base image with Python
FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# Install OpenCV dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y python3-opencv ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install basic scientific libraries
RUN pip install numpy matplotlib jupyter
