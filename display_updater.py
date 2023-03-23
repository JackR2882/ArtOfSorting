class Display_Updater():
    def __init__(self):
        self.sender = None

    def send(self, currAlg=None, nextAlg=None, swapSD=None, compareSD=None, volume=None):
        self.sender.send([currAlg, nextAlg, swapSD, compareSD, volume])