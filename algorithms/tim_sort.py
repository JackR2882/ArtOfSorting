# basic implmentation of tim sort

# split array into runs (size 32)
# then use insertion sort on those runs
# then merge runs using the merge from merge sort

# inspired by the following resource:
#   - https://www.geeksforgeeks.org/timsort/

from algorithms import insertion_sort_modified as insertion_sort
import math
import time


# try and find run size between max run size and 0 that will allow the arr to be equally divided into runs UNUSED
def calculate_run_size(max_run_size, length):
    run_size = max_run_size
    while max_run_size > 0:
        if length%(max_run_size) == 0:
            run_size = max_run_size
            break
        max_run_size -= 1
    return(run_size)



def merge(obj, audioObj, start_l, end_l, start_r, end_r):

    #swapSD = obj.swapSD
    #compareSD = obj.compareSD

    offset = start_l

    l_arr = obj.stripState[start_l:end_l+1]
    r_arr = obj.stripState[start_r:end_r+1]
    
    while(len(l_arr) and len(r_arr)) > 0:

        if l_arr[0] > r_arr[0]:
            obj.stripState[offset] = r_arr[0]
            r_arr.pop(0)
        else:
            obj.stripState[offset] = l_arr[0]
            l_arr.pop(0)
        
        audioObj.update(obj.stripState[offset][0])

        time.sleep(obj.compareSD + obj.swapSD)

        offset += 1
        obj.update()
        obj.update()
        obj.update()

    while len(r_arr) > 0:

        obj.stripState[offset] = r_arr[0]
        r_arr.pop(0)

        audioObj.update(obj.stripState[offset][0])

        time.sleep(obj.swapSD)

        offset += 1
        obj.update()
        obj.update()
        obj.update()

    while len(l_arr) > 0:

        obj.stripState[offset] = l_arr[0]
        l_arr.pop(0)

        audioObj.update(obj.stripState[offset][0])

        time.sleep(obj.swapSD)
        
        offset += 1
        obj.update()
        obj.update()
        obj.update()



def sort(obj, audioObj):

    default_b = obj.stripState[0][1]
    arr = obj.stripState

    # don't need to split arr into runs, can instead just use slices of arr
    # (runs still exist, just aren't represented)
    
    run_size = 32

    run_count = math.ceil(len(arr)/run_size)

    i = 0
    while i < run_count-1:
        #if i%2 == 0:
            #obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
        obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
        insertion_sort.sort(obj, audioObj, (i*run_size), ((i+1)*run_size)-1)
        i += 1


    # last sort, may be shorter than the rest
    obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
    insertion_sort.sort(obj, audioObj, (i*run_size), len(arr)-1)


    # now need to merge runs
    # | | | | | |     no merges
    # || | | | |      1st merge
    # || || | |       2nd merge
    # |||| | |        3rd merge
    # |||| ||         4th merge
    # ||||||          5th merge

    i = 0
    left_sorted = 0
    right_sorted = 0

    length = len(obj.stripState)

    while left_sorted < run_count:
        # if left_sorted and right_sorted are the same size (left_sorted == (right_sorted-left_sorted)):
        #      merge left and right sorted partitions
        # 
        # otherwise if right_sorted <= run_count:
        #      merge right sorted with whatever's to its right
        #  
        if (right_sorted < run_count) and ((left_sorted != (right_sorted-left_sorted)) or left_sorted == 0):
            inc = min(i+2, run_count)
            
            obj.highlight((i)*run_size, (inc*run_size)-1, default_b)
            
            merge(obj, audioObj, ((i)*run_size), ((i+1)*run_size)-1, ((i+1)*run_size), min((inc*run_size)-1, length))
            
            i = inc

            if left_sorted == 0:
                left_sorted = i
            else:
                right_sorted = i
        else:
            obj.highlight(0, (right_sorted*run_size)-1, default_b)
            merge(obj, audioObj, 0, (run_size*left_sorted)-1, (run_size*left_sorted), min((run_size*right_sorted)-1, length))
            left_sorted = right_sorted

    obj.highlight(0,0, default_b)