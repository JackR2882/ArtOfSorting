#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import multiprocessing
import speech_recognition
import audio_controller

#setup main object, runs the sorting algorithms
main = main.Main()

# buffer for display out
displayObj = None

#LED = None

def process_listen(sender):
    while True: # need to listen in a loop
        interupt = speech_recognition.listen()
        sender.send(interupt) # send through pipe to thread interupt

def thread_interupt(reciver):
    interupt = reciver.recv() # recieve from process_listen
    main.interrupt(interupt)

def thread_main():
    main.run(audioObj)

#start threads
if __name__ == "__main__":

    # define audio output object
    global audioObj
    audioObj = audio_controller.AudioOut()

    # define pipe between listenProcess and interuptThread
    sender, reciever = multiprocessing.Pipe()

    # define + start main and interrupt threads
    mainThread = threading.Thread(target=thread_main)    
    mainThread.start()
    interuptThread = threading.Thread(target=thread_interupt, args=(reciever,))
    interuptThread.start()

    # define + start listenerProcess
    listenerProcess = multiprocessing.Process(target=process_listen, args=(sender,))
    listenerProcess.start()

    # define + start audio output thread
    audioOutThread = threading.Thread(target=audioObj.audio_out)
    audioOutThread.start()

