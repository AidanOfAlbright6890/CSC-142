# Credit goes to Irv Kalb's book, Object-Oriented Python for ideas for this code from his code in chapter 8.
# Credit also goes to Irv Kalb's Object-Oriented Python for the list snippit from chapter 9.
class Vehicle():
    def __init__(self, vehicle, fuel_capacity, cost_per_gallon, miles_per_gallon):
        self.vehicle = vehicle
        self.fuel_capacity = fuel_capacity
        self.cost_per_gallon = cost_per_gallon
        self.miles_per_gallon = miles_per_gallon

    @property
    def range(self):
        return self.fuel_capacity * self.miles_per_gallon
    @property
    def cost_per_mile(self):
        return self.cost_per_gallon * self.miles_per_gallon
    
    
car = Vehicle("car", 12, 3.70, 26)
truck = Vehicle("truck", 20, 5.00, 6.5)
motorcycle = Vehicle("motorcycle", 3, 3.50, 55)
bus = Vehicle("bus", 100, 2.80, 3.5)
print("car")
print(car.range)
print(car.cost_per_mile)
print("truck")
print(truck.range)
print(truck.cost_per_mile)
print("motorcycle")
print(motorcycle.range)
print(motorcycle.cost_per_mile)
print("bus")
print(bus.range)
print(bus.cost_per_mile)

