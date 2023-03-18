# broken - can find a way to fix / git revert / just get rid of it, 
#        - fixed an issue with raw count though, so may be worth trying to preserve that

# the following resource was used in the writing of this function: https://www.javatpoint.com/counting-sort


import time

def sort(obj):

    swapSD = obj.swapSD
    compareSD = obj.compareSD

    arr = obj.stripState

    #def count(arr, item):
    #    counter = 0
    #    for i in range(0, len(arr)):
    #        #time.sleep(compareSD) # this is technically the correct delay - but doesn't work well
    #        if arr[i][0] == item:
    #            counter += 1

    #    time.sleep(compareSD)
    #    return counter


    # find max item in array:
    max_i = 0
    for i in range(1, len(arr)):
        time.sleep(compareSD)
        if arr[max_i] < arr[i]:
            max_i = i


    # init arr of length max + 1
    new_arr = [0]*(int(arr[max_i][0])+1)


    # clear array, before frequency count is to be displayed
    obj.clear()
    obj.stripState = [[0,224,0,0,0]]*146


    # work out and display frequencies (count items)
    # raw count:
    for i in range(0, len(new_arr)):
        time.sleep(compareSD)

        new_arr[arr[i][0]] += 1 # update with raw count

        # display frequencies as the colour white on the led strip: -> frequency of pixel corresponds to the brightness of its pixel
        ratio = (new_arr[arr[i][0]]) / 30
        obj.stripState[arr[i][0]] = [i,int(255 - (12*ratio)),int(255*ratio),int(255*ratio),int(255*ratio)]
        obj.update()



    # work out and display cumulative frequencies
    # cumulative-count:
    acc = 0
    for i in range(0, len(new_arr)):
        time.sleep(compareSD)
        acc += new_arr[i]
        new_arr[i] = acc

        # display cumulative frequencies as white pixels on the led strip -> same as above
        ratio = (acc+1)/145
        try: 
            obj.stripState[i] = [i,int(255 - (12*ratio)),int(255*ratio),int(255*ratio),int(255*ratio)]
        except:
            obj.stripState[i] = [i,0,255,255,255]
        obj.update()


    
    # revert strip state back to initial state
    sorted_arr = obj.stripState
    obj.stripState = arr.copy()
    obj.update()


    # sort items:
    for i in range(0, len(arr)):
        time.sleep(compareSD)

        index = new_arr[int(arr[i][0])]-1

        sorted_arr[index] = arr[i]


        # need to deal with multiple items overlapping:
        try:
            n = (new_arr[(arr[i][0])]) - (new_arr[(arr[i][0])-1])
            #print("1: " + str(new_arr[int(arr[i][0])])+ ", 2: " + str(new_arr[int(arr[i][0])-1]))
            #n = (146 - index)-1        
        except:
            n = index

        #while n > 0:
        #    sorted_arr[index-n] = arr[i]
        #    obj.stripState[index-n] = arr[i]
        #    n -= 1
        #    obj.update()

    print("this is broken - need to fix ^")


