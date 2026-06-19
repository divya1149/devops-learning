###### **Kubernetes Deployment Update and Rollback**

* **Deployment Update:** Change your application version. Kubernetes creates new Pods and replaces old ones automatically.
* **Rollout:** The process of updating the application.
* **Revision:** Each update creates a new version history.



###### **Deployment Strategies**

**1 Recreate:** 

* Delete all old Pods first
* Then create new Pods
* Causes downtime


**2 Rolling Update:**

* Replace Pass one by one
* No downtime



###### **Rollback**

* *kubectl rollout undo deployment/myapp-deployment :*Rollback to the previous version
* *kubectl rollout status deployment/myapp-deployment :* check update progress
* *kubectl rollout history deployment/myapp-deployment :* view update history
* *kubectl set image deployment/myapp-deployment nginx-container=nginx:1.9.1 :* update container image

