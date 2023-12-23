
![](https://ckeditor.com/apps/ckfinder/userfiles/files/image(4).png)

About
-----

This simple python app is build on the Flask web framwork.

The function of the app is to manage simple user database through exposed API endpoints for CRUD operations.

Documentation
-------------

### Technical characteristics

**Code base:** Python3, CSS, HTML, SQLite, Flask, Swagger.

The backend environment is running Python 3.11.6 in a virtualenv.  
The users data is stored in an sqlite instance db file users.db.   
Swagger is run by a Flask, API documentation is written in the swagger.json file.  
The fronend homepage is a simple HTML page, Flusk loads the CSS and the index from a static directory.    
The webserver is running on **port 8080**.

**Python virtualenv requirements:**  
aniso8601==9.0.1  
blinker==1.7.0  
click==8.1.7  
Flask==3.0.0  
Flask-RESTful==0.3.10  
Flask-SQLAlchemy==3.1.1  
flask-swagger==0.2.14  
flask-swagger-ui==4.11.1  
itsdangerous==2.1.2  
Jinja2==3.1.2  
MarkupSafe==2.1.3  
pytz==2023.3.post1  
PyYAML==6.0.1  
six==1.16.0  
SQLAlchemy==2.0.23  
typing\_extensions==4.9.0  
Werkzeug==3.0.1

### API endpoints

They are five endpoints exposed for managing the users in the database.  
Request and responce content type is in JSON.  
Server: [http://localhost:8080](http://localhost:8080)

Create a new User: 

    /api/new_user

> Example payload: Body
> 
>     {
>       "first_name": "Tony",
>       "last_name": "Stak",
>       "username": "ironman"
>     }

> Response: 200 OK
> 
>     {
>       "id": 1,
>       "first_name": "Tony",
>       "last_name": "Stak",
>       "username": "ironman"
>     }

List all users:

    /api/users

>  Response: 200 OK
> 
>     [	
>     	{
>             "id": 1,
>     		"username": "ironman",
>             "first_name": "Tony",
>             "last_name": "Stak"
>     
>         }
>         {
>             "id": 2,
>             "username": "jbond",
>             "first_name": "James",
>             "last_name": "Bond"
>         }, {
>             "id": 3,
>             "username": "malin",
>             "first_name": "Malin",
>             "last_name": "Markov"
>         }
>     ]

List user by ID: 

    /api/users/user/id={int}

Update a User: 

    /api/users/user/id={int}

>  Example payload: Body
> 
>     {
>       "first_name": "Tony",
>       "last_name": "Stak",
>       "username": "avenger"
>     }

> Response: 200 OK
> 
>     {
>       "id": 1,
>       "first_name": "Tony",
>       "last_name": "Stak",
>       "username": "avenger"
>     }

Delete a User: 

    /api/users/user/delete/id={int}

Deployments
-----------


### Local install

**Prerequisites:**   
_Python3, pip3, Virtualenv_

To install and run the app locally follow the below instruction:

1.  Clone the repository on your local machine.
2.  For Linux and Mac run the setup.sh bash script: _./setup.sh_
3.  For Windows: 
    1.  Install virtualenv: _pip install virtualenv_
    2.  Create virtual environment: _virtualenv .env_
    3.  Activate virtualenv: _\\.env\\scripts\\activate_
    4.  Install the required packages: _pip install -r requirements.txt_
4.  Start the app: python _app.py_
5.  Open the application in the browser: [http://localhost:8080](http://localhost:8080)

### Deploy the application in Docker container

* * *

Dockerization of the application streamlines the deployment and management  
by providing a consistent and efficient runtime environment.  
It's helping with dependencies, environment inconsistencies, and scalability.

**Prerequisites:**   
_Docker_

To run the app in docker you will need to build the docker image.

1.  Clone the repository on local or remote machine.
2.  Run the following command to build the image:  _docker build . -t user\_api\_app_
3.  Start the app with docker: _docker run --name FLASK\_APP -p 8080:8080 -v .:/app user\_api\_app_
4.  Open the application in the browser: [http://localhost:8080](http://localhost:8080)

### Deploy the application in Kuberneties Cluster

* * *

The benefits of using Kubernetes is to automate the deployment, scaling,  
and management of applications running in containers.  
It provides a platform for orchestrating and coordinating containers across a cluster of machines.

**Prerequisites:**   
_Docker, Minikube_

To run the app in a Kuberneties cluster you will create a single cluster node for the deployment and the servies. 

1.  Clone the repository on local or remote machine.
2.  Install [Docker](https://docs.docker.com/engine/install/) and [Minikube](https://minikube.sigs.k8s.io/docs/start/).
3.  Set an alias for the minikube to ease with the kubectl commands: 
    
        alias kubectl="minikube kubectl --"
    
4.  Start a Kuberneties cluster:
    
        minikube start
    
5.  Deploy the application to the default namespace by using the deployment yaml file located in the repository:
    
        kubectl apply -f Kuberneties/deploy-user-api-app.yaml
    
    Kuberneties will create the deployment and will start one replica pod and the service that will expose the port 8080.
    
    *   Confirm that the pod is running.
        
            $ kubectl get po
            NAME                            READY   STATUS    RESTARTS   AGE
            user-api-app-58598c4b89-86k6k   1/1     Running   0          51s
        
    *   Confirm that the _user-api-app_ service was created and running.
        
            $ kubectl get svc
            NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
            kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP          10m
            user-api-app   NodePort    10.101.169.14   <none>        8080:30104/TCP   3m
        
6.  Forward the port 8080 for the service to bevome reachable on the localhost:
    
        nohup kubectl port-forward service/user-api-app 8080:8080 &
    
7.  Test the connection:
    
        $ nc -zv localhost 8080

        Connection to localhost port 8080 [tcp/http-alt] succeeded!
    
8.  The application is now available at [http://localhost:8080](http://localhost:8080)

Continuous integration / Continuous deployment
-----------


This GitHub project has been setup for CI/CD processes with the use of GitGub Actions. 

Requirements to run the workflow:

1.  Secrets and Variables configured in GitHub settings as follows:  
    Secrets:    DOCKER\_PASSWORD = <your docker hub password>  
    Variables:
    1.  DOCKER\_USERNAME = <your docker hub username>
    2.  PLATFORM = \[<linux/arm/v8>, <linux/amd64>, <other>\]  
        Specify the platfrom for the image that needs to be build on. (currently configured to linux/arm64/v8)

The pipline runs in three stages using the CICD.yaml file located at **.github/workflows/** directory.

**Stages 1: Build**  
This stage builds the python API app code and tests the application.  
Python installs the dependencies packages from the requirements.txt file.   
Completing of this stage will ensure the code is checked and the application is running ok before the next stage.

**Stages 2: Dockerize**  
This stage builds a Docker image of the API app using a Dockerfile.  
The docker image is published to my public DockerHub repository [mmark0v/user\_api-app](https://hub.docker.com/repository/docker/mmark0v/user_api_app)   
The repository is configured as variable so you can provide your own repository variables.   
Once this stage is complete the new code is pushed to a new docker image with tag: _latest_

**Stages 3: Deploy**  
This stage is deploying the API app to Kuberneties cluster.   
At this stage I'm using Minikube with locally build container image.   
Deployment is sucesfull once the application is reachable on port 8080

Each stage can also be run manually by running each one of the workflows in the Actions.   
.github/workflows/[deploy\_app.yaml](https://github.com/mmark0v/Users-API-Simple-App/blob/main/.github/workflows/deploy_app.yaml "deploy_app.yaml")  
.github/workflows/[docker\_publish.yml](https://github.com/mmark0v/Users-API-Simple-App/blob/main/.github/workflows/docker_publish.yml "docker_publish.yml")  
.github/workflows/[python-app.yml](https://github.com/mmark0v/Users-API-Simple-App/blob/main/.github/workflows/python-app.yml "python-app.yml")

  
 

* * *

2023 AppV1.2 - [mmark0v](https://github.com/mmark0v)