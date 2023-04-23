# Class to manage updates to and from the display:
# contains two pipes, one to send and one to recieve, and uses these to send values back and forth



class DisplayUpdater():

    def __init__(self):
        self.recievePipe = None
        self.sendPipe = None

    # send updated labels to ui
    def send(self, currAlg=None, nextAlg=None):
        self.sendPipe.send([currAlg, nextAlg])

    # recive updated slowdowns from ui
    def recieve(self):
        return(self.recievePipe.recv())
