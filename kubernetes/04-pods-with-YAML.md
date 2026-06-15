###### **Pods With YAML**

YAML file is used to define a Pod in Kubernetes.

A Pod YAML file has 4 main fields:

* apiVersion: v1 = Kubernetes API version
* kind: Pod = type of object
* metadata:  

&#x20;        name: myapp-pod = information about Pod9name, labels)

* spec:

&#x20;       containers:

&#x20;       - name: nginx-container

&#x20;           image: nginx = What the Pod should run(containers, images)

* kubectl create -f pod-definition.yml = create Pod
* kubectl get pod = see all Pods
* kubectl describe pod myapp-pod = get detailed Pod information 

