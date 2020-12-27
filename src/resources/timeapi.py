from flask_restful import Resource
from flask import current_app
import datetime

class Timeapi(Resource):
    def get(self):

        return {
                  "time": str(datetime.datetime.now()),
                  "foo":  current_app.config['FOO']
                }