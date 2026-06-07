**Environment Variables**

* Environment variables are external settings given to an application.
* They allow us to change configuration without changing code .



**Problem Without Env Variables:**

* Color is fixed in code: code="red"
* If you want to change color → must edit code



**Solution Using Env Variables:**

*import os*

*color= os.environ.get("APP\_COLOR")*



* *export APP\_COLOR=blue; python app.py  -* run python app without changing code 
* *docker run -e APP\_COLOR=blue simple-webapp-color -* Pass variable while running container
* *docker inspect container\_name* -   Show all env variables inside containers

