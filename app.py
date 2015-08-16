import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Items(Resource):
    def post(self):
        app.logger.info(request.data)
        return {'res': 'OK'}

api.add_resource(HelloWorld, '/')
api.add_resource(Items, '/items')

if __name__ == "__main__":
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", debug=True)
