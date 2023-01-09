#run() -> loops through all algorithms in priorityQueue, and repeats this until interrupted
#interrupt() -> moves the pointer for the next algorithm in priorityQueue, allowing user to select next algorithm to run

import time
from init import generate_spectrum
import LED_controller
from algorithms import bubble_sort
from algorithms import insertion_sort
from algorithms import merge_sort
from algorithms import selection_sort
from algorithms import heap_sort

class Main:
    def __init__(self):
        self.stripSize = 144
        self.defaultBrightness = 1

        #list to store all algorithms, will loop through this list to execute algorithms
        #allows changing of order of execution
        self.priorityQueue = ["bubble", "insertion", "merge", "selection", "heap"]

        #get LED object from controller
        self.LED = LED_controller.LED(self.stripSize)

        #counter for current algorithm being executed
        self.currAlg = 4

    def run(self):
        #generate spectrup of RGB colours
        generate_spectrum.initialize(self.LED,self.stripSize,self.defaultBrightness)

        #self.currAlg = 2
        #loop indefinitely
        while True:

            #randomize strip state
            self.LED.shake()
            #update physical strip
            self.LED.update()
            time.sleep(0.5)

            if self.currAlg >= len(self.priorityQueue):
                #reset curr
                self.currAlg = 0

            if self.priorityQueue[self.currAlg] == "bubble":
                #execute bubble sort
                print("bubble sort")
                bubble_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "insertion":
                #execute insertion sort
                print("insertion sort")
                insertion_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "merge":
                #execute merge sort
                print("merge sort")
                merge_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "selection":
                #execute selection sort
                print("selection sort")
                selection_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "heap":
                #execute merge sort
                print("heap sort")
                heap_sort.sort(self.LED)

            #algorithm done so clear strip
            self.LED.clear()

            self.currAlg += 1
        
        self.LED.clear()

    def interrupt(self, name):
        try:
            #queue this algorithm next
            self.currAlg = self.priorityQueue.index(name) - 1
        except:
            print("Error, not valid input!")

