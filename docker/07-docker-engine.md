**Docker Engine**

Tool that creates isolated environments(containers) and controls their CPU, memory, and system access safely.



**Parts of Docker Engine**

* **Docker CLI** = type commands like docker run
* **Docker REST API** = sends your commands to Docker
* **Docker Daemon** = actually creates and runs containers



&#x20;**How Containers work?**

* Docker uses Linux namespaces so each container feels like a separate computer(its own processes, network, files,etc)
* Inside a container , it looks like it has its won system, but it actually sharing the host OS.



**Resource control**

* Docker uses cgroups to limit resources

CPU limit: --cpus=0.5 → uses only half CPU

Memory limit: --memory=100m → uses only 100 MB RAM

