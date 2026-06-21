###### **Kubernetes Networking**

* Every Node (computer/VM) has its own IP address. Ex: 192.168.1.2
* Every Pod also gets its own IP  address. Ex: 10.244.0.2
* Pods communicate with each other using their IP addresses .
* Pod IPs are temporary . If a pod is deleted and recreated , its IP may change .
* In a single-node cluster, all pods run on one machine and communicate easily.
* In a multi-node cluster , pods run  on different nodes. They still need to communicate with each other.
* Kubernetes requires: 1 Any pod can talk to any other Pod 2 Nodes can talk to pods 3 No NAT is needed between pods
* Kubernetes itself does not handle this networking automatically.
* Special networking tools called CNI plugins provide networking such as Flannel , Calico, Weave Net, Cilium.
* These tools give unique IP addresses to all pods and allow communication across all nodes.



