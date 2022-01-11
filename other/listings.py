from other import vehicles
import secrets

class Listing:

    def __init__(self, vehicle, location, time_of_sharing, listing_time, user, price):
        self.vehicle = vehicle
        self.time_of_sharing = time_of_sharing
        self.listing_time = listing_time
        self.user = user
        self.price = price
        self.location = location
        self.id_number = secrets.randbelow(99999)

    def get_info(self):
        return f"User {self.user} posted a listing of {self.vehicle} for {self.time_of_sharing}h of sharing." \
               f"The listing will be available for {self.listing_time}. The price for the listing is {self.price}" \
               f"and is based in {self.location}"

    def get_listing_data(self):
        val = {
            "vehicle": self.vehicle,
            "time_of_sharing": self.time_of_sharing,
            "listing_time": self.listing_time,
            "user": self.user,
            "price": self.price,
            "location": self.location,
            "id_number": self.id_number
        }
        return val