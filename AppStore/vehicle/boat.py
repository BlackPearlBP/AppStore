from .water import WaterVehicle

class Boat(WaterVehicle):
    def __init__(self, name, max_speed, price, capacity, model):
        super().__init__(name, max_speed, price, capacity)
        self.model = model

    def sport_mode(self):
        return f'{self.name} is now sailing!'
