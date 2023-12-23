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

**Python virtualenv requirements:**  
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
Server: [http://localhost:8080](http://localhost:8080/api/users)

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

>  Response: 200 OK
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

>  Example payload: Body
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
2.  For Linux and Mac run the setup.sh bash script: _./setup.sh_
3.  For Windows: 
    1.  Install virtualenv: _pip install virtualenv_
    2.  Create virtual environment: _virtualenv .env_
    3.  Activate virtualenv: _\\.env\\scripts\\activate_
    4.  Install the required packages: _pip install -r requirements.txt_
4.  Start the app: python _app.py_
5.  Open the application in the browser: [http://localhost:8080](http://localhost:8080)

### Deploy the application in Docker container


Dockerization of the application streamlines the deployment and management  
by providing a consistent and efficient runtime environment.  
It's helping with dependencies, environment inconsistencies, and scalability.

**Prerequisites:**   
_Docker_

To run the app in docker you will need to build the docker image.

1.  Clone the repository on local or remote machine.
2.  Run the following command to build the image:  _docker build . -t user\_api\_app_
3.  Start the app with docker: _docker run --name FLASK\_APP -p 8080:8080 -v .:/app user\_api\_app_
4.  Open the application in the browser: [http://localhost:8080](http://localhost:8080)

### Deploy the application in a Kuberneties Cluster


The benefits of using Kubernetes is to automate the deployment, scaling,  
and management of applications running in containers.  
It provides a platform for orchestrating and coordinating containers across a cluster of machines.

**Prerequisites:**   
_Docker, Minikube_

To run the app in a Kuberneties cluster you will create a single cluster node for the deployment and the servies. 

1.  Clone the repository on local or remote machine.
2.  Install [Docker](https://docs.docker.com/engine/install/) and [Minikube](https://minikube.sigs.k8s.io/docs/start/).
3.  Set an alias for the minikube to ease with the kubectl commands: 
    
        alias kubectl="minikube kubectl --"
    
4.  Start a Kuberneties cluster:
    
        minikube start
    
5.  Deploy the application to the default namespace by using the deployment yaml file located in the repository:
    
        kubectl apply -f Kuberneties/deploy-user-api-app.yaml
    
    Kuberneties will create the deployment and will start one replica pod. Kuberneties will create the service that will expose the port 8080 from the container to the cluster.
    
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
    
8.  The application is now available at [http://localhost:8080](http://localhost:8080)

  
 

* * *

2023 AppV1.2 - [mmark0v](https://github.com/mmark0v)