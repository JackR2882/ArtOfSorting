# Class to manage updates to and from the display:
# contains two pipes, one to send and one to recieve, and uses these to send values back and forth



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
