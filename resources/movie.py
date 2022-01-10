from flask import Response, request
from database.models import Movie, Block, Wallet, Transaction
from flask_restful import Resource
from other import first_simple_chain
import mongoengine as me

chain = first_simple_chain.chain
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
        return data, 200

    def get(self, name):
        blocks = Wallet.objects.get(id_number=name).to_json()
        return Response(blocks, mimetype="application/json", status=200)

class WalletsApi(Resource):
    def get(self):
        wallets = Wallet.objects().to_json()
        return Response(wallets, mimetype="application/json", status=200)

    def delete(self):
        wallets = Wallet.objects.delete()

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

