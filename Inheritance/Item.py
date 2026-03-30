# Credit goes to Irv Kalb's code in chapter 10 of the book Object Oriented Python
# Credit also goes to Irv Kalb's idea of Encapsulation in chapter 9 from Object Oriented Python that was used as part of this code

from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, item, weight, quantity):
        self.weight = weight
        self.quantity = quantity
        self.item = item
        
    
    
    
    @abstractmethod
    def calculate_cost(self):
        raise NotImplementedError
    
