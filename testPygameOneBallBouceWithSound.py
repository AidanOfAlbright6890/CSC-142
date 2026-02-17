# Credit for original code goes to IrvKalb on GitHub(Link: https://github.com/IrvKalb/Object-Oriented-Python-Code).

import pygame
from pygame.locals import *
import sys
import random
import pygwidgets


# 2 - Define constants
Color = (245, 66, 66)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PANEL_HEIGHT = 60
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
N_PIXELS_TO_MOVE = 3
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25))
 
# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('ball.png')
bounceSound = pygame.mixer.Sound('assignments/15_final_game/CSC142/Catch_The_Ball.py/sounds/boing.wav')
pygame.mixer.music.load('assignments/15_final_game/CSC142/Catch_The_Ball.py/sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)



# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)



 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program  
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
            
            

        if event.type == pygame.MOUSEBUTTONUP:
         if ballRect.collidepoint(event.pos):
            ballX = random.randrange(MAX_WIDTH)
            ballY = random.randrange(MAX_HEIGHT)
            ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)


    
            

            

        

    

    
    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction
        bounceSound.play()
        

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction
        bounceSound.play()

    # Update the rectangle of the ball, based on the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed
    

    # 9 - Clear the window before drawing it again
    window.fill(Color)
    
    # 10 - Draw the window elements
    window.blit(ballImage, ballRect)
    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

    pygame.font.init()

    myFont = pygame.font.SysFont('Comic SansMS', 30)
    textSurface = myFont.render('Some text', True, (0, 0, 0))
    window.blit(textSurface, (10, 10))
 
    

    
   



    
