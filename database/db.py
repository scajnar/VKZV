from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form, model_fields
import mongoengine
db = MongoEngine()
def initialize_db(app):
    db.init_app(app)