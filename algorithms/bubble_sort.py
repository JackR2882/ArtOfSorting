#basic implementation of bubble sort:
unsorted = True
#unsorted = False

def sort(obj):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(1, len(obj.stripState)):
            currVal = obj.stripState[i]
            prevVal = obj.stripState[i-1]
            obj.stripState[i] = [0,255,255,255,255]
            obj.update()

            if currVal < prevVal:
                #swap values
                obj.stripState[i] = prevVal
                obj.stripState[i-1] = currVal
                unsorted = True
            else:
                obj.stripState[i] = currVal            
            obj.update()
    print("Sorted!")