# working

# the following resource was used in the writing of this function: https://www.javatpoint.com/counting-sort


import time


def sort(obj):

    obj.update()

    #print(obj.stripState[0:4])
    arr = obj.stripState
    #print(arr)




    def count(arr, item):
        counter = 0
        for i in range(0, len(arr)):
            if arr[i][0] == item:
                counter += 1
        return counter

    # find max item in array:
    max_i = 0
    for i in range(1, len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
            

    # init arr of length max + 1
    new_arr = [0]*(int(arr[max_i][0])+1)



    obj.clear()
    obj.stripState = [[0,0,0,0,0]]*144


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

    #print("raw-count: ")
    #print(new_arr)


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

    #print("cumulative-count: ")
    #print(new_arr)
    
    #obj.stripState = arr
    sorted_arr = obj.stripState
    obj.stripState = arr.copy()
    obj.update()


    # sort items:
    for i in range(0, len(arr)):
        index = new_arr[int(arr[i][0])]-1
        #print(index)
        #index = new_arr

        sorted_arr[index] = arr[i]


        # need to deal with multiple items overlapping:
        try:
            n = (new_arr[(arr[i][0])]) - (new_arr[(arr[i][0])-1])
            #print("1: " + str(new_arr[int(arr[i][0])])+ ", 2: " + str(new_arr[int(arr[i][0])-1]))
            #n = (144 - index)-1        
        except:
            n = index

        while n > 0:
            sorted_arr[index-n] = arr[i]
            obj.stripState[index-n] = arr[i]
            n -= 1
            obj.update()


    
    #time.sleep(2.5)
    #obj.clear()
    #time.sleep(2.5)


    #print(sorted_arr)

    #print(new_arr)

    #print("---------------------------------------------------------------")
    #for i in range(1, len(sorted_arr)):
        #print("val: " + str(int(sorted_arr[i][0])) + ", diff: " + str((new_arr[(arr[i][0])]) - (new_arr[(arr[i][0])-1])))
    #    print(sorted_arr[i][0])
    #print("---------------------------------------------------------------")

    #print(len(sorted_arr))


