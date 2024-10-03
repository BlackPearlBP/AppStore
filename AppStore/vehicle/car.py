from .land import LandVehicle

class Car(LandVehicle):
    def __init__(self, name, max_speed, price, wheels, brand):
        super().__init__(name, max_speed, price, wheels)
        self.brand = brand

    def sport_mode(self):
        return f'{self.name} is now racing!'