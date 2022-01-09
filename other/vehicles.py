
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
        super().__init__(name)

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_horsepower(self):
        return self.horsepower

class Bike(Vehicle):

    def __init__(self, name, type):
        self.type = type  # Mountain, road, competitive ...
        super().__init__(name)

    def get_type(self):
        return self.type

