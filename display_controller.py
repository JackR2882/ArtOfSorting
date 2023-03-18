# controller to handle viusal output to display

import tkinter
from tkinter import ttk
import os

# set correct display
if os.environ.get('DISPLAY','') == '':
    #print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


class display:
    def __init__(self):

        #changed flag (tells the update loop when to update)
        self.changed = False

        # initalize window
        self.root = tkinter.Tk()
        self.root.geometry('500x300')
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        
        #self.root.wm_attributes('-fullscreen', 'True') # enable later -> will stretch window to fit fullscreen
                                                        # without header toolbar, irrespective of screen size

        # initalize relevant variables + outputs
        self.currAlg = ""
        self.currAlgLbl = ttk.Label(self.frm, text=self.currAlg).grid(column=0, row=0)
        
        self.swapSD = 0.0
        self.compareSD = 0.0
        self.swapSDLbl = ttk.Label(self.frm, text="Current algorithm: " + self.currAlg, anchor="e").grid(column=0, row=1)
        self.compareSDLbl = ttk.Label(self.frm, text=self.currAlg, anchor="e").grid(column=0, row=2)
        self.sExplainLbl = ttk.Label(self.frm, text="Slow down is performed on an item swap in array, that is, whenever an item changes position.", wraplength=300, justify="left").grid(column=1, row=1)
        self.sExplainLbl = ttk.Label(self.frm, text="Slow down is performed on an item comparison, that is, whenever two items are compared.", wraplength=300, justify="left").grid(column=1, row=2)
        
        self.nextAlg = ""
        self.nextAlgLbl = ttk.Label(self.frm, text="Next algorithm: " + self.nextAlg).grid(column=0, row=4)

        #ttk.Label(frm, text=self.currAlg).grid(column=0, row=0)

    def change(self, currAlg=None, nextAlg=None, swapSD=None, compareSD=None):
        if currAlg:
            self.currAlg = currAlg
        if swapSD:
            self.swapSD = swapSD
        if compareSD:
            self.compareSD = compareSD
        if nextAlg:
            self.nextAlg = nextAlg
        self.changed = True

    def update(self):
        self.currAlgLbl = ttk.Label(self.frm, text="Current algorithm: "+ self.currAlg).grid(column=0, row=0)
        self.swapSDLbl = ttk.Label(self.frm, text=("Swap slowdown: " + str(self.swapSD)), anchor="e").grid(column=0, row=1)
        self.compareSDLbl = ttk.Label(self.frm, text=("Comparison slowdown: " + str(self.swapSD)), anchor="e").grid(column=0, row=2)
        self.nextAlgLbl = ttk.Label(self.frm, text="Next algorithm: " + self.nextAlg).grid(column=0, row=4)

        self.root.update()
        self.changed = False


#import time
#DISPLAY = display()
#DISPLAY.update()

#time.sleep(1)
#DISPLAY.currAlg = "bubble_sort"
#DISPLAY.update()
#time.sleep(1)
#DISPLAY.currAlg = "merge_sort"
#DISPLAY.update()


# just to stop program exiting -> REMOVE LATER
#time.sleep(5000)






#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


