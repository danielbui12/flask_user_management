from flask import Flask
from flask_restful import Api
from controller import *

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/api/users/<int:user_id>')
api.add_resource(UserCreation, '/api/users/create')
api.add_resource(UserList, '/api/users')

if __name__ == "__main__":
	app.run(debug=True)