import secrets
class Vehicle:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Car(Vehicle):

    def __init__(self, name, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower
        self.id_number = secrets.randbelow(99999)
        super().__init__(name)

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_horsepower(self):
        return self.horsepower

    def get_id_number(self):
        return self.id_number;

    def get_vehicle_data(self):
        val = {
            "name": self.name,
            "brand": self.brand,
            "model": self.model,
            "horsepower": self.horsepower,
            "id_number": self.id_number
        }
        return val

class Bike(Vehicle):

    def __init__(self, name, type):
        self.type = type  # Mountain, road, competitive ...
        super().__init__(name)

    def get_type(self):
        return self.type

