**Docker Networking**

When Docker installs, it automatically creates 3 networks:

* bridge(default)
* host
* none



1. **Bridge Network(default)**
* Every container gets a private IP(like 172.17.x.x)
* Containers can talk to each other.
* External access needs port mapping.
* Ex: Container runs inside its own small private network.





2\. **Host Network**

* Container uses your real machine's network directly.
* No isolation
* No need for port mapping



3\. **None Network**

* No internet
* No communication
* Fully isolated container





**Custom Network**

*docker network create \\*

&#x20; *--driver bridge \\*

&#x20; *--subnet 182.18.0.0/16 \\*

&#x20; *my-network*

Used to separate groups of containers



* *docker network ls* : list networks
* *docker inspect container\_name* : inspect container network .





































































