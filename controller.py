from flask_restful import Resource, abort, fields, marshal_with, reqparse
from DB import DB
from const import RESPONSE
from urllib.parse import unquote

user_field = {
	"id": fields.Integer,
	"first_name": fields.String,
	"last_name": fields.String,
	"email": fields.String,
	"gender": fields.String,
	"ip_address": fields.String,
	"phone_number": fields.String
}

class UserList(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("limit", type=int, required=False)
		params_args.add_argument("skip", type=int, required=False)
		params_args.add_argument("query", type=str, required=False)
		params_args.add_argument("sort", type=dict, required=False)
		args = params_args.parse_args()

		if not args['limit']:
			args['limit'] = 20
		
		if not args['skip']:
			args['skip'] = 0
		
		if not args['sort']:
			args['sort'] = { 'key': 'id', 'value': 'ascending' }
		else:
			args['sort'] = unquote(args['sort'])
		
		if args['query']:
			args['query'] = unquote(args['query'])

		return DB.get(args['limit'], args['skip'], args['query'], args['sort'])


class User(Resource):
	@marshal_with(user_field)
	def get(self, user_id):
		data = DB.get_by_id(user_id)
		if not data:
			abort(404, message=f'Could not find todo id {user_id}')

		return data

class UserCreation(Resource):
	@marshal_with(user_field)
	def post(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("first_name", type=str, help="first_name is required.", required=True)
		params_args.add_argument("last_name", type=str, help="last_name is required.", required=True)
		params_args.add_argument("email", type=str, help="email is required.", required=True)
		params_args.add_argument("gender", type=str, help="gender is required.", required=True)
		params_args.add_argument("phone_number", type=str, help="phone_number is required.", required=True)
		args = params_args.parse_args()

		return DB.insert(args)

class UserDelete(Resource):
	def post(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("id", type=int, help="id is required.", required=True)
		args = params_args.parse_args()
		print(args["id"])
		return DB.delete_by_id(args["id"])