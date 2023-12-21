Documentation
-------------

* * *

### About

This simple python app is build on the Flask web framwork.

The purpose of the app is to manage simple user database through exposed API endpoints for CRUD operations.

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
>       "username": "aironman"
>     }

> Response: 200 OK
> 
>     {
>       "id": 1,
>       "first_name": "Tony",
>       "last_name": "Stak",
>       "username": "aironman"
>     }

List all users:

    /api/users

>  Response: 200 OK
> 
>     [	
>     	{
>             "id": 1,
>     		"username": "aironman",
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

Instalation
-----------

* * *

### Local install

Prerequisites:   
Python3, pip3, Virtualenv

To install and run the app locally follow the below instruction:

1.  Clone the repository on your local machine.
2.  For Linux and Mac run the setup.sh bash script: _./setup.sh_
3.  For Windows: 
    1.  Install virtualenv: _pip install virtualenv_
    2.  Create virtual environment: _virtualenv .env_
    3.  Activate virtualenv: _\\.env\\scripts\\activate_
    4.  Install the required packages: _pip install -r requirements.txt_
4.  Start the app: _./app.py_

### Run in Docker container

To run the app in docker you can build the docker image and run it.