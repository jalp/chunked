import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
formatter = logging.Formatter('%(asctime)s | %(module)s:%(lineno)d | %(levelname)s | %(message)s')
filename = os.path.join(os.path.dirname(__file__), 'web.log')
os.makedirs(os.path.dirname(filename), exist_ok=True)
handler = RotatingFileHandler(filename, maxBytes=50000000)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)
app.logger.info('Service started')
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Items(Resource):
    def post(self):
        response = {'res': 'OK'}
        app.logger.info(request.data)
        print(request.data)
        if not request.data:
            response['res'] = 'Empty'
        return response

api.add_resource(HelloWorld, '/')
api.add_resource(Items, '/items')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
