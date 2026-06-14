###### **Kubernetes Pod**

* A Pod is the smallest unit in Kubernetes.
* A Pod contains one or more containers.
* Kubernetes runs your application inside a pod.
* To handle more users, Kubernetes creates more Pods , not more containers inside same Pod.
* Pods can run on the same node or different nodes in a cluster.

###### 

###### **Multi-Container Pod**

* A Pod can have multiple containers that work together.
* These conatiners: share same network, share storage, communicate using localhost, start and stop together



* *kubectl run nginx --image=nginx*  = creates a Pod running nginx application
* *kubectl get pods* = create pod status 

&#x20;  Possible status:

&#x20;  ContainerCreating → Pod is being created.

&#x20;   Running → Pod is ready and working.

