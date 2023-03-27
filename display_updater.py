class Display_Updater():
    def __init__(self):
        self.pipe = None


    def send(self, currAlg=None, nextAlg=None):
        self.pipe.send([currAlg, nextAlg])

    # recive updated slowdowns from ui
    def recieve(self):
        return(self.pipe.recv())
