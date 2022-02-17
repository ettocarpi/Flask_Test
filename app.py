# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
import json
import logging
from functions import *

# creating the flask app
app = Flask(__name__)
# creating an API object

#security
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)

USER_DATA = {
"masnun": "abc123"
}

class User(object):
    def __init__(self, id):
        self.id = id

def __str__(self):
    return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=123)

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}


class PrivateResource(Resource):
		@jwt_required()
		def get(self):
			return {"meaning_of_life": 42}

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	@jwt_required()
	def get(self):

		return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	@jwt_required()
	def post(self):
		
		data = request.get_json()	 # status code
		response = jsonify({'data': data})
		json_data = json.dumps(data)
		log(json_data)
		#raise Exception()
		return response
		


# another resource to calculate the square of a number
class Square(Resource):
	def get(self, num):
		return jsonify({'square': num**2})


# adding the defined resources along with their corresponding urls
api.add_resource(PrivateResource, '/private')
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
jwt = JWT(app, verify, identity)


# driver function
if __name__ == '__main__':
	app.run(debug = True)
