#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
import speech_recognition
from init import buffer
#from init import generate_spectrum
import audio_controller_temp as audio_controller
#import LED_controller
import time

#setup main object, runs the sorting algorithms
main = main.Main()

# buffer for audio out
audioBuff = None

#LED = None

def thread_listen():
    while True: # need to listen in a loop
        interrupt_val = speech_recognition.listen()
        main.interrupt(interrupt_val)

def thread_main():
    #main.run(LED, audioBuff)
    main.run(audioBuff)

def thread_out():
    global audioBuff
    audioBuff = buffer.Buff()
    audioOut = audio_controller.AudioOut()

    #global LED
    #LED = LED_controller.LED(146)
    #generate_spectrum.initialize(LED, 146, 1)

    while True:

        #LED.update()

        #t1 = time.perf_counter()
        if len(audioBuff.buffer) > 0:
            #print(str(audioBuff.buffer[0]) + " in buffer")

            # to stop items building up in buffer, could send more than one at once if available
            # or could dynamically change duration in audio controller based on how much is in buffer

            #print(len(audioBuff.buffer))
            audioOut.out(audioBuff.buffer[0])
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
    time.sleep(0.1)
    mainThread.start()
    interruptThread.start()

