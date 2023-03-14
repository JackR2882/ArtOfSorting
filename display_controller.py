# controller to handle viusal output to display

class display:
    def __init__(self):
        # initalize relevant variables
        self.currAlg = None

    def update(self):
        print(self.currAlg)