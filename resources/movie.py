from flask import Response, request
from database.models import Movie, Block
from flask_restful import Resource
from other import first_simple_chain


class MockBlock(Resource):
    def get(self):
        block = Block.objects.to_json()
        return Response(block, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        chain = first_simple_chain.VehicleChain()
        chain.generate_first_block()
        block = chain.last_block.get_block_data()
        return block, 200

class BlocksApi(Resource):
    def get(self):
        block = Block.objects.to_json()
        return Response(block, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        block = Block(**body).save()
        block_hash = block.block_hash
        return {"block_hash": str(block_hash)}, 200

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