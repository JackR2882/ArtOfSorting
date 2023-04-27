# inspired by the following resource:
#  - https://www.javatpoint.com/counting-sort

# basic implementation of counting sort:

import time

def sort(obj, audioObj):

    default_b = obj.stripState[0][1]

    arr = obj.stripState

    # find max item in array:
    max_i = 0
    for i in range(1, len(arr)):
        if arr[max_i] < arr[i]:
            obj.highlight(i, i+1, default_b)
            max_i = i
        audioObj.update(arr[i][0])
        time.sleep(obj.compareSD+obj.swapSD)
        


    # init empty arr
    new_arr = [0]*(len(arr))



    # clear array, before frequency count is to be displayed
    obj.clear()
    obj.stripState = [[0,224,0,0,0]]*144



    # work out and display frequencies (count items)
    # raw count:
    for i in range(0, len(new_arr)):

        audioObj.update(arr[i][0])
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

        audioObj.update(arr[i][0])

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



    # sorting loop
    for i in range(0, len(arr)):

        audioObj.update(arr[i][0])

        new_arr[int(arr[i][0])] -= 1
        index = new_arr[int(arr[i][0])]

        obj.stripState[index] = arr[i]

        obj.update()
        obj.update()
        obj.update()

        time.sleep(obj.swapSD)



    # index:        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # arr:          1, 1, 2, 1, 3, 2, 4, 1, 2, 0
    # raw:          1, 4, 3, 1, 1, 0, 0, 0, 0, 0
    # cumulative:   1, 5, 8, 9,10,10,10,10,10,10


