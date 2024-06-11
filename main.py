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

class SlowedMergeSort():
    def __init__(self, lst):
        self.lst = lst
        self.i = 1
        self.lengthOfArry = len(lst)

    def one_step(self):
        if self.i >= self.lengthOfArry:
            return
        leftMostElement = 0
        while(leftMostElement<self.lengthOfArry):
            mid = min(leftMostElement + self.i - 1, self.lengthOfArry - 1)
            right = min(leftMostElement + 2 * self.i - 1, self.lengthOfArry - 1)
            self.merge(self.lst, leftMostElement, mid, right)
            leftMostElement+= self.i*2
        self.i*=2
            
    def iterativeMergeSort(self, arr):
        width = 1
        lengthOfArr = len(arr)
        while(width<lengthOfArr):
            leftMostElement = 0
            while(leftMostElement<lengthOfArr):
                r= min(leftMostElement+(width*2-1), lengthOfArr-1)
                m = min(width, lengthOfArr-1)
                self.merge(arr,leftMostElement,m ,r)

                leftMostElement+= width*2
            width *=2

    ''' def iterativeMerge(self, array, left, mid, right):
        subArrayOne = mid - left + 1
        subArrayTwo = right - mid

        leftArray = [0] * subArrayOne
        rightArray = [0] * subArrayTwo

        # Copy data to temp arrays leftArray[] and rightArray[]
        for i in range(subArrayOne):
            leftArray[i] = array[left + i]
        for j in range(subArrayTwo):
            rightArray[j] = array[mid + 1 + j]

        indexOfSubArrayOne = 0  # Initial index of first sub-array
        indexOfSubArrayTwo = 0  # Initial index of second sub-array
        indexOfMergedArray = left  # Initial index of merged array
'''
    
    def merge(self, array, left, mid, right):
        subArrayOne = mid - left + 1
        subArrayTwo = right - mid

        # Create temp arrays
        leftArray = [0] * subArrayOne
        rightArray = [0] * subArrayTwo

        # Copy data to temp arrays leftArray[] and rightArray[]
        for i in range(subArrayOne):
            leftArray[i] = array[left + i]
        for j in range(subArrayTwo):
            rightArray[j] = array[mid + 1 + j]

        indexOfSubArrayOne = 0  # Initial index of first sub-array
        indexOfSubArrayTwo = 0  # Initial index of second sub-array
        indexOfMergedArray = left  # Initial index of merged array

        # Merge the temp arrays back into array[left..right]
        while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
            if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                indexOfSubArrayOne += 1
            else:
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                indexOfSubArrayTwo += 1
            indexOfMergedArray += 1

        # Copy the remaining elements of left[], if any
        while indexOfSubArrayOne < subArrayOne:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
            indexOfMergedArray += 1

        # Copy the remaining elements of right[], if any
        while indexOfSubArrayTwo < subArrayTwo:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
            indexOfMergedArray += 1
        

    #recursive
    def sort(self, arr, begin, end):
        # print(arr[begin:end])
   
        if begin>=end:
            return
        middle = begin+ (end-begin)//2
        self.sort(arr, begin, middle)
        self.sort(arr, middle+1, end)

        self.merge(arr, begin, middle, end)
    

amt = 100
thelist = np.random.randint(500, size=amt)
thelist = list(thelist)

# Initialize Pygame/Set up the window
pygame.init()
window_size = (1200, 600)  # Width and height in pixels
window_title = "Pygame Window"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)


select = SlowedMergeSort(lst=thelist)
start_time = time.time()
stop = False
dt = 0.3
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


