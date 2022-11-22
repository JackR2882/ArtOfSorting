#thread_listen() -> listens for commands from user
#thread_main() -> runs the main thread (responsible for queueing and running sorting algorithms)
 
import main
import threading
#import time

#setup main object, runs the sorting algorithms
main = main.Main()

def thread_listen():
    print("listening")
    while True:
        x = input()
        main.interrupt(x)

def thread_main():
    main.run()

#start threads
if __name__ == "__main__":
    mainThread = threading.Thread(target=thread_main)    
    interruptThread = threading.Thread(target=thread_listen)
    mainThread.start()
    interruptThread.start()

#time.sleep(2)
#mainThread.stop()