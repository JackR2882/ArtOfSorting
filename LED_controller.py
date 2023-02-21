#setPixel() -> sets a specific pixel value on the strip
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
        self.spi.max_speed_hz = 10000000 #lower if errors occur (want as high as possible for response time)
        #10,000,000 (10MHz)

        #defualt values
        self.stripSize = ss #set strip size
        self.stripState = [[0,224,0,0,0]]*(ss) #create empty array to store pixel values in form ID,brighness,blue,green,red

        #flag for enabling a slow-down
        self.slowMode = False

    #set pixel value by updating strip state
    def setPixel(self,ID,address,brightness,blue,green,red):
        self.stripState[int(address)] = [ID,int(brightness)+224,int(red),int(green),int(blue)]
        #224 is added to brightness as formatting (first 3 bits of 8 mean new pixel then 5 bits of brightness)

    def update(self):

        if(self.slowMode):
            time.sleep(0.1)

        #open spi line
        self.spi.open(0,0)   
        #send start frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])

        # process and send list as one entire chunk
        temp_arr = (np.asarray(self.stripState)[:len(self.stripState),1:5]).flatten().tolist()
        self.spi.xfer(list(map(int, temp_arr)))

        #send strip state as data frames:
        #for i in range(0,len(self.stripState),4): 
            #self.spi.xfer([self.stripState[i][1],self.stripState[i][2],self.stripState[i][3],self.stripState[i][4],
            #              self.stripState[i+1][1],self.stripState[i+1][2],self.stripState[i+1][3],self.stripState[i+1][4],
            #              self.stripState[i+2][1],self.stripState[i+2][2],self.stripState[i+2][3],self.stripState[i+2][4],
            #              self.stripState[i+3][1],self.stripState[i+3][2],self.stripState[i+3][3],self.stripState[i+3][4],
            #              self.stripState[i+4][1],self.stripState[i+4][2],self.stripState[i+4][3],self.stripState[i+4][4],
            #              self.stripState[i+5][1],self.stripState[i+5][2],self.stripState[i+5][3],self.stripState[i+5][4],
            #              self.stripState[i+6][1],self.stripState[i+6][2],self.stripState[i+6][3],self.stripState[i+6][4],
            #              self.stripState[i+7][1],self.stripState[i+7][2],self.stripState[i+7][3],self.stripState[i+7][4]])
        #    self.spi.xfer([self.stripState[i][1],self.stripState[i][2],self.stripState[i][3],self.stripState[i][4],
        #                  self.stripState[i+1][1],self.stripState[i+1][2],self.stripState[i+1][3],self.stripState[i+1][4],
        #                  self.stripState[i+2][1],self.stripState[i+2][2],self.stripState[i+2][3],self.stripState[i+2][4],
        #                  self.stripState[i+3][1],self.stripState[i+3][2],self.stripState[i+3][3],self.stripState[i+3][4]])
            #self.spi.xfer([self.stripState[i][1],self.stripState[i][2],self.stripState[i][3],self.stripState[i][4],
            #              self.stripState[i+1][1],self.stripState[i+1][2],self.stripState[i+1][3],self.stripState[i+1][4]])

        #send end frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])    
        #close spi line
        self.spi.close()

    def clear(self):
        #open spi line
        self.spi.open(0,0)   
        #send start frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])

        #not sure why this is 145? need to look into this
        for i in range(0,145):
            self.spi.xfer([224,0,0,0])
        
        #send end frame:
        self.spi.xfer([0b00000000,0b00000000,0b00000000,0b00000000])
        #close spi line
        self.spi.close()

    def shake(self):
        random.shuffle(self.stripState)


    def highlight(self, start, end, default_b):        
        for i in range(0, len(self.stripState)):
            if i in range(start, end):
                # increase brightness here
                self.stripState[i][1] = default_b + 5
            else:
                # check brightness is default
                self.stripState[i][1] = default_b
    
        self.update()
        return(self.stripState)