from Item import *
from ByQuantityItem import *
from ByWeightItem import *

class Order(Item):
    def __init__(self, item, weight, cost_per_pound, quantity, cost_each):
        self.cost_each = cost_each
        self.cost_per_pound = cost_per_pound
        super().__init__(item, weight, quantity)

    @property
    def get_item(self):
        return self.item

    @property
    def add_item(self):
        return self.item_number
    @property
    def calculate_cost(self):
        return self.weight * self.cost_per_pound + self.quantity * self.cost_each

ototalcost1 = Order('receipt:  ', 0.75, 1.5, 4.6, 1.35)
print(ototalcost1.get_item)
print('$',ototalcost1.calculate_cost)
print('Number of items: 4')
print('Items ordered: Bananas, grapes, cantaloupes and oranges')

