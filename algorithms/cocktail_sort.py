# basic implementation of cocktail shaker sort:
# probably cleaner ways to do this, but can fix later

def sort(obj, audioBuff):

    unsorted = True
    forward = True   # switch between forward and backwards directions:
    
    sorted_r = 0     # optimisation as algoithm will always put largest item on the right (don't need to re-check this area each time)
    sorted_l = 0     # opposite of above   

    while unsorted:
        unsorted = False

        if forward:
            for i in range(sorted_l+1, (len(obj.stripState)-sorted_r), 1):
                audioBuff.append(obj.stripState[i][0])

                currVal = obj.stripState[i].copy()
                prevVal = obj.stripState[i-1].copy()
                obj.stripState[i][1] += 10
                obj.stripState[i-1][1] += 10
                #obj.stripState[i] = [0,255,255,255,255]
                #obj.stripState[i-1] = [0,255,255,255,255]
                obj.update()


                if currVal < prevVal:
                    #swap values
                    obj.stripState[i], obj.stripState[i-1] = prevVal, currVal
                    unsorted = True
                else:
                    obj.stripState[i], obj.stripState[i-1] = currVal, prevVal
            
            sorted_r += 1
            forward = not forward

        else:
            for i in range((len(obj.stripState)-sorted_r)-1, sorted_l-1, -1):
                audioBuff.append(obj.stripState[i][0])

                currVal = obj.stripState[i].copy()
                prevVal = obj.stripState[i+1].copy()
                obj.stripState[i][1] += 10
                obj.stripState[i+1][1] += 10
                #obj.stripState[i] = [0,255,255,255,255]
                #obj.stripState[i+1] = [0,255,255,255,255]
                obj.update()


                if currVal > prevVal:
                    #swap values
                    obj.stripState[i], obj.stripState[i+1] = prevVal, currVal
                    unsorted = True
                else:
                    obj.stripState[i], obj.stripState[i+1] = currVal, prevVal
            
            sorted_l += 1
            forward = not forward