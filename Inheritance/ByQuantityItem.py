from abc import ABC
from ByWeightItem import *
from Item import *

class BYQuantityItem(Item):
    def __init__(self, item, quantity):
        super().__init__(item, quantity)
   
    @property
    def quantity(self):
        return self.quantity
    @property
    def cost_each(self):
        return self.cost_each

class Oranges(BYQuantityItem):
    def __init__(self, quantity, cost_each):
        self.cost_each = cost_each
        super().__init__(quantity)

    def calculate_cost():
        cost = 4.6 * 1.35
        return cost
class Cantaloupes(BYQuantityItem):
    def __init__(self, quantity, cost_each):
        self.cost_each = cost_each
        super().__init__(quantity)

    def calculate_cost():
        cost = 5 * 4.00
        return cost
    
