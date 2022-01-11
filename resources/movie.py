from flask import Response, request
from database.models import Movie, Block, Wallet, Transaction
from database.models import *
from flask_restful import Resource
from other import first_simple_chain
from other import vehicles, listings
import mongoengine as me

chain = first_simple_chain.chain
class BlockChain(Resource):
    
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

class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        print("Penis")
        id = movie.id
        return {'id': str(id)}, 200

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


class MovieApi(Resource):
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)

