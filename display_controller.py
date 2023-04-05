# controller to handle viusal output to display
# SCREEN DIMENSIONS: 800x480

import tkinter
import os
import customtkinter as ctk


# set correct display
if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')


class Display:
    def __init__(self):

        ctk.set_appearance_mode("Dark")

        # initalize window
        self.root = ctk.CTk()
        
        self.root.wm_attributes('-fullscreen', 'True')  # enable later -> will stretch window to fit fullscreen
                                                        # without header toolbar, irrespective of screen size

        # make sure cursor is disabled
        self.root.config(cursor="none")

        # initalize relevant variables + outputs
        self.currAlg = "placeholder"
        self.currAlgLbl = ctk.CTkLabel(self.root, text="Current algorithm: " + self.currAlg, font=("Times", 60), wraplength=790)
        self.currAlgLbl.place(relx=0.01, rely=0.1, anchor=tkinter.W)

        self.swapSD = tkinter.DoubleVar(0.0)
        self.compareSD = tkinter.DoubleVar(0.0)

        self.swapSDLbl = ctk.CTkLabel(self.root, text="Swap SD: " + str(self.swapSD), justify='left', font=('Times', 39), width=20)
        self.swapSDLbl.place(relx=0.01, rely=0.4, anchor=tkinter.W)
        self.compareSDLbl = ctk.CTkLabel(self.root, text="Comparison SD: " + str(self.compareSD), justify='left', font=("Times", 39), width=20)
        self.compareSDLbl.place(relx=0.01, rely=0.6, anchor=tkinter.W)
        self.sExplainLbl = ctk.CTkLabel(self.root, text="Slow down is performed on an item swap in array, that is, whenever an item changes position.", wraplength=390, justify="left", font=("Times", 25))
        self.sExplainLbl.place(relx=0.5, rely=0.4, anchor=tkinter.W)
        self.cExplainLbl = ctk.CTkLabel(self.root, text="Slow down is performed on an item comparison, that is, whenever two items are compared.", wraplength=390, justify="left", font=("Times", 25))
        self.cExplainLbl.place(relx=0.5, rely=0.6, anchor=tkinter.W)

        # initialize and display sliders for swap and comparison slowdowns
        self.swapSlider = ctk.CTkSlider(self.root, from_=0, to=0.1, orientation='horizontal', variable=self.swapSD, width=385, number_of_steps=20)
        self.swapSlider.place(relx=0.01, rely=0.5, anchor=tkinter.W)
        self.compareSlider = ctk.CTkSlider(self.root, from_=0, to=0.1, orientation='horizontal', variable=self.compareSD, width=385, number_of_steps=20)
        self.compareSlider.place(relx=0.01, rely=0.7, anchor=tkinter.W)

        self.nextAlg = "placeholder"
        self.nextAlgLbl = ctk.CTkLabel(self.root, text="Next algorithm: " + str(self.nextAlg), justify='left', font=("Times", 39))
        self.nextAlgLbl.place(relx=0.05, rely=0.9, anchor=tkinter.W)



    def change(self, update):
        if update[0]:
            self.currAlg = update[0]
        if update[1]:
            self.nextAlg = update[1]



    def refresh(self):
        while True:
            # update label text values
            self.currAlgLbl.configure(text="Current algorithm: " + self.currAlg)
            self.swapSDLbl.configure(text="Swap SD: " + str(self.swapSD))
            self.compareSDLbl.configure(text="Comparison SD: " + str(self.compareSD))
            self.nextAlgLbl.configure(text="Next algorithm: " + str(self.nextAlg))

            # update values based on current slider position
            self.swapSD = round(self.swapSlider.get(),3)
            self.compareSD = round(self.compareSlider.get(),3)

            # refresh screen with new values
            self.root.update()
