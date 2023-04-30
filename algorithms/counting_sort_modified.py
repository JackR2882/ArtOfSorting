# inspired by the following resource:
#  - https://www.javatpoint.com/counting-sort

# modified implmentation of counting sort - for use as a subroutine in radix sort,
# so includes the ability to specify a 'granularity' with which to sort by

import math
import time

def sort(obj, audioObj, off):

    default_b = obj.stripState[0][1]

    arr = obj.stripState.copy()

    

    # init empty arr
    new_arr = [0]*(len(arr))


    # clear array, before frequency count is to be displayed
    obj.clear()
    obj.stripState = [[0,224,0,0,0]]*len(arr)
    
    

    # work out and display frequencies (count items)
    # raw count:
    for i in range(0, len(new_arr)):

        audioObj.update(arr[i][0])
        new_arr[math.floor(arr[i][0]/off)] += 1 # update with raw count
        
        # display frequencies as the colour white on the led strip: -> frequency of pixel corresponds to the brightness of its pixel
        ratio = (new_arr[math.floor(arr[i][0]/off)]) / 101
        obj.stripState[math.floor(arr[i][0]/off)] = [i,int(255 - (12*ratio)),int(255*ratio),int(255*ratio),int(255*ratio)]
        obj.update()
        obj.update()
        obj.update()
        
        time.sleep(obj.swapSD) # technically updating array, so count as swap

    raw_count = new_arr.copy()



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

    
    
    for i in range(0, len(arr)):

        audioObj.update(arr[i][0])

        index = new_arr[int(math.floor(arr[i][0]/off))]
        val = raw_count[int(math.floor(arr[i][0])/off)]

        raw_count[int(math.floor(arr[i][0])/off)] -= 1

        obj.stripState[index-val] = arr[i]

        obj.update()
        obj.update()
        obj.update()

        time.sleep(obj.swapSD)







    # count the number of occurences of a given item within an input array
    #def count(arr, item):
    #    counter = 0
    #    for i in range(0, len(arr)):
    #        if int(math.floor(arr[i][0]/off)) == item:
    #            counter += 1
    #    return counter


    # find the maximum value item in array:
    #max_i = 0
    #for i in range(1, len(arr)):
    #    if math.floor(arr[max_i][0]/off) < math.floor(arr[i][0]/off): # (first item in ret arr is ID value)
    #        max_i = i
            

    # initialize arr of length max + 1
    #new_arr = [0]*(int(arr[max_i][0]/off)+1)


    # work out frequencies (count items)
    # raw count:
    #for i in range(0, len(new_arr)):
    #    new_arr[i] = count(arr, i)

    #print("raw count: " + str(new_arr))

    # work out cumulative frequencies
    # cumulative-count:
    #acc = 0
    #for i in range(0, len(new_arr)):
    #    acc += new_arr[i]
    #    new_arr[i] = acc

    #print("cum count: " + str(new_arr))
    
    # revert strip state back to initial state
    #sorted_arr = obj.stripState

    # sort items:
    #for i in range(0, len(arr)):
    #    offset = math.floor(arr[i][0]/off)
    #    index = new_arr[offset]-1 # get index of item as corresponding item from cumulative freq array
    #    new_arr[offset] -= 1

    #    sorted_arr[index] = arr[i]
        
    #    obj.update()
    #    obj.update()
    #    obj.update()


