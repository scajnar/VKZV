import json
import http
from flask import Response, request
from database.models import Movie, Block, Wallet, Transaction
from database.models import *
from flask_restful import Resource
from other import first_simple_chain
from other import vehicles, listings
import hashlib
import secrets
import random
import json as js
from database import models
import requests
chain = first_simple_chain.chain
class SinBlock:
    def __init__(self, previous_block_hash, events):
        self.previous_block_hash = previous_block_hash
        self.block_input_data = {
            "previous_block_hash": previous_block_hash,
            "events": events,
        }
        self.block_hash = hashlib.sha256(js.dumps(self.block_input_data).encode()).digest()
        self.block_data = {
            "previous_block_hash": str(self.previous_block_hash),
            "events": [js.dumps(events)],
            "block_hash": str(self.block_hash),
        }
        #r = requests.post(f'http://localhost:5000/api/block/', data=self.block_data)


    def get_block_data(self):
        return self.block_data

class TodB(Resource):
    def post(self):
        body = request.get_json()
        block = VehBlock(**body).save()
        return 200



class VehChain:
    def __init__(self):
        self.chain = []
        self.generate_first_block()

    def generate_first_block(self):
        self.chain.append(SinBlock(12345678910, "No events"))

    def get_last_block_data(self):
        return self.chain[-1].get_block_data()

vehicle_chain = VehChain()


def create_block_from_events(events=None):
    vehicle_chain.chain.append(SinBlock(vehicle_chain.chain[-1].block_hash, events))

class VehChainApi(Resource):
    def get(self):
        blocks = VehBlock.objects().to_json()
        return Response(blocks, mimetype="application/json", status=200)


class MockBlock(Resource):

    def get(self):
        blocks = Block.objects().to_json()
        return Response(blocks, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        chain.generate_random_block()
        block = chain.last_block.get_block_data()
        Block(**block).save()
        return block, 200

    def delete(self):
        block = Block.objects.delete()
        return "", 200

class BlocksApi(Resource):
    def get(self):
        blocks = Block.objects().to_json()
        return Response(blocks, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        chain.generate_random_block()
        block = chain.last_block.create_block_from_transaction()
        Block(**block).save()
        return block, 200

class WalletApi(Resource):
    def post(self,name):
        wallet = first_simple_chain.Wallet(name=name)
        data = wallet.get_wallet_data()
        Wallet(**data).save()
        return wallet.get_id(), 200

    def get(self, name):
        blocks = Wallet.objects.get(id_number=name).to_json()
        return Response(blocks, mimetype="application/json", status=200)

class WalletsApi(Resource):
    def get(self):
        wallets = Wallet.objects().to_json()
        return Response(wallets, mimetype="application/json", status=200)

    def delete(self):
        wallets = Wallet.objects.delete()

class TransactionApi(Resource):
    def post(self, sender, reciever, ammount):
        # transaction = Transaction
        pass


class PostVehicleApi(Resource):
    def post(self, name, brand, model, horsepower):
        car = vehicles.Car(name=name, brand=brand, model=model, horsepower=horsepower)
        data = car.get_vehicle_data()
        Vehicle(**data).save()
        return car.get_id_number(), 200

class GetAllVehiclesApi(Resource):
    def get(self):
        vehicles = Vehicle.objects().to_json()
        return Response(vehicles, mimetype="application/json", status=200)

class GetOneVehicleApi(Resource):
    def get(self, id):
        vehicle = Vehicle.objects.get(id_number=id).to_json()
        return Response(vehicle, mimetype="application/json", status=200)

class CreateListingApi(Resource):
    def post(self, vehicle_id, time_of_sharing, listing_time, user_id, price, location):
        listing = listings.Listing(
            vehicle=vehicle_id,
            time_of_sharing=time_of_sharing,
            listing_time=listing_time,
            user=user_id,
            price=price,
            location=location,
        )
        data = listing.get_listing_data()
        Listing(**data).save()
        return data, 200

class ClaimListingApi(Resource):
    def post(self, listing_id, claiming_user_id):
        listing = Listing.objects.get(id_number=listing_id)
        lister = listing.user
        price = listing.price
        claimer = claiming_user_id
        execute_transaction(claimer, lister, price)
        # Listing.objects.get(id_number=listing_id).delete()
        return 123, 200

class GetAllListingsApi(Resource):
    def get(self):
        listings = Listing.objects().to_json()
        return Response(listings, mimetype="application/json", status=200)

class DeleteAllApi(Resource):
    def get(self):
        Wallet.objects.delete()
        Vehicle.objects.delete()
        Listing.objects.delete()
        return Response("ide", mimetype="application/json", status=200)

def execute_transaction(sender_id, reciever_id, price):
    sender = Wallet.objects.get(id_number=sender_id)
    sender.balance -= price
    sender.save()
    reciever = Wallet.objects.get(id_number=reciever_id)
    reciever.balance += price
    reciever.save()
    chain.create_block_from_transaction([Transaction])
