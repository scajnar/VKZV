from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie
import json
from flask_restful import Api
from resources.routes import initialize_routes
app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/VKZV'
}
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

initialize_db(app)
initialize_routes(api)
app.run()
