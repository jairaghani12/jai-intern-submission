Mini Blog App Deployment Using Docker and AWS EC2
DevOps Intern Assignment Final Report

1. Introduction
The goal of this assignment was to build a small web application using Python (Flask), package it using Docker, and deploy it on a cloud server using Amazon EC2. This report documents every step clearly, with explanations and commands used during the entire process.

2. What is This Project About?
This project is a simple Mini Blog web application. The app shows blog posts on the homepage, and clicking on a title opens the full blog post. The main purpose is to demonstrate how to deploy such an app using Docker and AWS EC2.

3. Technologies Used
Python
Flask
Docker
AWS EC2
GitHub
Linux / Ubuntu

4. GitHub Repository
All the code and files for this project are stored in a GitHub repository.
GitHub link: https://github.com/jairaghani12/jai-intern-submission


5. Step-by-Step Instructions
Step 1: Dockerizing the Application
 - Create requirements.txt
   flask==2.2.5

 - Create the Dockerfile:
   FROM python:3.10-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["python", "app.py"]
 
- Build and Run Locally:
   docker build -t mini-blog .
   docker run -d -p 5000:5000 mini-blog

Step 2: Set Up AWS EC2 (Ubuntu Server)
 - Launch EC2 instance (Ubuntu 22.04, t2.micro, port 5000 open)
 - Connect via SSH:
     ssh -i devops-key.pem ubuntu@13.60.45.249:5000


Step 3: Install Docker and Git:
   sudo apt update
   sudo apt install docker.io git -y

Step 4: Clone GitHub Repository:
   git clone https://github.com/your-username/mini_blog.git
   cd mini_blog

Step 5: Build and Run on EC2:
   sudo docker build -t mini-blog .
   sudo docker run -d -p 5000:5000 mini-blog

Access at: http://13.60.45.249:5000

6. Useful Docker Commands Used
sudo docker ps  # list containers
sudo docker build -t myapp .  # build image
sudo docker run -d -p 5000:5000 myapp  # run container

7. Conclusion
This assignment helped in understanding the full cycle of deploying a web application to the cloud. Starting with a basic blog app built using Flask, we learned how to containerize it using Docker and then host it on an AWS EC2 instance. The process covered important steps such as writing clean code, building a Docker image, setting up a virtual server, and running the app live so it can be accessed from anywhere. It also introduced useful tools and services like GitHub, Docker, and AWS.
Overall, this was a valuable learning experience that showed how different parts of a project — coding, containerization, and cloud hosting — come together to make an application available online.

