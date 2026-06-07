**CMD**

* Default command for container
* Can be easily overridden
* Dockerfile:   CMD\["sleep" ' "5"]

&#x20;    docker run image sleep 10



**ENTRYPOINT**

* Fixed main command
* Only arguments can change
* Dockerfile:  ENTRYPOINT \["sleep"] 

&#x20;                       CMD \["5"]

&#x20;    docker run image 10



**Override ENTRYPOINT:** docker run --entrypoint sleep2.0 image 10

