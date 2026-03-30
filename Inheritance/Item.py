from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, item, weight, quantity):
        self.weight = weight
        self.quantity = quantity
        self.item = item
        
    
    
    
    @abstractmethod
    def calculate_cost(self):
        raise NotImplementedError
    
