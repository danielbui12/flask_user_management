from flask_restful import Resource, abort, fields, marshal_with, reqparse
from DB import DB
from urllib.parse import unquote
import ast

class ResourceFields:
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
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("limit", type=int, required=False)
		params_args.add_argument("skip", type=int, required=False)
		params_args.add_argument("query", type=str, required=False)
		params_args.add_argument("sort", type=str, required=False)
		args = params_args.parse_args()

		if not args['limit']:
			args['limit'] = 20
		
		if not args['skip']:
			args['skip'] = 0
		
		if not args['sort']:
			args['sort'] = { 'key': 'id', 'value': 'ascending' }
		else:
			args['sort'] = ast.literal_eval(unquote(args['sort']))

		if args['query']:
			args['query'] = unquote(args['query'])

		return DB.get(args['limit'], args['skip'], args['query'], args['sort'])

class User(Resource):
	@marshal_with(ResourceFields.resource_fields)
	def get(self, user_id):
		data = DB.get_by_id(user_id)
		if not data:
			abort(404, message=f'Could not find todo id {user_id}')

		return data

class UserCreation(Resource):
	@marshal_with(ResourceFields.resource_fields)
	def post(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("first_name", type=str, help="first_name is required.", required=True)
		params_args.add_argument("last_name", type=str, help="last_name is required.", required=True)
		params_args.add_argument("email", type=str, help="email is required.", required=True)
		params_args.add_argument("gender", type=str, help="gender is required.", required=True)
		params_args.add_argument("phone_number", type=str, help="phone_number is required.", required=True)
		params_args.add_argument("ip_address", type=str, help="phone_number is required.", required=True)
		args = params_args.parse_args()

		return DB.insert(args)

class UserDelete(Resource):
	def post(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("id", type=int, help="id is required.", required=True)
		args = params_args.parse_args()
		return DB.delete_by_id(args["id"])


class UserPriceMax(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("query", type=str, required=False)
		args = params_args.parse_args()

		return DB.get_max_price(args['query'])


class UserPriceMin(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("query", type=str, required=False)
		args = params_args.parse_args()

		return DB.get_min_price(args['query'])


class UserPriceAvg(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("query", type=str, required=False)
		args = params_args.parse_args()

		return DB.get_avg_price(args['query'])


class UserPriceTotal(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("query", type=str, required=False)
		args = params_args.parse_args()

		return DB.get_total_price(args['query'])


class UserPriceMedian(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("query", type=str, required=False)
		args = params_args.parse_args()

		return DB.get_median_price(args['query'])


class UserPriceQuantile(Resource):
	def get(self):
		params_args = reqparse.RequestParser()
		params_args.add_argument("query", type=str, required=False)
		params_args.add_argument("quantile", type=int, required=False)
		args = params_args.parse_args()

		if not args['quantile']:
			args['quantile'] = 0.5

		return DB.get_quantile_price(args['query'], args['quantile'])