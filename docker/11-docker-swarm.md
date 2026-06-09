**Docker Swarm**

Docker Swarm is a tool that: combines multiple docker machines into one cluster.

Lets you run and manage containers across all machines automatically.



* *docker swarm init --advertise-addr <manager-ip>* = Creates the swarm and gives a join command for workers
* *docker swarm join --token <toke> <manager-ip>:2377 =* Workers join using the command given by manager
* *docker service create --replicas=3 -p 8080:80 my-web-server* = creates 3 running copies of your app and manages them automatically, while making it accessible on port 8080

