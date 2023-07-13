# Project Title

Docker and Kubernetes Exercise

## Introduction

The goal of this exercise is to gain hands-on experience with Docker and get acquainted with the basics of Kubernetes.

## Steps

### Step 1: Docker Image Creation

In this step, you will create a Docker image based on a Linux distribution. The image should include the necessary tools, such as `curl`, to perform various operations.

### Step 2: Development of a Simple Server

In this step, you will develop a basic server that can handle incoming requests and respond with the hostname and current time. You will need to write the server code and then create a Dockerfile to containerize the project.

### Step 3: Kubernetes Deployment

Now it's time to deploy the project on Kubernetes using Minikube. You will need to write the required deployment files, including a Config Map, Deployment, and Service. These files will define the desired state of the application and how it should be managed within the cluster.

## Execution

Follow the steps below to execute the project:

1. Build the Docker image: `docker build -t image-name .`
2. Run the Docker container: `docker run -d -p 8080:8080 image-name`
3. Access the server by sending requests to `http://localhost:8080`

To deploy the project on Kubernetes using Minikube:

1. Ensure Minikube is installed and running.
2. Apply the Kubernetes deployment files: `kubectl apply -f deployment.yaml`
3. Access the deployed application using the exposed service.

Please note that you may need to customize the deployment files, such as specifying container image names and ports, to align with your project's requirements.

## Conclusion

By completing this exercise, you will have gained practical experience with Docker and Kubernetes, enabling you to containerize applications and deploy them on a Kubernetes cluster.
