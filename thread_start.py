#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import speech_recognition
import audio_controller

#setup main object, runs the sorting algorithms
main = main.Main()

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

#start threads
if __name__ == "__main__":

    # define audio output object
    global audioObj
    audioObj = audio_controller.AudioOut()

    # define + start main and interrupt threads
    mainThread = threading.Thread(target=thread_main)    
    interruptThread = threading.Thread(target=thread_listen)
    mainThread.start()
    interruptThread.start()

    # define + start audio output thread
    audioOutThread = threading.Thread(target=audioObj.audio_out)
    audioOutThread.start()

