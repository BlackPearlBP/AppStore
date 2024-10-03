class Vehicle:
    def  __init__(self, name, max_speed, price):
        self.name = name
        self.max_speed = max_speed
        self.price = price

    def get_info(self):
        return f'{self.name}: top speed  {self.max_speed} km/h, price ${self.price}'

    def start_engine(self):
        return f'{self.name} engine started!'
