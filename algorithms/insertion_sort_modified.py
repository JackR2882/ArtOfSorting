# modified implmentation of insertion sort:
# for use in tim-sort
# only operates on a slice of the whole array, starting at start and ending at end

def sort(obj, audioObj, start, end):

    #default_b = obj.stripState[0][1]
    sorted = start+1

    for i in range(start, end):

        audioObj.update(obj.stripState[i][0])

        for n in reversed(range(start,sorted)):

            audioObj.update(obj.stripState[n][0])
            #obj.highlight(n, n+2, default_b, stack=True, val=5)
            
            if not obj.compareAndSwapPixel(n+1, n):
                break

            obj.update()

        sorted += 1