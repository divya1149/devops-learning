**Docker Registry**

Place where Docker images are stored and shared



1. **Docker Hub (default registry)**
* Default public registry: Docker Hub
* Docker automatically pulls images from here.
* Ex: docker run nginx
* This actually means: docker.io/library/nginx  (library/= official images)



**2. Private Registry**

* Used for company/internal images
* Requires login: docker login private-registry.io
* Then run image: docker run private-registry.io/my-app



**3. Cloud Registries**

Used for secure production deployments



**4. Create you own registry(on-premise)**

Docker itself provides a registry image: *docker run -d -p 5000:5000 --name registry registry:2*



**Push image to your registry**

1. Tag image: docker image tag my-image localhost:5000/my-image
2. Push: docker push localhost:5000/my-image



**Push image:** docker pull localhost:5000/my-image

