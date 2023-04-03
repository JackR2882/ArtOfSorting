class Display_Updater():
    def __init__(self):
        self.recievePipe = None
        self.sendPipe = None


    def send(self, currAlg=None, nextAlg=None):
        #print("sending: " + currAlg + " & " + nextAlg)
        self.sendPipe.send([currAlg, nextAlg])

    # recive updated slowdowns from ui
    def recieve(self):
        return(self.recievePipe.recv())
