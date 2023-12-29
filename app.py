from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

import os
import requests
import json
import base64

app = Flask(__name__)
api = Api(app)
swagger = swagger(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Defining the database model to store user data
class dbUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(200), nullable=True)
    last_name = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return self.name

# Exposing the data model fields for the marshal decorator for the API response
userFields = {
    'id':fields.Integer,
    'username':fields.String,
    'first_name':fields.String,
    'last_name':fields.String,
 }
 


# Prometheus metrics

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)
####################


 # Providing a home page from a static html template
@app.route('/')
def home():
   return render_template('index.html')
   start_time = time.time()
   REQUEST_COUNT.labels('GET', '/', 200).inc()
   REQUEST_LATENCY.labels('GET', '/').observe(time.time() - start_time)
   

# Defiinng our API resource methods 
class Users(Resource): 
    @marshal_with(userFields)
    def get(self):
        users = dbUsers.query.all()
        return users

class NewUser(Resource):   
    @marshal_with(userFields)
    def post(self):
        data = request.json
        user = dbUsers(username=data['username'],first_name=data['first_name'],last_name=data['last_name'])
        db.session.add(user)
        db.session.commit()

        users = dbUsers.query.all()
        return users

class User(Resource):
    @marshal_with(userFields)
    def get(self, pk):
        user = dbUsers.query.filter_by(id=pk).first()
        return user 
    
    @marshal_with(userFields)
    def put(self, pk):
        data = request.json
        user = dbUsers.query.filter_by(id=pk).first()
        user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        db.session.commit()

        return user

class Userdel(Resource):
    @marshal_with(userFields)
    def delete(self, pk):
        user = dbUsers.query.filter_by(id=pk).first()
        db.session.delete(user)
        db.session.commit()
        
        users = dbUsers.query.all()
        return users

# Configure the resource endpoints URI
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/users/user/id=<int:pk>') 
api.add_resource(Userdel, '/api/users/user/delete/id=<int:pk>') 
api.add_resource(NewUser, '/api/new_user') 



# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Users Database API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))




if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    print('* OS Port:  ', port)
    app.run(host='0.0.0.0', port=port, debug=True)

