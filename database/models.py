from .db import db
import mongoengine as me

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
    name = me.StringField(required=True, unique=True)
    id_number = me.StringField(required=True, unique=True)
    balance = me.IntField()
