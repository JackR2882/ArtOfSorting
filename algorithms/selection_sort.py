# basic implementation of insertion sort:

def sort(obj):

    default_brightness = obj.stripState[0][1]

    for i in range(0, len(obj.stripState)-1):
        
        # keep track of current min
        min = obj.stripState[i]
        min_index = i        
        # keep track of current anchor
        mem = obj.stripState[i]
        # set pointer for current element
        obj.stripState[i][1] += 15
        # update strip state
        #obj.update()

        # for each item in remaining arr:
        for n in range(i+1, len(obj.stripState)):
            
            # if current item is less than the current min value 
            if min > obj.stripState[n]:
                # remove old pointer
                min[1] = default_brightness
                obj.stripState[min_index] = min
                # update min
                min = obj.stripState[n]
                min_index = n
                # add new pointer
                obj.stripState[n][1] += 15
            else:
                # brighten current pixel value:
                obj.stripState[n][1]  += 15

            # dim previous pixel value (only if min-pointer isn't on prev val)
            try:
                if n-1 != min_index:
                    obj.stripState[n-1][1] = default_brightness
            except:
                min[1] = default_brightness
                obj.stripState[n-1] = min

            obj.update()


        # swap values
        min[1] = default_brightness
        mem[1] = default_brightness
        obj.stripState[i] = min
        obj.stripState[min_index] = mem
        
        # update strip state
        obj.update()