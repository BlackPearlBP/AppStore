from vehicle.boat import Boat
from vehicle.car import Car
from vehicle.helicopter import Helicopter
from vehicle.motorboat import Motorboat
from vehicle.motorcycle import Motorcycle
from vehicle.plane import Plane
from vehicle.truck import Truck
from store.box import Box
import time

def register_vehicles(dealership):
    print("Which kind of vehicle would you like to register? ")
    print("1. Boat\n2. Car\n3. Helicopter\n4.  Motorboat\n5. Motorcycle\n6. Plane\n7. Truck")
    choice = input("Enter your choice: ")

    while choice != "0":
        if choice == "1":
            name = input("Enter the name of the boat: ")
            max_speed = input("Enter the max speed of the boat: ")
            price = input("Enter the price of the boat: ")
            capacity = input("Enter the capacity of the boat: ")
            model = input("Enter the model of the boat: ")
            dealership.add_vehicle(Boat(name, max_speed, price, capacity, model))
            return

        if choice == "2":
            name = input("Enter the name of the car: ")
            max_speed = input("Enter the max speed of the car: ")
            price = input("Enter the price of the car: ")
            wheels = input("Enter the wheels of the car: ")
            brand = input("Enter the brand of the car: ")
            dealership.add_vehicle(Car(name, max_speed, price, wheels, brand))
            return

        if choice == "3":
            name = input("Enter the name of the helicopter: ")
            max_speed = input("Enter the max speed of the helicopter: ")
            price = input("Enter the price of the helicopter: ")
            wingspan = input("Enter the wingspan of the helicopter: ")
            occupants = input("Enter the occupants of the helicopter: ")
            dealership.add_vehicle(Helicopter(name, max_speed, price, wingspan, occupants))
            return

        if choice == "4":
            name = input("Enter the name of the motorboat: ")
            max_speed = input("Enter the max speed of the motorboat: ")
            price = input("Enter the price of the motorboat: ")
            capacity = input("Enter the capacity of the motorboat: ")
            motor_power = input("Enter the motor power of the motorboat: ")
            dealership.add_vehicle(Motorboat(name, max_speed, price, capacity, motor_power))
            return

        if choice == "5":
            name = input("Enter the name of the motorcycle: ")
            max_speed = input("Enter the max speed of the motorcycle: ")
            price = input("Enter the price of the motorcycle: ")
            wheels = input("Enter the wheels of the motorcycle: ")
            cc = input("Enter the cylinders of the motorcycle: ")
            dealership.add_vehicle(Motorcycle(name, max_speed, price, wheels, cc))
            return

        if choice == "6":
            name = input("Enter the name of the plane: ")
            max_speed = input("Enter the max speed of the plane: ")
            price = input("Enter the price of the plane: ")
            wingspan = input("Enter the wingspan of the plane: ")
            occupants = input("Enter the occupants capacity of the plane: ")
            dealership.add_vehicle(Plane(name, max_speed, price, wingspan, occupants))
            return
        
        if choice == "7":
            name = input("Enter the name of the truck: ")
            max_speed = input("Enter the max speed of the truck: ")
            price = input("Enter the price of the truck: ")
            capacity = input("Enter the capacity of the truck: ")
            num_wheels = input("Enter the motor power of the truck: ")
            dealership.add_vehicle(Truck(name, max_speed, price, capacity, num_wheels))
            return

        else:
            print("Invalid option! Please choose a valid option.")

def main():
    dealership = Box()

    while True:
        print("\n1. Register a vehicle")
        print("\n2. Display all vehicles")
        print("\n3. Buy a vehicle")
        print("\n4. Exit")
        option = input("\nChoose an option: ")

        if option == '1':
            register_vehicles(dealership)
        elif option == '2':
            dealership.show_vehicles()
            time.sleep(3)
        elif option == '3':
            vehicle_name = input("\nInsert the name of the vehicle you want to buy: ")
            print(dealership.purchase_vehicle(vehicle_name))
        elif option == '4':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid option! Please choose a valid option.")

if __name__ == "__main__":
    main()

        


    




