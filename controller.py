from flask_restful import Resource, abort, fields, marshal_with, reqparse

todos = [
	{
			"id": 1,
			"todo": "Do something nice for someone I care about",
			"completed": True
	},
	{
			"id": 2,
			"todo": "Memorize the fifty states and their capitals",
			"completed": False
	},
	{
			"id": 3,
			"todo": "Watch a classic movie",
			"completed": False
	},
	{
			"id": 4,
			"todo": "Contribute code or a monetary donation to an open-source software project",
			"completed": False
	},
	{
			"id": 5,
			"todo": "Solve a Rubik's cube",
			"completed": False
	},
	{
			"id": 6,
			"todo": "Bake pastries for me and neighbor",
			"completed": False
	},
	{
			"id": 7,
			"todo": "Go see a Broadway production",
			"completed": False
	},
	{
			"id": 8,
			"todo": "Write a thank you letter to an influential person in my life",
			"completed": True
	},
	{
			"id": 9,
			"todo": "Invite some friends over for a game night",
			"completed": False
	},
	{
			"id": 10,
			"todo": "Have a football scrimmage with some friends",
			"completed": False
	},
	{
			"id": 11,
			"todo": "Text a friend I haven't talked to in a long time",
			"completed": False
	},
	{
			"id": 12,
			"todo": "Organize pantry",
			"completed": True
	},
	{
			"id": 13,
			"todo": "Buy a new house decoration",
			"completed": False
	},
	{
			"id": 14,
			"todo": "Plan a vacation I've always wanted to take",
			"completed": False
	},
	{
			"id": 15,
			"todo": "Clean out car",
			"completed": False
	},
	{
			"id": 16,
			"todo": "Draw and color a Mandala",
			"completed": True
	},
	{
			"id": 17,
			"todo": "Create a cookbook with favorite recipes",
			"completed": False
	},
	{
			"id": 18,
			"todo": "Bake a pie with some friends",
			"completed": False
	},
	{
			"id": 19,
			"todo": "Create a compost pile",
			"completed": True
	},
	{
			"id": 20,
			"todo": "Take a hike at a local park",
			"completed": True
	},
	{
			"id": 21,
			"todo": "Take a class at local community center that interests you",
			"completed": False
	},
	{
			"id": 22,
			"todo": "Research a topic interested in",
			"completed": False
	},
	{
			"id": 23,
			"todo": "Plan a trip to another country",
			"completed": True
	},
	{
			"id": 24,
			"todo": "Improve touch typing",
			"completed": False
	},
	{
			"id": 25,
			"todo": "Learn Express.js",
			"completed": False
	},
	{
			"id": 26,
			"todo": "Learn calligraphy",
			"completed": False
	},
	{
			"id": 27,
			"todo": "Have a photo session with some friends",
			"completed": False
	},
	{
			"id": 28,
			"todo": "Go to the gym",
			"completed": False
	},
	{
			"id": 29,
			"todo": "Make own LEGO creation",
			"completed": False
	},
	{
			"id": 30,
			"todo": "Take cat on a walk",
			"completed": False
	}
]

resource_fields = {
	'id': fields.Integer,
	'todo': fields.String,
	'completed': fields.Boolean
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task is required.", required=True)

'''
class Video(Resource):
	@marshal_with(resource_fields)
	def get(self, video_id):
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="Video id taken...")

		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result

	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204

'''

class ToDoList(Resource):
	@marshal_with(resource_fields)
	def get(self):
		return todos


class ToDo(Resource):
	@marshal_with(resource_fields)
	def get(self, todo_id):
		for todo in todos:
			if todo["id"] == todo_id:
				return todo
		
		abort(404, message=f'Could not find todo id {todo_id}')
