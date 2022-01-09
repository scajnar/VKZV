from .db import db

class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)

class Block(db.DynamicDocument):
    previous_block_hash = db.StringField(required=True)
    transaction_list = db.ListField(db.StringField())
    block_data = db.StringField(required=True)
    block_hash = db.StringField(required=True)

class Wallet(db.Document):
    name = db.StringField(required=True, unique=True)
    id_number = db.StringField(required=True, unique=True)
    balance = db.StringField()


