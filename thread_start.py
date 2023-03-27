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

def process_display(pipe):
    displayObj = display_controller.Display()

    # recieve from 
    def rcv():
        update = pipe.recv()
        displayObj.change(update)
    
    t1 = threading.Thread(target=rcv)
    t1.start()

    displayObj.refresh()


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
    pipe1, pipe2 = multiprocessing.Pipe(True)

    # define display update object
    displayUpdateObj = display_updater.Display_Updater
    displayUpdateObj.sender = pipe1

    # define + start displayProcess
    displayProcess = multiprocessing.Process(target=process_display, args=(pipe2,))
    displayProcess.start()

    # define pipe between listenProcess and interuptThread
    sender, reciever = multiprocessing.Pipe()

    # define + start main and interrupt threads
    mainThread = threading.Thread(target=thread_main, args=(displayUpdateObj,))    
    mainThread.start()
    interuptThread = threading.Thread(target=thread_interupt, args=(reciever,))
    interuptThread.start()

    # define + start listenerProcess
    listenerProcess = multiprocessing.Process(target=process_listen, args=(sender,))
    listenerProcess.start()

    # define + start audio output thread
    audioOutThread = threading.Thread(target=audioObj.audio_out)
    audioOutThread.start()

