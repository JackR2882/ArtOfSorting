#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import speech_recognition
import audio_controller
import display_controller
import time

#setup main object, runs the sorting algorithms
main = main.Main()

# buffer for audio out
audioBuff = None

# buffer for display out
displayObj = None

#LED = None

def thread_listen():
    while True: # need to listen in a loop
        interrupt_val = speech_recognition.listen()
        main.interrupt(interrupt_val)
        #interrupt_val2 = input("Control slowdowns here: ")
        #main.interrupt2(interrupt_val2)

def thread_main():
    main.run(audioObj, displayObj)

def thread_out():
    # mights as well define both output objects together
    global audioObj
    audioObj = audio_controller.AudioOut()
    global displayObj
    displayObj = display_controller.display()

    #while True:
    #    if displayObj.changed:
    #        displayObj.update()



#start threads
if __name__ == "__main__":

    mainThread = threading.Thread(target=thread_main)    
    interruptThread = threading.Thread(target=thread_listen)
    outThread = threading.Thread(target=thread_out)
    outThread.start()

    # start these fractionally later, to give time for audio and LED objects to be generated
    print("Initializing...")
    time.sleep(2)

    audioOutThread = threading.Thread(target=audioObj.audio_out)
    audioOutThread.start()

    mainThread.start()
    interruptThread.start()

