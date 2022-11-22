#initialize() -> generates and sets pixel values to form an rgb spectrum

import math

#initialize spectrum of rgb colours
def initialize(obj, stripSize, defaultBrightness):
    rampSize = stripSize/6
    step = math.floor(255/rampSize)
    i = 0
    while i < rampSize:        
        obj.setPixel(i,i,defaultBrightness, 255,i*step,0)
        obj.setPixel(i+rampSize,i+rampSize,defaultBrightness,255-i*step,255,0)
        obj.setPixel(i+rampSize*2,i+rampSize*2,defaultBrightness,0,255,i*step)
        obj.setPixel(i+rampSize*3,i+rampSize*3,defaultBrightness,0,255-i*step,255)
        obj.setPixel(i+rampSize*4,i+rampSize*4,defaultBrightness,i*step,0,255)
        obj.setPixel(i+rampSize*5,i+rampSize*5,defaultBrightness,255,0,255-i*step)
        i+=1