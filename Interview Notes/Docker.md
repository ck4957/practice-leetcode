# Containers
Containers are a way of packaging software. All of your application’s code, libraries, and dependencies are packed together in the container as an immutable artifact.

# Docker
With Docker, you create a special file called a Dockerfile. 

Dockerfiles define a build process, which, when fed to the ‘docker build’ command, will produce an immutable docker image. 

You can think of this as a snapshot of your application, ready to be brought to life at any time. 

When you want to start it up, just use the ‘docker run’ command to run it anywhere the docker daemon is supported and running. 

It can be on your laptop, your production server in the cloud, or on a raspberry pi. Regardless of where your image is running, it will behave the same way. 

# Docker Hub (Swarm)
Docker also provides a cloud-based repository called Docker Hub. You can think of it like GitHub for Docker Images. You can use Docker Hub to store and distribute the container images you build.