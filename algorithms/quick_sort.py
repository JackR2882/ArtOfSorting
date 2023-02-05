# basic implmentation of quick sort
# could do with highlighting the pivot

import random

import time

def highlight(obj, start, end, default_b):
    for i in range(0, len(obj.stripState)):
        if i in range(start, end):
            # increase brightness here
            obj.stripState[i][1] += 5
        else:
            # check brightness is default
            obj.stripState[i][1] = default_b
    
    obj.update()
    return(obj.stripState)



# start of code stup to integrate with system
def sort(obj):

    default_b = obj.stripState[0][1]

    arr = obj.stripState
    obj.update()

    def quicksort(arr_in, start_index, end_index):

        obj.stripState = highlight(obj, start_index, end_index, default_b)

        if len(arr_in) > 1:

            pivot = start_index + random.randint(0, end_index - start_index)
            pivot_val = arr_in[pivot]

            l_part = start_index      # stores left partition

            # shift indexes into the right position:
            for i in range(start_index, end_index+1):
                if arr_in[i] < pivot_val:
                    # insert into left partition
                    arr_in[i], arr_in[l_part] = arr_in[l_part], arr_in[i]
                    l_part += 1
                
                obj.update()

            # shift pivot into the correct position:
            pivot = arr_in.index(pivot_val) # find new location of pivot
            while arr_in[pivot] < arr_in[pivot-1] and pivot != start_index:
                arr_in[pivot], arr_in[pivot-1] = arr_in[pivot-1], arr_in[pivot]
                pivot -= 1
                
                obj.update()

            # recurse:
            if pivot != start_index:
                arr_in = quicksort(arr_in, start_index, pivot-1)
            if pivot != end_index:
                arr_in = quicksort(arr_in, pivot+1, end_index)

            return(arr_in)
    
        else:

            return arr_in

    quicksort(arr, 0, len(arr)-1)
    time.sleep(500)