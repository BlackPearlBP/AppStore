class Box:
    def __init__(self):
        self.available_vehicles = []

    def add_vehicle(self, vehicle):
        self.available_vehicles.append(vehicle)

    def show_vehicles(self):
        for vehicle in self.available_vehicles:
            print(vehicle.get_info())

    def purchase_vehicle(self, vehicle_name):
        for vehicle in self.available_vehicles:
            if  vehicle.name == vehicle_name:
                self.available_vehicles.remove(vehicle)
                return f'You have purchased the {vehicle.name} for ${vehicle.price}'
        return f'Vehicle {vehicle_name} not found!'