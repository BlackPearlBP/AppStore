from .air import AirVehicle

class Helicopter(AirVehicle):
    def __init__(self, name, max_speed, price, wingspan, occupants):
        super().__init__(name, max_speed, price, wingspan)
        self.occupants = occupants

    def sport_mode(self):
        return f'{self.name} is now flying!'