# LED class manages strip state any output to the strip

#setPixel() -> sets a specific pixel value on the strip
#swapPixel() -> swap two pixel values
#compareAndSwapPixel() -> orders two pixels into ascending order
#comparePixel() -> returns pixel addresses in ascending order
#highlight() -> highlights a section of the strip (between two input values)
#update() -> updates entire strip with new values
#clear() -> flushes the strip with empty pixel values
#shake() -> shuffles array randomly

import spidev
import random
import time
import numpy as np

class LED:
    def __init__(self, ss):
        #initialize spi line
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz = 10000000 # lower if errors occur (want as high as possible for response time)

        #defualt values
        self.stripSize = ss #set strip size
        self.stripState = [[0,224,0,0,0]]*(ss) # create empty array to store pixel values in form ID,brighness,blue,green,red
                                               # items are sorted by ID value

        #flag for enabling a slow-down
        self.slowMode = False

        self.swapSD = 0.0 # JUST USING RAW TIME AT THE MOMENT, WILL EXPERIMENT WITH LOOPING LATER
        self.compareSD = 0.0
        self.recursionSD = 0.0

        #mode for how to shuffle
        self.shuffleModes = ["random", "reversed", "almost-sorted"]
        self.shuffleMode = 0


    #set pixel value by updating strip state
    def setPixel(self,address,ID,brightness,blue,green,red):
        self.stripState[int(address)] = [int(ID),int(brightness)+224,int(red),int(green),int(blue)]
        #224 is added to brightness as formatting (first 3 bits of 8 mean new pixel then 5 bits of brightness)

    # swaps pixels at locations ID_1 and ID_2
    def swapPixel(self,ID_1,ID_2):
        time.sleep(self.swapSD)

        self.stripState[ID_1], self.stripState[ID_2] = self.stripState[ID_2], self.stripState[ID_1]

    # compares and swaps pixels at locations ID_1 and ID_2
    # returns true if swap occured, and false if no swap
    def compareAndSwapPixel(self,ID_1,ID_2):
        if self.stripState[ID_1] < self.stripState[ID_2]:
            time.sleep(self.compareSD + self.swapSD)
            self.stripState[ID_1], self.stripState[ID_2] = self.stripState[ID_2], self.stripState[ID_1]
            return(True) # flag to signify that swap occured
        else:
            time.sleep(self.compareSD)
            return(False) # flag to signify that no swap occured

    # compares pixels at locations ID_1 and ID_2
    # returns correct ordering of ID_1 and ID_2    
    def comparePixel(self,ID_1,ID_2):
        time.sleep(self.compareSD)
        if self.stripState[ID_1] < self.stripState[ID_2]:
            return(ID_1, ID_2)
        else:
            return(ID_2, ID_1)
        
    # highlights pixels in range start (inclusive) to end (exclusive)
    # used to provide a clearer representation of what algorithms are actually doing
    # has optional arguments to facilitate multiple highlights stacking on top of each other, otherwise higlights are reset each time
    def highlight(self, start, end, default_b, stack=False, val=1):        
        for i in range(0, len(self.stripState)):
            if not stack:
                if i in range(start, end):
                    # increase brightness here
                    self.stripState[i][1] = default_b + 5
                else:
                    # check brightness is default
                    self.stripState[i][1] = default_b
            else:
                if i in range(start, end): 
                    self.stripState[i][1] = min(self.stripState[i][1] + val, 255)  
        self.update()
        return(self.stripState)

    # currently unused, was intended to replace sleeps in some algorithms
    #def evaluate(self, val_1, val_2):
    #    time.sleep(self.compareSD)
    #    if val_1 < val_2:
    #        return (True, False, False)
    #    elif val_1 == val_2:
    #        return (False, True, False) 
    #    else:
    #        return (False, False, False)
 
    # currently unused
    #def recursionSlowDown(self):         
    #     time.sleep(self.recursionSD)


    # updates entire strip based on current value of self.stripState
    def update(self):

        if(self.slowMode): # apply slowdown
            time.sleep(0.1)

        #open spi line
        self.spi.open(0,0)   
        #send start frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])
        
        # process and send strip state as one entire chunk
        temp_arr = (np.asarray(self.stripState)[:len(self.stripState),1:5]).flatten().tolist()
        self.spi.xfer(list(map(int, temp_arr)))
        
        #send end frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])    
        #close spi line
        self.spi.close()

    # clears the strip
    def clear(self):
        #open spi line
        self.spi.open(0,0)   
        #send start frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])

        # one empty frame for each pixel
        for i in range(0,146):
            self.spi.xfer([0b11100000,0b00000000,0b00000000,0b00000000])

        #send end frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])
        #close spi line
        self.spi.close()

    # randomly shuffles (shakes the array), or performs other suffles based on current mode
    def shake(self):
        if self.shuffleModes[self.shuffleMode] == "random":
            # randomly shuffle arr
            random.shuffle(self.stripState)
        elif self.shuffleModes[self.shuffleMode] == "reversed":
            # reverse arr without sorting
            self.stripState.reverse()
        elif self.shuffleModes[self.shuffleMode] == "almost-sorted":
            # select 20 elements at random from arr and move them to the start of the arr
            for i in range(0, 20):
                item_i = random.randint(20, len(self.stripState)-1)
                self.stripState[i], self.stripState[item_i] = self.stripState[item_i], self.stripState[i]