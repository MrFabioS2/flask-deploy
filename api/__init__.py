import time
from flask import jsonfy
from flask_restful import Api, Resource
from tasks import celery
import config

api = Api(prefix=config.API_PREFIX)

class taskStatusAPI(resource):
	def get(self, task_id):
		task = celery.AsyncResult(task_id)
		return jsonfy(task.result)

class DataProcessingAPI(Resource):
	def POST(self):
		task = process_data.delay()
		return {'task_id': task.id}, 200

@celery.task()
def process_data():
	time.sleep(60)

# data processing endpoint
api.add_resource(DataProcessingAPI, '/process_data')

# taks status endpoint
api.add_resource(TaskStatusAPI, '/task/<string:task_id>')