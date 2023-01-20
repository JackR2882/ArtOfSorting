# this version uses partitioning to allow an in place method to be used (also reduces the space complexity of the algorithm)

import math
import random

arr = [1,4,6,2,99,90,8,60,40,73]
arr = [80, 97, 60, 24, 38, 10, 57, 13, 69, 84, 64, 89, 32, 90,
       19, 36, 27, 44, 43, 2, 56, 67, 83, 51, 25, 95, 45, 8, 14,
       96, 46, 91, 63, 82, 59, 4, 54, 26, 70, 76, 37, 20, 55, 74,
       77, 88, 3, 9, 28, 94, 48, 62, 40, 79, 85, 35, 81, 23, 98,
       6, 29, 52, 41, 50, 87, 99, 78, 22, 93, 21, 72, 58, 42, 33,
       49, 73, 75, 5, 86, 66, 47, 11, 16, 12, 30, 17, 7, 68, 92, 71,
       15, 53, 18, 34, 65, 61, 31, 1, 100]

#arr = [1,3,9,8,2,7,5]


# seems to be working
def quicksort(arr_in, start_index, end_index):

    if len(arr_in) > 1:

        #pivot = math.floor(len(arr_in)/2)
        pivot = start_index + random.randint(0, end_index - start_index)
        #pivot = 6
        pivot_val = arr_in[pivot]

        l_part = start_index      # stores left partition

        # shift indexes into the right position:
        for i in range(start_index, end_index+1):
            if arr_in[i] < pivot_val:
                # insert into left partition
                arr_in[i], arr_in[l_part] = arr_in[l_part], arr_in[i]
                l_part += 1

        # shift pivot into the correct position:
        pivot = arr_in.index(pivot_val) # find new location of pivot
        while arr_in[pivot] < arr_in[pivot-1] and pivot != start_index:
            arr_in[pivot], arr_in[pivot-1] = arr_in[pivot-1], arr_in[pivot]
            pivot -= 1

        # recurse:
        if pivot != start_index:
            arr_in = quicksort(arr_in, start_index, pivot-1)
        if pivot != end_index:
            arr_in = quicksort(arr_in, pivot+1, end_index)

        return(arr_in)
    
    else:

        return arr_in
    
#print(arr)
print(quicksort(arr, 0, len(arr)-1))

