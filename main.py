from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from controller import *

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "My API"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

api = Api(app)

api.add_resource(User, '/api/users/<int:user_id>') # get
api.add_resource(UserCreation, '/api/users/create') # post
api.add_resource(UserDelete, '/api/users/delete') # post
api.add_resource(UserList, '/api/users') # get

api.add_resource(UserPriceMax, '/api/price/max') # get
api.add_resource(UserPriceMin, '/api/price/min') # get
api.add_resource(UserPriceAvg, '/api/price/avg') # get
api.add_resource(UserPriceTotal, '/api/price/total') # get
api.add_resource(UserPriceMedian, '/api/price/median') # get
api.add_resource(UserPriceQuantile, '/api/price/quantile') # get

if __name__ == "__main__":

    app.run(debug=True)