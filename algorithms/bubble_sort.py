# basic implementation of bubble sort:

def sort(obj, audioBuff):

    unsorted = True
    sorted = 0 # optimisation as algoithm will always put largest item on the right (don't need to re-check this area each time)

    while unsorted:
        unsorted = False

        for i in range(1, (len(obj.stripState)-sorted)):

            audioBuff.append(obj.stripState[i][0])

            currVal = obj.stripState[i].copy()
            prevVal = obj.stripState[i-1].copy()
            #obj.stripState[i] = [0,255,255,255,255]
            #obj.stripState[i-1] = [0,255,255,255,255]
            obj.stripState[i][1] += 10
            obj.stripState[i-1][1] += 10
            obj.update()

 
            obj.stripState[i], obj.stripState[i-1] = currVal, prevVal # reset brightness 
            
            if currVal < prevVal:
                # swap values
                obj.swapPixel(i,i-1)
                unsorted = True
            #else:
            #    # just reset brightness 
            #    obj.stripState[i], obj.stripState[i-1] = currVal, prevVal 
                

        sorted += 1