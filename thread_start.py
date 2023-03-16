#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import speech_recognition
from init import buffer
import audio_controller_temp as audio_controller
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
    main.run(audioBuff, displayObj)

def thread_out():
    #global audioObj
    global audioBuff
    audioBuff = buffer.Buff()
    audioObj = audio_controller.AudioOut()

    global displayObj
    displayObj = display_controller.display()

    while True:

        
        if displayObj.changed:
            displayObj.update()

        #t1 = time.perf_counter()
        if len(audioBuff.buffer) > 0:
            #print(str(audioBuff.buffer[0]) + " in buffer")

            # to stop items building up in buffer, could send more than one at once if available
            # or could dynamically change duration in audio controller based on how much is in buffer

            #print(len(audioBuff.buffer))
            audioObj.out(audioBuff.buffer[0])
            audioBuff.remove()
        #t2 = time.perf_counter()
        #print("time: " + str(t2-t1))



#start threads
if __name__ == "__main__":

    mainThread = threading.Thread(target=thread_main)    
    interruptThread = threading.Thread(target=thread_listen)
    outThread = threading.Thread(target=thread_out)
    outThread.start()

    # start these fractionally later, to give time for audio and LED objects to be generated
    print("Initializing...")
    time.sleep(2)
    mainThread.start()
    interruptThread.start()

