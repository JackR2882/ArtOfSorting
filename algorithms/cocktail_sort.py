# basic implementation of cocktail shaker sort:
# probably cleaner ways to do this, but can fix later

def sort(obj, audioObj):

    default_b = obj.stripState[0][1]

    unsorted = True
    forward = True   # switch between forward and backwards directions:
    
    sorted_r = 0     # optimisation as algoithm will always put largest item on the right (don't need to re-check this area each time)
    sorted_l = 0     # opposite of above   

    while unsorted:
        unsorted = False

        if forward:
            for i in range(sorted_l+1, (len(obj.stripState)-sorted_r), 1):
                
                audioObj.update(obj.stripState[i][0])

                currVal = obj.stripState[i].copy()
                prevVal = obj.stripState[i-1].copy()
                obj.highlight(i-1,i+1,default_b)

                #audioObj.update(obj.stripState[i-1][0])

                if obj.compareAndSwapPixel(i,i-1):
                    unsorted = True
            
            sorted_r += 1
            forward = not forward

        else:
            for i in range((len(obj.stripState)-sorted_r)-1, sorted_l-1, -1):
                
                audioObj.update(obj.stripState[i][0])

                currVal = obj.stripState[i].copy()
                prevVal = obj.stripState[i+1].copy()
                obj.highlight(i,i+2,default_b)

                #audioObj.update(obj.stripState[i+1][0])

                if obj.compareAndSwapPixel(i+1, i):
                    unsorted = True
            
            sorted_l += 1
            forward = not forward

    obj.highlight(0,0,default_b)