from .land import LandVehicle

class Motorcycle(LandVehicle):
    def __init__(self, name, max_speed, price, wheels, cc):
        super().__init__(name, max_speed, price, wheels)
        self.cc = cc

    def ride_on(self):
        return f'{self.name} is now riding!'