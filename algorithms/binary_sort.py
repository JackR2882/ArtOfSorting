#basic implmentation of binary sort:

#essentially the same as insertion sort, however a binary search is used to find the correct index for insertion

import time

def binary_search(val, obj, audioObj, start_i, end_i, default_b):

    time.sleep(obj.compareSD)

    audioObj.update(val[0])

    # highlight current section of arr
    # can switch between stacking and non-stacking brightness change by enabling / unenabling the flag
    obj.highlight(start_i, end_i, default_b)
    obj.update()
    obj.update()

    arr = obj.stripState

    # get mid index from between start_i and end_i
    i = start_i + int((end_i-start_i)/2)

    # if search area is too small
    if (end_i == start_i) or (i == start_i):
        time.sleep(obj.compareSD)
        if arr[i] < val:
            time.sleep(obj.compareSD)
            i += 1
        if end_i > start_i and arr[end_i] < val:
            time.sleep(obj.compareSD)
            i += 1
    # greater than, so recurse to right
    elif val > arr[i]:
        time.sleep(obj.compareSD)
        audioObj.update(arr[i][0])
        # recurse to right of val
        i = binary_search(val, obj, audioObj, i+1, end_i, default_b)
    # less than, so recurse to left
    elif val < arr[i]:
        time.sleep(obj.compareSD)
        audioObj.update(arr[i][0])
        # recurse to left of val
        i = binary_search(val, obj, audioObj, start_i, i-1, default_b)

    return(i)



def sort(obj, audioObj):

    swapSD = obj.swapSD

    sorted = 1

    default_b = obj.stripState[0][1]

    for i in range(1, len(obj.stripState)):

        val = obj.stripState[i].copy()
        audioObj.update(val[0])

        # highlight pixel to be inserted
        obj.stripState[i][1] += 5
        obj.update()

        index = binary_search(val, obj, audioObj, 0, sorted, default_b) # perform binary search to find where to insert item

        obj.highlight(0,0,default_b)

        time.sleep(swapSD*(sorted-index))

        # insert at index (need to shift rest of arr)
        obj.stripState[index:(sorted+1)] = [val] + obj.stripState[index:sorted]
        obj.update()

        sorted += 1