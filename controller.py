from flask_restful import Resource, abort, fields, marshal_with, reqparse
from DB import DB
from const import RESPONSE

resource_fields = {
	"id": fields.Integer,
	"first_name": fields.String,
	"last_name": fields.String,
	"email": fields.String,
	"gender": fields.String,
	"ip_address": fields.String,
	"phone_number": fields.String
}

class UserList(Resource):
	@marshal_with(resource_fields)
	def get(self):
		return DB.get()


class User(Resource):
	@marshal_with(resource_fields)
	def get(self, user_id):
		data = DB.get_by_id(user_id)
		if not data:
			abort(404, message=f'Could not find todo id {user_id}')

		return data

class UserCreation(Resource):
	@marshal_with(resource_fields)
	def post(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("first_name", type=str, help="first_name is required.", required=True)
		params_args.add_argument("last_name", type=str, help="last_name is required.", required=True)
		params_args.add_argument("email", type=str, help="email is required.", required=True)
		params_args.add_argument("gender", type=str, help="gender is required.", required=True)
		params_args.add_argument("phone_number", type=str, help="phone_number is required.", required=True)
		args = params_args.parse_args()

		return args

	