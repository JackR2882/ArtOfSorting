#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import multiprocessing
import speech_recognition
import audio_controller
import display_controller
import display_updater

#setup main object, runs the sorting algorithms
main = main.Main()

def process_display(reciever):
    displayObj = display_controller.Display()
    displayObj.refresh()
    while True:
        update = reciever.recv()
        displayObj.change(update)


def process_listen(sender):
    while True: # need to listen in a loop
        interupt = speech_recognition.listen()
        sender.send(interupt) # send through pipe to thread interupt

def thread_interupt(reciever):
    interupt = reciever.recv() # recieve from process_listen
    main.interrupt(interupt)

def thread_main(displayUpdateObj):
    main.run(audioObj, displayUpdateObj)

#start threads
if __name__ == "__main__":

    # define audio output object
    global audioObj
    audioObj = audio_controller.AudioOut()

    # define pipe between displayUpdateObj and displayProcess
    sender, reciever = multiprocessing.Pipe()

    # define display update object
    displayUpdateObj = display_updater.Display_Updater
    displayUpdateObj.sender = sender

    # define + start displayProcess
    displayProcess = multiprocessing.Process(target=process_display, args=(reciever,))
    displayProcess.start()

    # define pipe between listenProcess and interuptThread
    sender1, reciever1 = multiprocessing.Pipe()

    # define + start main and interrupt threads
    mainThread = threading.Thread(target=thread_main, args=(displayUpdateObj,))    
    mainThread.start()
    interuptThread = threading.Thread(target=thread_interupt, args=(reciever1,))
    interuptThread.start()

    # define + start listenerProcess
    listenerProcess = multiprocessing.Process(target=process_listen, args=(sender1,))
    listenerProcess.start()

    # define + start audio output thread
    audioOutThread = threading.Thread(target=audioObj.audio_out)
    audioOutThread.start()

