# basic implmentation of radix sort:

# use counting sort to sort array based on current digit

# need to work out maximum item in array to inform radix sort, then if item is for example 144: sort
# items first by their hundreth digit value, e.g. 144 == 1 and 95 == 0
# then do the same for the 10th digit value, etc... all the way down to zero


# woprking counting sort
# JUST NEED TO SWAP INSERTION SORT FOR COUNTING SORT


import math
import time
from algorithms import selection_sort_modified as selection_sort
from algorithms import counting_sort_modified as counting_sort



def sort(obj):
    arr = obj.stripState
    obj.update()

    max_i = 0
    for i in range(0, len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
    
    max_val = arr[max_i][0]

    size = int(math.log10(max_val))+1
    off = int(math.pow(10,size-1))

    def counting(arr_in, off):
        for i in range(0,len(arr_in)):
            x = i
            while x >= 1 and int(arr_in[x][0]/off) > int(arr_in[x-1][0]/off):
                arr_in[x], arr_in[x-1] = arr_in[x-1], arr_in[x]
                x -= 1
        obj.update()
        time.sleep(2)

    while off >= 1:
        #counting(arr, off)
        counting_sort.sort(obj, off)
        off = off/10
