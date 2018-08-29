
import json
from cassandra.cqlengine import connection
from flask import Flask, jsonify
from flask_restful import Resource, Api
from models.CustomerSeg import CustomerSeg
import util
import pandas as pd


app = Flask(__name__)

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
		#users = CustomerSeg.objects().all()
		#user=[user.get_data() for user in users]
		df = pd.read_csv('raw_data/DatasetGenerated.csv')
		user = df.to_dict('records')
		return (user)
apis.add_resource(UserAll, '/users')


class UserSearch(Resource):
	def get(self,id):
		#users = CustomerSeg.objects.all().filter(party_id=id)
		#user=[user.get_data() for user in users]
		df = pd.read_csv('raw_data/DatasetGenerated.csv')
		df = df[df['party_id']==id]
		user = df.to_dict('records')
		return (user)
apis.add_resource(UserSearch, '/users/<int:id>')


class UserAllSegment(Resource):
	def get(self):
		#users = CustomerSeg.objects.all()
		#user=list(set([user.fresco13_seg for user in users]))
		df = pd.read_csv('raw_data/DatasetGenerated.csv')
		user = list(df['fresco13_seg'].unique())
		return (user)
apis.add_resource(UserAllSegment, '/user_seg')


class UserSegment(Resource):
	def get(self,seg_cd):
		#users = CustomerSeg.objects.all().filter(fresco13_seg=int(seg_cd))
		#user=[user.get_data() for user in users]
		df = pd.read_csv('raw_data/DatasetGenerated.csv')
		df = df[df['fresco13_seg']==seg_cd]
		user = df.to_dict('records')
		return (user)
apis.add_resource(UserSegment, '/user_seg/<int:seg_cd>')

