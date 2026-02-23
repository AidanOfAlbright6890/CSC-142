#  Demo of pygwidgets capabilities
#
#  4/17  Developed by Irv Kalb

# 1 - Import libraries
import os
import sys
# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
from pygame.locals import *
import pygwidgets


# 2 - Define constants
BLACK = (0, 0, 0)
ORANGE = (237, 175, 19)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # create a clock object

# 4 - Load assets: image(s), sounds,  etc.
oBackgroundImage = pygwidgets.Image(window, (0, 0), 'images/background.jpg')

oDisplayTextTitle = pygwidgets.DisplayText(window, (10, 30), "Temperature Converter",
                                fontSize=52, width=400, textColor=BLACK, justified='center')

oInputText1 = pygwidgets.InputText(window, (20, 100), initialFocus=True,
                                   textColor=(0, 0, 0),
                                   fontSize=28)

oDisplayText1 = pygwidgets.DisplayText(window, (20, 400), "The temperature is",
                           fontSize=36, width=640, textColor=ORANGE, backgroundColor=BLACK )

oRestartButton = pygwidgets.CustomButton(window, (100, 430), 
                                    'images/restartButtonUp.png',
                                    down='images/restartButtonDown.png',
                                    over='images/restartButtonOver.png',
                                    disabled='images/restartButtonDisabled.png',
                                    soundOnClick='sounds/blip.wav',
                                    nickname='restartButton',) 

# oCheckBoxA controls the availability the custom radio buttons
# oCheckBoxB controls the availability of the text radio buttons



# 5 - Initialize variables
counter = 0
angle = 0
pct = 100

# 6 - Loop forever
while True:

    # 7 - Check for and handle events

    for event in pygame.event.get():
       # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()
        if oInputText1.handleEvent(event):
            theText = oInputText1.getValue()
            print("The text of oInputText1 is: " + theText)


        if oRestartButton.handleEvent(event):  # clicked
            counter = 0
            





       

        # If we wanted to keep track of the angle, we could start with:  angle = 0
        # Then for every left arrow:  angle = angle + 5
        # and for every right arrow:  angle = angle - 5
        # Finally, call:  oPythonIcon.rotateTo
    
 


    # 8  Do any "per frame" actions
    counter = counter + 1
    oDisplayText1.setValue('The temperature is. loop counter: ' + str (counter))
    
    
    # 9 - Clear the window
    oBackgroundImage.draw()

    # 10 - Draw all window elements
    oInputText1.draw()
    oDisplayText1.draw()
    oRestartButton.draw()
    oDisplayTextTitle.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait 
