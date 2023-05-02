# basic implmentation of radix sort:

# inspired by the following resource:
#   - https://www.programiz.com/dsa/radix-sort

import math
from algorithms import counting_sort_modified as counting_sort

# use counting sort to sort array based on current digit

# need to work out maximum item in array to inform radix sort, then if item is for example 144: sort
# items first by their hundreth digit value, e.g. 144 == 1 and 95 == 0
# then do the same for the 10th digit value, etc... all the way down to zero


def sort(obj, audioObj):

    arr = obj.stripState
    obj.update()

    max_i = 0
    for i in range(0, len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
    
    max_val = arr[max_i][0]

    size = int(math.log10(max_val))+1
    off = int(math.pow(10,size-1))

    while off >= 1:
        counting_sort.sort(obj, audioObj, off)
        off = off/10
