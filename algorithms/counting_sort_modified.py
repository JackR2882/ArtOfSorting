# modified implmentation of counting sort - for use as a subroutine in radix sort, so includes the ability to specify a 
# 'granularity' with which to sort by
# the following resource was used in the writing of this function: https://www.javatpoint.com/counting-sort

def sort(obj, off):


    arr = obj.stripState


    # count the number of occurences of a given item within an input array
    def count(arr, item):
        counter = 0
        for i in range(0, len(arr)):
            if int(arr[i][0]/off) == item:
                counter += 1
        return counter


    # find the maximum value item in array:
    max_i = 0
    for i in range(1, len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
            

    # initialize arr of length max + 1
    new_arr = [0]*(int(arr[max_i][0]/off)+1)

    print("count length: " + str(len(new_arr)))


    # clear array, before frequency count is to be displayed
    obj.clear()
    obj.stripState = [[0,0,0,0,0]]*144


    # work out and display frequencies (count items)
    # raw count:
    for i in range(0, len(new_arr)):
        new_arr[i] = count(arr, i)

        # display frequencies as the colour white on the led strip: -> frequency of pixel corresponds to the brightness of its pixel
        ratio = (count(arr, i)+1) / 30
        try: 
            obj.stripState[i] = [i,int(255 - (12*ratio)),int(255*ratio),int(255*ratio),int(255*ratio)]
        except:
            obj.stripState[i] = [i,0,255,255,255]
        obj.update()

    #time.sleep(1) # sleep 1s to display pixel frequencies before starting sorting


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

    #time.sleep(1) # sleep 1s to display cumulative pixel frequencies before starting sorting

    
    # revert strip state back to initial state
    sorted_arr = obj.stripState
    obj.stripState = arr.copy()
    obj.update()


    # sort items:
    for i in range(0, len(arr)):
        index = new_arr[int(arr[i][0]/off)]-1 # get index of item as corresponding item from cumulative freq array

        sorted_arr[index] = arr[i]

        # need to deal with multiple items overlapping:
        try:
            n = (new_arr[int(arr[i][0]/off)]) - (new_arr[int(arr[i][0]/off)-1])
        except:
            n = index

        while n > 0:
            sorted_arr[index-n] = arr[i]
            obj.stripState[index-n] = arr[i]
            n -= 1
            obj.update()


