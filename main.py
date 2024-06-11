import pygame 
import numpy as np
import time
from sortingAlgo import *


#create the list with amt elements
amt = 100
thelist = np.random.randint(500, size=amt)
thelist = list(thelist)

# Initialize Pygame/Set up the window
pygame.init()
window_size = (1200, 600)  # Width and height in pixels
window_title = "Pygame Window"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)


select = SlowedSelectionSort(lst=thelist)

stop = False
dt = 0.1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((200, 200, 200))

    x=10
    for i in thelist:
        pygame.draw.rect(screen, (0,0,0), (x, 580-i, 4, i))
        x+=6

    time.sleep(dt)

    if not stop:
        select.one_step()
        # if not select.steps:
        #     stop = True

    if isinstance(select, SlowedBubbleSort):
        select.i-=1
    elif(isinstance(select, SlowedMergeSort)):
        pass
    else:
        select.i+=1
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


