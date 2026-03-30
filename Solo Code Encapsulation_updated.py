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
    
    @property
    def getType(self):
        return self.vehicle
    
    
ovehicle1 = Vehicle('car', 12, 3.70, 26)
ovehicle2 = Vehicle("truck", 20, 5.00, 6.5)
ovehicle3 = Vehicle("motorcycle", 3, 3.50, 55)
ovehicle4 = Vehicle("bus", 100, 2.80, 3.5)
print(ovehicle1.getType)
print(ovehicle1.range)
print(ovehicle1.cost_per_mile)
print(ovehicle2.getType)
print(ovehicle2.range)
print(ovehicle2.cost_per_mile)
print(ovehicle3.getType)
print(ovehicle3.range)
print(ovehicle3.cost_per_mile)
print(ovehicle4.getType)
print(ovehicle4.range)
print(ovehicle4.cost_per_mile)



