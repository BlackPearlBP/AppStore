from .vehicle import Vehicle

class AirVehicle(Vehicle):
    def __init__(self, name, max_speed, price, wingspan):
        super().__init__(name, max_speed, price)
        self.wingspan = wingspan

    def fly(self):
        return f'{self.name} is flying with a  wingspan of {self.wingspan} meters!'