from .db import db
import mongoengine as me
from flask_mongoengine.wtf import model_form, model_fields
from flask_mongoengine import *
from wtforms import *
from flask_wtf import *
from .db import model_form, model_fields

class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)

class Block(db.DynamicDocument):
    previous_block_hash = me.StringField(required=True)
    transaction_list = me.ListField(db.StringField())
    block_data = me.StringField(required=True)
    block_hash = me.StringField(required=True)

class Wallet(db.DynamicDocument):
    name = me.StringField(required=True)
    id_number = me.IntField(required=True, unique=True)
    balance = me.IntField()


'''class Transaction(db.DynamicDocument):
    sender = me.EmbeddedDocumentField(Wallet)
    reciever = me.EmbeddedDocumentField(Wallet)
    amount = me.IntField(required=True)
    transaction_id = me.StringField(required=True, unique=True)
'''

class Transaction(db.DynamicDocument):
    sender = me.ReferenceField(Wallet)
    reciever = me.ReferenceField(Wallet)
    id_number = me.StringField(required=True, unique=True)
    balance = me.IntField()

class Vehicle(db.DynamicDocument):
    # type = me.StringField(required=True)
    name = me.StringField(required=True)
    brand = me.StringField(required=False)
    model = me.StringField(required=False)
    horsepower = me.IntField(required=False)
    id_number = me.IntField(required=True)

class Listing(db.DynamicDocument):
    vehicle = me.IntField(required=True)
    time_of_sharing = me.StringField(required=True) # In hours
    listing_time = me.StringField(required=True)
    user = me.IntField(required=True)
    price = me.IntField(required=True)
    location = me.StringField(required=True)
    id_number = me.IntField(required=True)
