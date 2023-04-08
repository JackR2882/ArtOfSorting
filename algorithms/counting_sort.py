# inspired by the following resource:
#  - https://www.javatpoint.com/counting-sort

# basic implementation of insertion sort:

import time

def sort(obj):

    arr = obj.stripState

    # find max item in array:
    max_i = 0
    for i in range(1, len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
        time.sleep(obj.compareSD)



    # init empty arr
    new_arr = [0]*(len(arr)-1)



    # clear array, before frequency count is to be displayed
    obj.clear()
    obj.stripState = [[0,224,0,0,0]]*146



    # work out and display frequencies (count items)
    # raw count:
    for i in range(0, len(new_arr)):
        new_arr[arr[i][0]] += 1 # update with raw count
        
        # display frequencies as the colour white on the led strip: -> frequency of pixel corresponds to the brightness of its pixel
        ratio = (new_arr[arr[i][0]]) / 30
        obj.stripState[arr[i][0]] = [i,int(255 - (12*ratio)),int(255*ratio),int(255*ratio),int(255*ratio)]
        obj.update()
        obj.update()
        obj.update()
        
        time.sleep(obj.swapSD) # technically updating array, so count as swap



    # work out and display cumulative frequencies
    # cumulative-count:
    acc = 0
    for i in range(0, len(new_arr)):
        acc += new_arr[i]
        new_arr[i] = acc

        # display cumulative frequencies as white pixels on the led strip -> same as above
        ratio = (acc+1)/145
        try: 
            obj.stripState[i] = [i,int(255 - (12*ratio)),int(255*ratio),int(255*ratio),int(255*ratio)]
        except:
            obj.stripState[i] = [i,0,255,255,255]
        obj.update()
        obj.update()
        obj.update()

        time.sleep(obj.swapSD) # technically updating array, so count as swap


    
    # revert strip state back to initial state
    obj.stripState = arr.copy()
    obj.update()



    for i in range(0, len(arr)):
        index = new_arr[int(arr[i][0])]
        prev_index = new_arr[int(arr[i][0])-1]

        # need to account for repeated items:
        if prev_index > index or prev_index == 0:
            prev_index = -1
        time.sleep(obj.compareSD)

        for d in range(index, prev_index, -1):
            obj.stripState[d] = arr[i]
            obj.update()
            obj.update()
            obj.update()
            time.sleep(obj.swapSD)



    # index:        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # arr:          1, 1, 2, 1, 3, 2, 4, 1, 2, 0
    # raw:          1, 4, 3, 1, 1, 0, 0, 0, 0, 0
    # cumulative:   1, 5, 8, 9,10,10,10,10,10,10


