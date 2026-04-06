import pygame
import random
import math
from RaindropManager import *

class Raindrop(RaindropsManager):
    __slots__ = ['window', 'x', 'y', 'radius', 'maxWidth', 'maxHeight']

    def __init__(self, window, maxWidth, maxHeight, radius):
        super().__init__(window)
        self.x = random.randrange(10, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.radius = random.choice(10, 50)
    
    def draw(self):
        pygame.draw.circle(self.window, (self.x, self.y), self.radius, 0)

    def update(self):
        

        
