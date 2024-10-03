from .vehicle import Vehicle

class WaterVehicle(Vehicle):
    def __init__(self, name,  max_speed, price, capacity):
        super().__init__(name, max_speed, price)
        self.capacity = capacity

    def sail(self):
        return f'{self.name} is sailing with a capacity of {self.capacity} tons!'
