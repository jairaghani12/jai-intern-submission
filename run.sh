#!/bin/bash

# Update and install Docker & Git
sudo apt update
sudo apt install -y docker.io git

# Clone repo
git clone https://github.com/jairaghani12/jai-intern-submission
cd dockerized-webapp-ec2

# Build and run container
sudo docker build -t todo-api .
sudo docker run -d -p 5000:5000 todo-api
chmod +x run.sh
