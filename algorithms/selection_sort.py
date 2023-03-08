# basic implementation of insertion sort:

def sort(obj):

    default_b = obj.stripState[0][1]

    for i in range(0, len(obj.stripState)-1):

        # track curr min
        min_index = i
        min = obj.stripState[min_index]

        for n in range(i+1, len(obj.stripState)):

            
            #obj.highlight(n,n+1,default_b,stack=True,val=10)
            obj.stripState[n][1] += 10
            obj.update()

            min_index, _ = obj.comparePixel(min_index, n)
            
            obj.highlight(min_index, min_index+1, default_b)

        obj.swapPixel(i, min_index)

        obj.update()