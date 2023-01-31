# basic implementation of selection sort:
# has been modified to include an offset (for use in radix sort -> sort by hundreds, tens, ones, etc...)

def sort(obj, off):

    print("modified selection sort (sorting " + str(int(off)) + "'s)")

    for i in range(0, len(obj.stripState)-1):
        
        # keep track of current min
        min = obj.stripState[i]
        min_index = i
        
        # keep track of current anchor
        mem = obj.stripState[i]

        # set pointer
        obj.stripState[i] = [0,255,255,255,255]
        obj.update()

        for n in range(i+1, len(obj.stripState)):

            #if obj.stripState[min_index] > obj.stripState[n]:
            if int(min[0]/off) > int(obj.stripState[n][0]/off):
                # remove old pointer
                obj.stripState[min_index] = min

                # update min
                min = obj.stripState[n]
                min_index = n

                # add new pointer
                obj.stripState[n] = [0,255,255,255,255]
                obj.update()

        # swap values
        obj.stripState[i] = min
        obj.stripState[min_index] = mem
        obj.update()


