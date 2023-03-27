#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import multiprocessing
import speech_recognition
import audio_controller
import display_controller
import display_updater
import time

#setup main object, runs the sorting algorithms
main = main.Main()

# process takes pipe as argument, sets up two threads, one to update display values based on values recieved from pipe
# and one to recieve updated slowdown values to pass back to main thread
# also refreshes display at steady intervals
def process_display(pipe):
    displayObj = display_controller.Display()

    # recieve updated labels from display updater
    def rcv():
        update = pipe.recv()
        displayObj.change(update)

    # send updated slowdowns to display updater
    def send():
        while True:
            time.sleep(1)
            pipe.send((displayObj.swapSD, displayObj.compareSD))
    
    t1 = threading.Thread(target=rcv)
    t1.start()
    t2 = threading.Thread(target=send)
    t2.start()

    # start display refreshing loop
    displayObj.refresh()

# process to listen to audio from microphone and send message through pipe to thread_interrupt when hotword detected
def process_listen(sender):
    while True: # need to listen in a loop
        interupt = speech_recognition.listen()
        sender.send(interupt) # send through pipe to thread interupt

# recives hotword message from pipe and interrupts main with that message
def thread_interupt(reciever):
    interupt = reciever.recv() # recieve from process_listen
    main.interrupt(interupt)

# recieves updated slowdown values through pipe and updates LED obj with these values
# also runs main
def thread_main(displayUpdateObj):
    def recv():
        while True:
            updatedSD = displayUpdateObj.recieve(displayUpdateObj)
            main.LED.swapSD = updatedSD[0]
            main.LED.compareSD = updatedSD[1]
    
    t1 = threading.Thread(target = recv)
    t1.start()

    main.run(audioObj, displayUpdateObj)

#start threads
if __name__ == "__main__":

    # define audio output object
    global audioObj
    audioObj = audio_controller.AudioOut()

    # define pipe between displayUpdateObj and displayProcess (pipe is bi-directional)
    pipe1, pipe2 = multiprocessing.Pipe(True)

    # define display update object
    displayUpdateObj = display_updater.Display_Updater
    displayUpdateObj.pipe = pipe1

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

