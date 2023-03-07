from flask import Flask
from flask_restful import Api
from controller import *

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/api/users/<int:user_id>') # get
api.add_resource(UserCreation, '/api/users/create') # post
api.add_resource(UserDelete, '/api/users/delete') # post
api.add_resource(UserList, '/api/users') # get

if __name__ == "__main__":
	app.run(debug=True)