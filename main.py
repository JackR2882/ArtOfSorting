#run() -> loops through all algorithms in priorityQueue, and repeats this until interrupted
#interrupt() -> moves the pointer for the next algorithm in priorityQueue, allowing user to select next algorithm to run

import time
from init import generate_spectrum
import LED_controller

# import algorithms:
from algorithms import bubble_sort
from algorithms import insertion_sort
from algorithms import merge_sort
from algorithms import selection_sort
from algorithms import heap_sort
from algorithms import quick_sort
from algorithms import counting_sort
from algorithms import bucket_sort
from algorithms import radix_sort
from algorithms import cocktail_sort
from algorithms import tim_sort
from algorithms import binary_sort
from algorithms import shell_sort

class Main:
    def __init__(self):
        self.stripSize = 144
        self.defaultBrightness = 1

        #list to store all algorithms, will loop through this list to execute algorithms
        #allows changing of order of execution
        self.priorityQueue = ["bubble", "insertion", "merge", "selection",
                              "heap", "quick", "counting", "bucket", "radix",
                              "cocktail shaker", "tim", "binary", "shell"]

        #get LED object from controller
        self.LED = LED_controller.LED(self.stripSize)

        #counter for current algorithm being executed
        self.currAlg = 12

        #audio-output object
        self.AUDIO = None

        #display-output obj
        self.DISPLAY = None


    #def run(self, LED, audioBuff):
    def run(self, audioObj, displayUpdateObj):
        
        self.AUDIO = audioObj
        self.DISPLAY = displayUpdateObj

        #generate spectrup of RGB colours
        generate_spectrum.initialize(self.LED,self.stripSize,self.defaultBrightness)
        default_b = self.LED.stripState[0][1]

        #loop indefinitely
        while True:

            # stop audio out
            self.AUDIO.amplitude = 0
 
            #randomize strip state
            self.LED.shake()
            #update physical strip
            self.LED.update()
            #ensure any highlighting is removed from LED strip
            self.LED.highlight(0,0, default_b)
            time.sleep(0.5)

            # loop around to start when necessary
            if self.currAlg >= len(self.priorityQueue):
                #reset currAlg
                self.currAlg = 0
                # reinitialize strip in case of memory errors
                generate_spectrum.initialize(self.LED,self.stripSize,self.defaultBrightness)
                self.LED.shake()

            # set volume of audio out
            #self.AUDIO.amplitude = 0.5
            self.AUDIO.amplitude = 0.01

            # execute relevant algorithm:
            if self.priorityQueue[self.currAlg] == "bubble":
                #execute bubble sort
                print("bubble sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="bubble sort", nextAlg="insertion sort")
                bubble_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "insertion":
                #execute insertion sort
                print("insertion sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="insertion sort", nextAlg="merge sort")
                insertion_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "merge":
                #execute merge sort
                print("merge sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="merge sort", nextAlg="selection sort")
                merge_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "selection":
                #execute selection sort
                print("selection sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="selection sort", nextAlg="heap sort")                
                selection_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "heap":
                #execute merge sort
                #self.DISPLAY.change(currAlg="heap sort", nextAlg="quick sort", swapSD=self.swapSD, compareSD=self.swapSD)
                print("heap sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="heap sort", nextAlg="quick sort")
                heap_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "quick":
                #execute quick sort
                print("quick sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="quick sort", nextAlg="counting sort")
                quick_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "counting":
                #execute counting sort
                print("counting sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="counting sort", nextAlg="bucket sort")
                generate_spectrum.initializeHalfSpectrum(self.LED,self.stripSize,self.defaultBrightness) # convert strip to random rg dist
                counting_sort.sort(self.LED, self.AUDIO)
                generate_spectrum.initialize(self.LED,self.stripSize,self.defaultBrightness) # return strip to standard rgb dist
            elif self.priorityQueue[self.currAlg] == "bucket":
                #execute bucket sort
                print("bucket sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="bucket sort", nextAlg="radix sort")
                bucket_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "radix":
                #execute radix sort
                print("radix sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="radix sort", nextAlg="cocktail shaker sort")
                radix_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "cocktail shaker":
                #execute cocktail shaker sort
                print("cocktail shaker sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="cocktail shaker sort", nextAlg="tim sort")
                cocktail_sort.sort(self.LED, self.AUDIO)
            elif self.priorityQueue[self.currAlg] == "tim":
                # execute tim sort
                print("tim sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="tim sort", nextAlg="binary sort")
                tim_sort.sort(self.LED, audioObj)
            elif self.priorityQueue[self.currAlg] == "binary":
                # execute binary sort
                print("binary sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="binary sort", nextAlg="shell sort")
                binary_sort.sort(self.LED, audioObj)
            elif self.priorityQueue[self.currAlg] == "shell":
                # execute shell sort
                print("shell sort")
                displayUpdateObj.send(displayUpdateObj, currAlg="shell sort", nextAlg="bubble sort")
                shell_sort.sort(self.LED, self.AUDIO)

            #algorithm done so clear strip
            self.LED.clear()

            self.currAlg += 1

        self.LED.clear()

    def interrupt(self, interrupt_val):
        name = interrupt_val[0] # interrupt val contains, both the name of interupt alg, and the volume it was spoken at
        vol = interrupt_val[1]
        # need to do something with volume (use it to change the size of the array)

        try:
            #queue the spoken algorithm next
            self.currAlg = self.priorityQueue.index(name)-1
            ret_str = name + " sort"
            print("queuing: " + ret_str)
            self.DISPLAY.send(self.DISPLAY, nextAlg=ret_str)

        except Exception as e:
            #print(e)
            # could be slow or fast mode
            if name == "fast":
                print("entering fast mode!")
                self.LED.slowMode = False
            elif name == "slow":
                print("entering slow mode!")
                self.LED.slowMode = True
            else:
                print("Error, cannot find: " + name + " sort algorithm")
        

