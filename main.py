from flask import Flask
from flask_restful import Api
from controller import ToDo, ToDoList

app = Flask(__name__)
api = Api(app)

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')

if __name__ == "__main__":
	app.run(debug=True)