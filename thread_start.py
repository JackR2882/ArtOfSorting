# entry point for system, spawns all threads / processes used by system

# wait for new usb connection before continuing, prevents seg fault if speaker is connected after boot
import pyudev # sourced from: https://pyudev.readthedocs.io/en/v0.14/api/monitor.html
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='input')
for _, _ in monitor:
    break

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
def process_display(sendPipe, recievePipe):
    displayObj = display_controller.Display()

    # recieve updated labels from display updater
    def rcv():
        while True:
            update = recievePipe.recv()
            #print("receiving: " + update[0] + " & " + update[1])
            displayObj.change(update)

    # send updated slowdowns to display updater - doesn't need to be that responsive so can do once every second
    def send():
        while True:
            time.sleep(1)
            sendPipe.send((displayObj.swapSD, displayObj.compareSD, displayObj.shuffleMode))
    
    t1 = threading.Thread(target=rcv)
    t1.start()
    t2 = threading.Thread(target=send)
    t2.start()

    # start display refresh loop
    displayObj.refresh()

# process to listen to audio from microphone and send message through pipe to thread_interrupt when hotword detected
def process_listen(sender):
    while True: # need to listen in a loop
        interupt = speech_recognition.listen()
        sender.send(interupt) # send through pipe to thread interupt
        speech_recognition.clear() # to prevent trailing end of word being detected

# recives hotword message from pipe and interrupts main with that message
def thread_interupt(reciever):
    while True:
        interupt = reciever.recv() # recieve from process_listen
        main.interrupt(interupt)

# recieves updated slowdown values, and shuffle mode through pipe and updates LED obj with these values
# also runs main
def thread_main(displayUpdateObj):
    def rcv():
        while True:
            ret = displayUpdateObj.recieve(displayUpdateObj)
            main.LED.swapSD = ret[0]
            main.LED.compareSD = ret[1]
            main.LED.shuffleMode = ret[2]
    
    t1 = threading.Thread(target = rcv)
    t1.start()

    main.run(audioObj, displayUpdateObj)

#start threads
if __name__ == "__main__":

    # define audio output object
    global audioObj
    audioObj = audio_controller.AudioOut()

    # define pipe between displayUpdateObj and displayProcess (pipe is bi-directional) <- changed to use separate pipes
    pipe1, pipe2 = multiprocessing.Pipe(True)
    pipe3, pipe4 = multiprocessing.Pipe()

    # define display update object
    displayUpdateObj = display_updater.Display_Updater
    displayUpdateObj.recievePipe = pipe1
    displayUpdateObj.sendPipe = pipe3

    # define + start displayProcess
    displayProcess = multiprocessing.Process(target=process_display, args=(pipe2,pipe4,))
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

