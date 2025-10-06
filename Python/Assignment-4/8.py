# Create a Vehicle base class with subclasses Car, Bike, and Truck. Each
# should override a method calculate_trip_cost(distance) using their
# own fuel efficiency.

FUEL_PRICE = 100

class Vehicle:
    def __init__(self, name, fuel_eff):
        self.name = name
        self.fuel_eff = fuel_eff

    def calculate_trip_cost(self, distance):
        fuel_needed = distance / self.fuel_eff
        cost = fuel_needed * FUEL_PRICE

        print(f"\n Calculating generic cost for {self.name}...")
        return cost
    

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, 15)

    def calculate_trip_cost(self, distance):
        baseCost = super().calculate_trip_cost(distance)
        maintenance = 0.5 * distance
        print("\n Adding maintenance cost...")
        return baseCost + maintenance
    
class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, 50)

    def calculate_trip_cost(self, distance):
        fuel_needed = distance / self.fuel_eff
        return fuel_needed * FUEL_PRICE
    
class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name, 5)
    
    def calculate_trip_cost(self, distance):
        baseCost = super().calculate_trip_cost(distance)
        heavy_load = 2 * distance
        print("\n Adding heavy load fee ...")
        return baseCost + heavy_load
    
my_car = Car("Sedan")
my_bike = Bike("Raider")
my_truck = Truck("Lorry")

vehicles = [my_car, my_bike, my_truck]
trip_distance = 100

print(f"\n ----- Calculating cost for a {trip_distance}km trip -----")

for vehicle in vehicles:
    cost = vehicle.calculate_trip_cost(trip_distance)
    print(f"\n Cost for travelling {trip_distance}km in a {vehicle.name} = {cost:.2f}")