from .vehicle import Vehicle

class LandVehicle(Vehicle):
    def __init__(self, name, max_speed, price, wheels):
        super().__init__(name, max_speed, price)
        self.wheels = wheels

    def drive(self):
        return f'{self.name} is driving on {self.wheels} wheels!'