
import json
from cassandra.cqlengine import connection
from flask import Flask, jsonify
from flask_restful import Resource, Api
#from flask_restful import reqparse
#from flask import Blueprint, Response
from models.CustomerSeg import CustomerSeg
import util


#api = Api(app)
app = Flask(__name__)
#apis = Blueprint("apis", __name__)
apis = Api(app)
app.debug = True



#connection.setup(['127.0.0.1'], "customer_seg", protocol_version=3)

# def get_all():
    # customer_segs = CustomerSeg.objects().all()
    # return [customer_seg.get_data() for customer_seg in customer_segs]
	

	
class HelloWorld(Resource):
    def get(self):
        return ("Hello! This is a mock api for Fresco(testing Flask with Cassandra)")

apis.add_resource(HelloWorld, '/')	
	
	
	
	
class UserAll(Resource):
	def get(self):
		#parser = reqparse.RequestParser()
		#parser.add_argument('party_id')
	#	args = parser.parse_args()
	#	print (args)
	#	filters=id
		#users = CustomerSeg.objects.all().filter(party_id=id)
		users = CustomerSeg.objects().all()
	#	.filter(party_id).all()
		
		user=[user.get_data() for user in users]
		#print (util.to_json(user))
		#return (util.to_json(user))
		#print (user)
		return (user)
apis.add_resource(UserAll, '/users')


#@apis.route("/user/<fresco13_seg>")
class UserSearch(Resource):
	def get(self,id):
		#parser = reqparse.RequestParser()
		#parser.add_argument('party_id')
	#	args = parser.parse_args()
	#	print (args)
	#	filters=id
		users = CustomerSeg.objects.all().filter(party_id=id)
		#users = CustomerSeg.objects().all()
	#	.filter(party_id).all()
		
		user=[user.get_data() for user in users]
		#print (util.to_json(user))
		#return (util.to_json(user))
		#print (user)
		return (user)
apis.add_resource(UserSearch, '/users/<id>')




class UserAllSegment(Resource):
	def get(self):
		#parser = reqparse.RequestParser()
		#parser.add_argument('party_id')
	#	args = parser.parse_args()
	#	print (args)
	#	filters=id
		users = CustomerSeg.objects.all()
		#users = CustomerSeg.objects(party_id)
	#	.filter(party_id).all()
		
		user=list(set([user.fresco13_seg for user in users]))
		#print (util.to_json(user))
		#return (util.to_json(user))
		#print (user)
		#print(users.fresco13_mseg)
		return (user)
apis.add_resource(UserAllSegment, '/user_seg')

class UserSegment(Resource):
	def get(self,seg_cd):
		#parser = reqparse.RequestParser()
		#parser.add_argument('party_id')
	#	args = parser.parse_args()
	#	print (args)
	#	filters=id
		users = CustomerSeg.objects.all().filter(fresco13_seg=int(seg_cd))
		#users = CustomerSeg.objects().all()
	#	.filter(party_id).all()
		
		user=[user.get_data() for user in users]
		#print (util.to_json(user))
		#return (util.to_json(user))
		print (user)
		return (user)
apis.add_resource(UserSegment, '/user_seg/<seg_cd>')
#app.register_blueprint(apis)
