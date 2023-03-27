# basic implementation of bubble sort:

def sort(obj, audioObj):

    default_b = obj.stripState[0][1]

    unsorted = True
    sorted = 0 # optimisation as algoithm will always put largest item on the right (don't need to re-check this area each time)

    while unsorted:
        unsorted = False

        for i in range(1, (len(obj.stripState)-sorted)):

            audioObj.update(obj.stripState[i][0])

            currVal = obj.stripState[i].copy()
            prevVal = obj.stripState[i-1].copy()
            obj.highlight(i-1,i+1, default_b)
            #obj.stripState[i][1] += 10
            #obj.stripState[i-1][1] += 10
            obj.update()
 
            obj.stripState[i], obj.stripState[i-1] = currVal, prevVal # reset brightness

            if obj.compareAndSwapPixel(i,i-1):
                unsorted = True

        sorted += 1