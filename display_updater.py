class Display_Updater():
    def __init__(self):
        self.pipe = None


    def send(self, currAlg=None, nextAlg=None, volume=None):
        self.pipe.send([currAlg, nextAlg, volume])

    # recive updated slowdowns from ui
    def recieve(self):
        return(self.pipe.recv())
