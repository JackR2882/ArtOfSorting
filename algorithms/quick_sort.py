# basic implmentation of quick sort
# uses a randomized pivot, or the leftmost item as a pivot

import random
import time

def sort(obj, audioObj, rand=True):  

    default_b = obj.stripState[0][1]

    arr = obj.stripState
    obj.update()

    def quicksort(arr_in, start_index, end_index):

        obj.stripState = obj.highlight(start_index, end_index, default_b)

        if len(arr_in) > 1:

            # choose between randomised or regular quicksort
            if rand:
                pivot = start_index + random.randint(0, end_index - start_index)
            else:
                pivot = start_index

            pivot_val = arr_in[pivot]

            audioObj.update(pivot_val[0])

            l_part = start_index      # stores left partition

            # shift indexes into the right position:
            for i in range(start_index, end_index+1):
                
                time.sleep(obj.compareSD)
                if arr_in[i] < pivot_val:
                    audioObj.update(arr_in[i][0])
                    # insert into left partition
                    obj.swapPixel(i, l_part)
                    l_part += 1
                
                obj.update()
                obj.update()

            # shift pivot into the correct position:
            pivot = arr_in.index(pivot_val) # find new location of pivot
            while arr_in[pivot] < arr_in[pivot-1] and pivot != start_index:
                audioObj.update(arr_in[pivot-1][0])
                time.sleep(obj.compareSD + obj.swapSD)
                arr_in[pivot], arr_in[pivot-1] = arr_in[pivot-1], arr_in[pivot]
                pivot -= 1
                
                obj.update()
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