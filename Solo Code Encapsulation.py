# Credit goes to Irv Kalb's book, Object-Oriented Python for ideas for this code from his code in chapter 8.
# Credit also goes to Irv Kalb's Object-Oriented Python for the list snippit from chapter 9.
class Vehicle():
    def __init__(self, vehicle, fuelcapacity, cost_per_gallon_of_fuel, miles_per_gallon):
        self._vehicle = vehicle
        self._fuelcapacity = fuelcapacity
        self._cost_per_gallon_of_fuel = cost_per_gallon_of_fuel
        self._miles_per_gallon = miles_per_gallon

    @property
    def range(self):
        return (self._fuelcapacity * self._miles_per_gallon)
    @property
    def cost_per_mile(self):
        return (self._cost_per_gallon_of_fuel * self._miles_per_gallon)





ovehicle1 = ('Car, Fuel capacity is 12 gallons, average cost per gallon of $3.70, and miles per gallon is 26 miles')
ovehicle2 = ('Truck, Fuel capacity is 20 gallons, average cost per gallon of $5.00, and miles per gallon is 6.5 miles')
ovehicle3 = ('Motorcycle, Fuel capacity is 3 gallons, average cost per gallon of $3.50, and miles per gallon is 55 miles')
ovehicle4 = ('Bus, Fuel capacity is 100 gallons, average cost per gallon of $2.80, and miles per gallon is 3.5 miles')

ofuel_capacity_multiplied_by_miles_per_gallon_for_car = 12 * 26
ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_car = 3.70 * 26

ofuel_capacity_multiplied_by_miles_per_gallon_for_truck = 20 * 6.5
ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_truck = 5.00 * 6.5

ofuel_capacity_multiplied_by_miles_per_gallon_for_motorcycle = 3 * 55
ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_motorcycle = 3.50 * 55

ofuel_capacity_multiplied_by_miles_per_gallon_for_bus = 100 * 3.5
ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_bus = 2.80 * 3.5

vehicleList = [ovehicle1, ovehicle2, ovehicle3, ovehicle4]

print(vehicleList)
print('The amount of miles that cars can typically go on a full tank of gas is', ofuel_capacity_multiplied_by_miles_per_gallon_for_car, 'miles.')

print('The cost per mile for typical cars is $',ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_car,'.')

print('The amount of miles that trucks can typically go on a full tank of gas is', ofuel_capacity_multiplied_by_miles_per_gallon_for_truck, 'miles.')

print('The cost per mile for typical trucks is $',ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_truck,'.')

print('The amount of miles that motorcycles can typically go on a full tank of gas is', ofuel_capacity_multiplied_by_miles_per_gallon_for_motorcycle, 'miles.')

print('The cost per mile for typical trucks is $',ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_motorcycle,'.')

print('The amount of miles that buses can typically go on a full tank of gas is', ofuel_capacity_multiplied_by_miles_per_gallon_for_bus, 'miles.')

print('The cost per mile for typical buses is $',ocost_per_gallon_of_fuel_multiplied_by_miles_per_gallon_for_bus,'.')

