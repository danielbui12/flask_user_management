from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from swagger_ui import api_doc

from controller import *

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')
api_doc(app, config_url='http://localhost:5000/api/spec.json', url_prefix='/api/doc', title='API doc')


api.add_resource(User, '/api/users/<int:user_id>') # get
api.add_resource(UserCreation, '/api/users/create') # post
api.add_resource(UserDelete, '/api/users/delete') # post
api.add_resource(UserList, '/api/users') # get

if __name__ == "__main__":
	app.run(debug=True)