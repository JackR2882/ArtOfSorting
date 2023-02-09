# basic implmentation of tim sort

# split array into runs (size 32)
# then use insertion sort on those runs
# and merge runs using the merge from merge sort

from algorithms import insertion_sort_modified as insertion_sort
import math



def merge(obj, start_l, end_l, start_r, end_r):
    #print(obj)
    #print("------------------------------------")
    arr = obj.stripState

    l = end_l - start_l
    r = end_r - start_r

    lo = 0
    ro = 0

    print("l: " + str(l) + ", r: " + str(r))

    while lo < l and ro < r:
        if arr[start_l+lo] > arr[start_r+ro]:
            arr[start_l+lo+ro], arr[start_r] = arr[start_r+ro], arr[start_l+lo+ro]
            ro += 1
        else:
            arr[start_l+lo+ro], arr[start_l] = arr[start_l+lo], arr[start_r+lo+ro]
            lo += 1
        obj.update()



def sort(obj, audioBuff):
    #obj.update()

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
        insertion_sort.sort(obj, audioBuff, (i*run_size), ((i+1)*run_size)-1)
        i += 1

    # acount for last run which may be smaller
    #if i%2 == 0:
    #    obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
    obj.highlight((i*run_size), ((i+1)*run_size)-1, default_b)
    insertion_sort.sort(obj, audioBuff, (i*run_size), len(arr)-1)


    # now need to merge runs
    obj.highlight(((i-1)*run_size)-1, len(arr)-1, default_b)
    #print("end: " + str(len(arr)-1) + " start: " + str(((i-1)*run_size)-1))
    
    print(type(obj))
    merge(obj, ((i-1)*run_size)-1, ((i)*run_size)-1, ((i)*run_size), len(arr)-1)
    
    import time
    time.sleep(5)


    



#def merge(l_arr, r_arr):
#    merged = []

#    while (len(l_arr) and len(r_arr)) > 0:
#        if l_arr[0] > r_arr[0]:
#            merged.append(r_arr[0])
#            r_arr.pop(0)
#        else:
#            merged.append(l_arr[0]) 
#            l_arr.pop(0)
    
#    while len(r_arr) > 0:
#        merged.append(r_arr[0])
#        r_arr.pop(0)
#    while len(l_arr) > 0:
#        merged.append(l_arr[0])
#        l_arr.pop(0)

#    return(merged)



# merge runs
# merge last two runs, then merge merged run with third to last run, ... , then merge merged run with first run
#num_runs = len(runs) - 1
#merged = runs[num_runs]
#for i in range(num_runs-1, -1, -1):
#    merged = merge(runs[i], merged)
#print(merged)





arr = [69, 129, 137, 17, 6, 23, 43, 97, 130, 13, 119, 66, 51, 2, 115,
       24, 31, 141, 144, 143, 15, 82, 104, 11, 49, 16, 135, 93, 27, 5,
       78, 131, 52, 1, 21, 34, 48, 63, 45, 55, 40, 72, 106, 41, 128,
       111, 29, 74, 123, 73, 89, 14, 125, 122, 86, 95, 19, 100, 113, 4,
       3, 56, 127, 80, 42, 57, 105, 102, 53, 76, 87, 50, 140, 103, 54,
       68, 94, 35, 107, 20, 60, 39, 136, 134, 36, 126, 98, 10, 116, 114,
       84, 25, 132, 120, 9, 12, 85, 77, 30, 83, 58, 117, 65, 71, 79, 8,
       75, 112, 121, 90, 18, 33, 99, 108, 70, 47, 28, 101, 91, 37, 124,
       22, 46, 139, 92, 32, 96, 138, 62, 44, 109, 7, 38, 67, 88, 59, 110,
       26, 142, 61, 118, 64, 133, 81]


def split(arr):
    # set run size to 32:
    run_size = 32

    run_count = math.ceil(len(arr)/run_size) # work out number of runs needed

    runs = [] # empty arr to store runs

    # need to this, to stop nested arrays from being linked to each other
    for i in range(0, run_count):
        runs.append([])

    for i in range(0, len(arr)):
        #print(i%run_count)
        runs
        runs[int(i%run_count)].append(arr[i])

    return runs


#def insertion_sort(arr):

#    sorted = 0

#    for i in range(1, len(arr)):
#        n = sorted

#        while (arr[i] < arr[n]) and n >= 0:
#            arr[n], arr[i] = arr[i], arr[n]
#            i = n
#            n -= 1
#        sorted += 1

#    return(arr)


#def merge(l_arr, r_arr):
#    merged = []

#    while (len(l_arr) and len(r_arr)) > 0:
#        if l_arr[0] > r_arr[0]:
#            merged.append(r_arr[0])
#            r_arr.pop(0)
#        else:
#            merged.append(l_arr[0]) 
#            l_arr.pop(0)
    
#    while len(r_arr) > 0:
#        merged.append(r_arr[0])
#        r_arr.pop(0)
#    while len(l_arr) > 0:
#        merged.append(l_arr[0])
#        l_arr.pop(0)

#    return(merged)






# split into runs
#runs = split(arr)

# insertion sort runs
#for i in range(0, len(runs)):
#    runs[i] = insertion_sort(runs[i])
#    print(runs[i])

# merge runs
# merge last two runs, then merge merged run with third to last run, ... , then merge merged run with first run
#num_runs = len(runs) - 1
#merged = runs[num_runs]
#for i in range(num_runs-1, -1, -1):
#    merged = merge(runs[i], merged)
#print(merged)

