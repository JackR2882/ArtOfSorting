# basic implementation of selection sort:
# has been modified to include an offset (for use in radix sort -> sort by hundreds, tens, ones, etc...)

def sort(obj, off):

    print(obj.stripState)

    default_brightness = obj.stripState[0][1]

    for i in range(0, len(obj.stripState)-1):
        
        # keep track of current min
        min = obj.stripState[i]
        min_index = i        
        # keep track of current anchor
        mem = obj.stripState[i]
        # set pointer for current element
        obj.stripState[i] = [0,255,255,255,255]
        # update strip state
        obj.update()

        # for each item in arr:
        for n in range(i+1, len(obj.stripState)):
            
            # if current item is less than the current min value 
            if int(min[0]/off) > int(obj.stripState[n][0]/off):
                # remove old pointer
                obj.stripState[min_index] = [min[0], default_brightness, min[2], min[3], min[4]]
                # update min
                min = obj.stripState[n]
                min_index = n
                # add new pointer
                obj.stripState[n] = [0,255,255,255,255]

            else:
                # brighten current pixel value:
                curr = obj.stripState[n]
                obj.stripState[n] = [curr[0], 250, curr[2], curr[3], curr[4]]
            
                # dim previous pixel value (only if min-pointer isn't on prev val)


                obj.update()

            # dim previous pixel value (only if min-pointer isn't on prev val)
            try:
                if n-1 != min_index:
                    prev = obj.stripState[n-1]
                    obj.stripState[n-1] = [prev[0], default_brightness, prev[2], prev[3], prev[4]]
            except:
                obj.stripState[n-1] = [min[0], default_brightness, min[2], min[3], min[4]]


        # swap values
        obj.stripState[i] = [min[0], default_brightness, min[2], min[3], min[4]]
        obj.stripState[min_index] = [mem[0], default_brightness, mem[2], mem[3], mem[4]]
        
        # update strip state
        obj.update()


