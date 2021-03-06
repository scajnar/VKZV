from .movie import Block, BlocksApi, MockBlock, WalletApi, WalletsApi
from .movie import *
def initialize_routes(api):
    api.add_resource(BlocksApi, '/api/blocks/')
    api.add_resource(MockBlock, '/api/mockblock/')
    api.add_resource(WalletApi, '/api/wallet/<name>')
    api.add_resource(WalletsApi, '/api/wallet/')
    api.add_resource(PostVehicleApi, "/api/vehicle/<name>/<brand>/<model>/<horsepower>/")
    api.add_resource(GetAllVehiclesApi, "/api/vehicles/")
    api.add_resource(GetOneVehicleApi, "/api/vehicle/<id>")
    api.add_resource(CreateListingApi, "/api/listing/<vehicle_id>/<time_of_sharing>/<listing_time>/<user_id>/<price>/<location>/")
    api.add_resource(ClaimListingApi, "/api/listing/claim/<listing_id>/<claiming_user_id>/")
    api.add_resource(GetAllListingsApi,"/api/listings")
    api.add_resource(DeleteAllApi, "/api/delete")
    api.add_resource(VehChainApi, "/api/chain/")
    api.add_resource(TodB, "/api/block/")
#42113 vehicle id
#51537 poster user id
#88320 listing id
#92858 claimer