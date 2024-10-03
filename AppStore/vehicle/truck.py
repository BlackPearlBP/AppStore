from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, name, max_speed, price, capacity, num_wheels):
        super().__init__(name, max_speed, price, capacity)
        self.num_wheels = num_wheels

    def drive(self):
        return f"The {self.name} is driving on {self.num_wheels} wheels!"