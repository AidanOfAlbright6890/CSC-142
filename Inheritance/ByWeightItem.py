from Item import *

class BYWeightItem(Item):
    def __init__(self, item, weight):
        super().__init__(item, weight)

    @property
    def weight(self):
        return self.weight
    @property
    def cost_per_pound(self):
        return self.cost_per_pound

class Bananas(BYWeightItem):
    def __init__(self, weight, cost_per_pound):
        self.cost_per_pound = cost_per_pound
        super().__init__(weight)
    def calculate_cost():
        cost_per_pound = 0.75 * 1.5
        return cost_per_pound
class Grapes(BYWeightItem):
    def __init__(self, weight, cost_per_pound):
        self.cost_per_pound = cost_per_pound
        super().__init__(weight)
    def calculate_cost():
        cost_per_pound = 2.17 * 2
        return cost_per_pound




    
    

    
