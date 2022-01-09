from .movie import MoviesApi, MovieApi, Block, BlocksApi, MockBlock

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')
    api.add_resource(BlocksApi, '/api/blocks/')
    api.add_resource(MockBlock, '/api/mockblock/')
