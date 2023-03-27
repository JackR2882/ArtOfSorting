# controller to handle viusal output to display

# SCREEN DIMENSIONS: 800x480

import tkinter
from tkinter import ttk
import os


# set correct display

if os.environ.get('DISPLAY','') == '':
    #print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


class Display:
    def __init__(self):

        # initalize window
        self.root = tkinter.Tk()
        #self.root.geometry('800x480')
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        
        self.root.wm_attributes('-fullscreen', 'True')  # enable later -> will stretch window to fit fullscreen
                                                        # without header toolbar, irrespective of screen size

        # make sure cursor is disabled
        self.root.config(cursor="none")

        # initalize relevant variables + outputs
        self.currAlg = "long algorithm name here"
        self.currAlgLbl = ttk.Label(self.frm, text="Current algorithm: " + self.currAlg, font=("Times", 40), wraplength=790)
        self.currAlgLbl.grid(column=0, row=0, columnspan=6, rowspan=3)

        self.swapSD = 0.0
        self.compareSD = 0.0
        self.swapSDLbl = ttk.Label(self.frm, text="Swap SD: " + str(self.swapSD), justify='left', font=('Times', 25), width=20)
        self.swapSDLbl.grid(column=0, row=6, rowspan=3) # need to do this separately as .grid() returns none
        self.compareSDLbl = ttk.Label(self.frm, text="Comparison SD: " + str(self.compareSD), justify='left', font=("Times", 25), width=20)
        self.compareSDLbl.grid(column=0, row=9, rowspan=3)
        self.sExplainLbl = ttk.Label(self.frm, text="Slow down is performed on an item swap in array, that is, whenever an item changes position.", wraplength=300, justify="left", font=("Times", 15))
        self.sExplainLbl.grid(column=3, row=6, rowspan=3)
        self.cExplainLbl = ttk.Label(self.frm, text="Slow down is performed on an item comparison, that is, whenever two items are compared.", wraplength=300, justify="left", font=("Times", 15))
        self.cExplainLbl.grid(column=3, row=9, rowspan=3)
        
        self.volume = 0.0
        self.volumeLbl = ttk.Label(self.frm, text="Volume: " + str(self.volume), justify='left', font=("Times", 25), width=20)
        self.volumeLbl.grid(column=0, row=12, rowspan=3)


        #self.slide_val = tkinter.DoubleVar()
        #self.slide_val.set(0.0)
        #self.slider = ttk.Scale(self.frm, from_=0, to=100, orient='horizontal', variable=self.slide_val)
        #self.slider.grid(column=3, row=18, columnspan=4)
        #self.volSlider = ttk.Scale(self.frm, from_=0, to=100, orient='horizontal', variable=self.volume)
        #self.volSlider.grid(column = 3, row=12, rowspan=3)
        
        # works, but only applies changes on update -> not very responsive
        button = ttk.Button(self.frm, text ="Hello", command=self.test)
        button.grid(column=3, row=3, rowspan=3)

        self.nextAlg = "long algorithm name here"
        self.nextAlgLbl = ttk.Label(self.frm, text="Next algorithm: " + str(self.nextAlg), justify='left', font=("Times", 25))
        self.nextAlgLbl.grid(column=0, row=15, columnspan=4)

        #self.root.mainloop()

    def test(self):
            print("works")

    def change(self, update):
        if update[0]:
            self.currAlg = update[0]
        if update[1]:
            self.nextAlg = update[1]
        if update[2]:
            self.swapSD = update[2]
        if update[3]:
            self.compareSD = update[3]
        if update[4]:
            self.volume = update[4]

        #print(self.volSlider.get())

        # update label text values
        #self.currAlgLbl.config(text="Current algorithm: " + self.currAlg)
        #self.swapSDLbl.config(text="Swap SD: " + str(self.swapSD))
        #self.compareSDLbl.config(text="Comparison SD: " + str(self.compareSD))
        #self.nextAlgLbl.config(text="Next algorithm: " + str(self.nextAlg))

        #self.refresh()

    def refresh(self):
        while True:
            # update label text values
            self.currAlgLbl.config(text="Current algorithm: " + self.currAlg)
            self.swapSDLbl.config(text="Swap SD: " + str(self.swapSD))
            self.compareSDLbl.config(text="Comparison SD: " + str(self.compareSD))
            self.nextAlgLbl.config(text="Next algorithm: " + str(self.nextAlg))
            
            #print(self.slide_val.get())

            # refresh screen with new values
            self.root.update()

    #def interrupt(self, pipe):
    #    while True:
    #        update = pipe.recv()
    #        self.change(update)

