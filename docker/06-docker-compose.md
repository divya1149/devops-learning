**Docker Compose**

* Tools to run multiple containers together.
* Uses one file: docker-compose.yml



**Docker Compose File(YAML)**

services:

&#x20; web:

&#x20;    image: voting-app

&#x20;  redis:

&#x20;    image: redis

&#x20;  db:

&#x20;    image: postgres



* *docker-compose up* - starts all containers together

