# basic implementation of bubble sort:

import audio_controller_temp

unsorted = True
#unsorted = False

def sort(obj):
    
    audio = audio_controller_temp.AudioOut()

    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(1, len(obj.stripState)):

            audio.out(obj.stripState[i][0])

            currVal = obj.stripState[i]
            prevVal = obj.stripState[i-1]
            obj.stripState[i] = [0,255,255,255,255]
            obj.update()

            if currVal < prevVal:
                #swap values
                obj.stripState[i] = prevVal
                obj.stripState[i-1] = currVal
                unsorted = True
            else:
                obj.stripState[i] = currVal            
            obj.update()
    print("Sorted!")