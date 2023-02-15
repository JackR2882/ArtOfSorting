# basic implmentation of tim sort

# split array into runs (size 32)
# then use insertion sort on those runs
# and merge runs using the merge from merge sort

from algorithms import insertion_sort_modified as insertion_sort
import math


# try and find run size between max run size and 0 that will allow the arr to be equally divided into runs
def calculate_run_size(max_run_size, length):
    run_size = max_run_size
    while max_run_size > 0:
        if length%(max_run_size) == 0:
            run_size = max_run_size
            break
        max_run_size -= 1
    
    return(run_size)



def merge(obj, start_l, end_l, start_r, end_r):
    
    #print("start_l: " + str(start_l) + ", end_l: " + str(end_l))
    #print("start_r: " + str(start_r) + ", end_r: " + str(end_r))

    offset = start_l

    l_arr = obj.stripState[start_l:end_l+1]
    r_arr = obj.stripState[start_r:end_r]
    
    while(len(l_arr) and len(r_arr)) > 0:
        if l_arr[0] > r_arr[0]:
            obj.stripState[offset] = r_arr[0]

            r_arr.pop(0)
        else:
            obj.stripState[offset] = l_arr[0]

            l_arr.pop(0)
        offset += 1
        obj.update()

    while len(r_arr) > 0:
        obj.stripState[offset] = r_arr[0]
        r_arr.pop(0)
        offset += 1
        obj.update()

    while len(l_arr) > 0:
        obj.stripState[offset] = l_arr[0]
        l_arr.pop(0)
        offset += 1
        obj.update()



def sort(obj, audioBuff):

    default_b = obj.stripState[0][1]
    arr = obj.stripState

    # don't need to split arr into runs, can instead just use slices of arr
    # (runs still exist, just aren't represented)
    
    max_run_size = 32
    run_size = calculate_run_size(max_run_size, len(obj.stripState))

    run_count = math.ceil(len(arr)/run_size)

    i = 0
    while i < run_count-1:
        #if i%2 == 0:
            #obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
        obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
        insertion_sort.sort(obj, audioBuff, (i*run_size), ((i+1)*run_size)-1)
        i += 1

    # acount for last run which may be smaller
    #if i%2 == 0:
    #    obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
    obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
    insertion_sort.sort(obj, audioBuff, (i*run_size), len(arr)-1)


    # now need to merge runs
    # | | | | | |     no merges
    # || | | | |      1st merge
    # || || | |       2nd merge
    # |||| | |        3rd merge
    # |||| ||         4th merge
    # ||||||          5th merge
    while i > 0:
        obj.highlight(((i-1)*run_size), len(arr)-1, default_b)
        merge(obj, ((i-1)*run_size), ((i)*run_size)-1, ((i)*run_size), len(arr)-1)
        i -= 1