import pygame
import time
import pygwidgets
import sys
from pygame.locals import *
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
TIMER_LENGTH = 2.5
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
timerRunning = False

headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Click Start to start a ' +
                                       str(TIMER_LENGTH) + '-second timer:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)
startButton = pygwidgets.TextButton(window, (180, 100), 'Start')

clickMeButton = pygwidgets.TextButton(window, (180, 100), 'Start')

timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Message showing during timer',
                                      fontSize=36, justified='center', width=WINDOW_WIDTH)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if startButton.handleEvent(event):
            timeStarted = time.time()
            startButton.disable()
            timerMessage.show()
            print('Starting Timer')
            timerRunning = True
        if timerRunning:
            elapsed = time.time() - timeStarted
            if elapsed >= TIMER_LENGTH:
                startButton.enable()
                timerMessage.hide()
                print('Timer ended')
                timerRunning = False
            
            window.fill(WHITE)

            headerMessage.draw()
            startButton.draw()
            timerMessage.draw()

            pygame.display.update()

            clock.tick(FRAMES_PER_SECOND)