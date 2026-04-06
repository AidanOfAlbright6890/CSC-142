# Credit for starting point template goes to Irv Kalb's book, Object Oriented Python from chapter 5

import pygame
import pygwidgets
import random
import sys
from pygame.locals import *
from abc import ABC, abstractmethod

class RaindropsManager(ABC):
     MAX_RADIUS = 20
     RAIN_RATE = 10 # miliseconds
     WINDOW_WIDTH = 640
     WINDOW_HEIGHT = 480
     BLUE = (0, 0, 250)
     GRAY = (117, 120, 125)
     FRAMES_PER_SECOND = 30
     pygame.init()
     window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
     clock = pygame.time.Clock()
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               window.fill(GRAY)
               pygame.draw.circle(window, BLUE, (250, 50), 30, 1)
               pygame.draw.circle(window, BLUE, (400, 50), 30, 1)

               pygame.display.update()
               clock.tick(FRAMES_PER_SECOND)
               pygame.display.flip()
          
            


                    
