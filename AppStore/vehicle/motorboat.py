from .water import WaterVehicle

class Motorboat(WaterVehicle):
    def __init__(self, name, max_speed, price, capacity, motor_power):
        super().__init__(name, max_speed, price, capacity)
        self.motor_power = motor_power

    def boost(self):
        return f'{self.name} is boosting its motor power to {self.motor_power}!'
