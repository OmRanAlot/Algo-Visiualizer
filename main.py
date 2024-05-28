import pygame 
import numpy as np
import time

class SlowedSelectionSort():
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def one_step(self):
        min_idx = self.i
        for k in range(self.i+1, len(self.lst)):
            if self.lst[min_idx] > self.lst[k]:
                min_idx = k
        self.lst[self.i], self.lst[min_idx] = self.lst[min_idx], self.lst[self.i]

    def sort(self):
        for i in range(len(self.lst)):
            min_idx = i
            for k in range(i+1, len(self.lst)):
                if self.lst[min_idx] > self.lst[k]:
                    min_idx = k
            self.lst[i], self.lst[min_idx] = self.lst[min_idx], self.lst[i]

class SlowedInsertionSort():
    def __init__(self, lst):
        self.lst = lst
        self.i =0

    def one_step(self):
        key = self.lst[self.i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
        j = self.i-1
        while j >= 0 and key < self.lst[j] :
            self.lst[j + 1] = self.lst[j]
            j -= 1
        self.lst[j + 1] = key

    def sort(self, lst):
        # Traverse through 1 to len(arr)
        for i in range(len(lst)):

            key = self.lst[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < self.lst[j] :
                    lst[j + 1] = self.lst[j]
                    j -= 1
            self.lst[j + 1] = key

class SlowedBubbleSort():
    def __init__(self, lst):
        self.lst = lst
        self.i = len(self.lst)-1
    def one_step(self):
        for j in range(self.i):
            if self.lst[j]>self.lst[j+1]:
                temp = self.lst[j]
                self.lst[j] = self.lst[j+1]
                self.lst[j+1] = temp

    def sort(self):        
        for i in range(len(self.lst)-1, 0, -1):
            for j in range(i):
                if self.lst[j]>self.lst[j+1]:
                    temp = self.lst[j]
                    self.lst[j] = self.lst[j+1]
                    self.lst[j+1] = temp


amt = 200
thelist = np.random.randint(500, size=amt)
# print(thelist)
# sort(lst=thelist)
# print(thelist)

# Initialize Pygame/Set up the window
pygame.init()
window_size = (1200, 600)  # Width and height in pixels
window_title = "Pygame Window"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Main loop
select = SlowedBubbleSort(lst=thelist)
start_time = time.time()
stop = False
dt = 0.05
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

    if select.i+1 > len(thelist)-1 and stop:
        
        stop = True
    else:
        select.i-=1
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()




