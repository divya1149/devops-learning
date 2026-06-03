**Docker Images**

A docker image is ready-made package that contains: application code, required software, libraries and dependencies and configuration files.



**Dockerfile=** Instructions to create image



* FROM: Define base image
* RUN: Executes commands while building the image
* COPY: Copies files from local machine to image
* ENTRYPOINT: Command that runs when container starts



* *docker build -t my-app .* : Build docker image (-t : tag/name the image, . = current directory (contains Dockerfile))
* *docker push username/my-app :* push image to Docker Hub
* *docker history image-name*: Check Image Layers

