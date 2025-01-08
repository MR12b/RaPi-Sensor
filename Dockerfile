# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set a maintainer for the image (optional)
# LABEL maintainer="yourname@example.com"

# Update the package list and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    wget \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your application files into the container
COPY . /app

# Install Python dependencies, including opencv-python
RUN pip3 install --no-cache-dir \
    opencv-python \
    numpy

# Expose any necessary ports (if your app uses them)
# EXPOSE 5000  # Example: exposing port 5000 for Flask app

# Set the default command to run your application
# CMD ["python3", "app.py"]

RUN pip3 install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/MR12b/TIK-projekt.git
RUN mkdir img
