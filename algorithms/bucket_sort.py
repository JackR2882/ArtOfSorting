# basic implementation of bucket sort

import math
import time

def sort(obj):

    num_buckets = 5
    
    arr = obj.stripState
    obj.update()


    # get max item from arr to decide what bucket size to use
    max = arr[0][0]
    for i in range(1, len(arr)):
        if max < arr[i][0]:
            max = arr[i][0]    
    max += 1

    bucket_range = math.ceil(max / num_buckets)

    # divide array into 5 buckets:
    obj.clear()
    buckets = [[]]*num_buckets
    for i in range(0, len(arr)):
        bucket_index = math.floor(arr[i][0]/bucket_range)

        # need to do this to work around issue with updating list nested in array
        temp_arr = buckets[bucket_index].copy()
        temp_arr.append(arr[i])
        buckets[bucket_index] = temp_arr


        obj.stripState = []       
        for n in range (0, num_buckets):
            obj.stripState = obj.stripState + buckets[n]

        obj.update()
        time.sleep(0.1)


    # now just need to sort buckets - can just do any basic sort e.g. insertion sort
    for i in range(0, num_buckets):
        arr_unsorted = buckets[i]

        for x in range(1, len(arr_unsorted)):
            curr_pos = x
            # insert into right position (insertion sort)
            while arr_unsorted[curr_pos] < arr_unsorted[curr_pos-1] and curr_pos > 0:
                arr_unsorted[curr_pos], arr_unsorted[curr_pos-1] = arr_unsorted[curr_pos-1], arr_unsorted[curr_pos]
                curr_pos -= 1


            buckets[i] = arr_unsorted
            obj.stripState = []        
            for n in range (0, num_buckets):
                obj.stripState = obj.stripState + buckets[n]

            obj.update()
            time.sleep(0.1)


    obj.clear()