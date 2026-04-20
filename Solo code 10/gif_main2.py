import pygame
import time
from gif import Gif
import pygwidgets
import sys
from pygame.locals import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

gifAnimTuple = ('Tropics [Recovered].jpg', 
                'Tropics [Recovered] 2.jpg', 
                'Tropics [Recovered] 3.jpg', 
                'Tropics [Recovered] 4.jpg', 
                'Tropics [Recovered] 5.jpg', 
                'Tropics [Recovered] 6.jpg', 
                'Tropics [Recovered] 7.jpg',
                'Tropics [Recovered] 8.jpg',
                'Tropics [Recovered] 9.jpg',
                'Tropics [Recovered] 10.jpg',
                'Tropics [Recovered] 11.jpg',
                'Tropics [Recovered] 12.jpg',
                'Tropics [Recovered] 13.jpg',
                'Tropics [Recovered] 14.jpg',
                'Tropics [Recovered] 15.jpg',
                'Tropics [Recovered] 16.jpg',
                'Tropics [Recovered] 17.jpg',
                'Tropics [Recovered] 18.jpg',
                'Tropics [Recovered] 19.jpg')

oTropicsAnimation = Gif(window, (22, 140), gifAnimTuple, .1)

oPlayButton = pygwidgets.TextButton(window, (20, 240), "Play Scene")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if oPlayButton.handleEvent(event):
            oTropicsAnimation.play()

    oTropicsAnimation.update()

    window.fill(BGCOLOR)

    oTropicsAnimation.draw()
    oPlayButton.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
        





