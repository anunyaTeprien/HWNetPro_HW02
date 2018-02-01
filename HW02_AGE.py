from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json,time
from datetime import datetime,date

app = Flask (__name__)

api = Api(app)

def CalAge(data):
	today = date.today()
	return today.year-data.year-((today.month, today.day) < (data.month, data.day))

parser = reqparse.RequestParser()
parser.add_argument('dateofbirth')

class Age(Resource):
	def get(self):
		return {"message":"Plese sent 'dateofbirth' (POST method) to me."}
	def post(self):
		args = parser.parse_args()
		birthdate = args['dateofbirth']
		datetime_object = datetime.strptime(birthdate, '%d-%m-%Y')
		age = int(CalAge(datetime_object))
		return {"Date of birth":datetime_object.strftime('%m-%d-%Y'),"age":age}

api.add_resource(Age,'/')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)

