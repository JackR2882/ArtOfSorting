# basic implementation of bucket sort

import math
import time

def sort(obj):

    num_buckets = 5
    
    arr = obj.stripState
    obj.update()


    #arr = arr[0:20]
    #print(len(arr))

    max = arr[0][0]
    for i in range(1, len(arr)):
        if max < arr[i][0]:
            max = arr[i][0]
    
    max += 1

    #print(max)
    bucket_range = math.ceil(max / num_buckets)
    print(bucket_range)
    #print(bucket_range)

    # divide array into 5 buckets:        NEED TO THINK OF A WAY OF REPRESENTING THIS ON LED STRIP?

    obj.clear()

    buckets = [[]]*num_buckets
    for i in range(0, len(arr)):
        bucket_index = math.floor(arr[i][0]/bucket_range)

        # need to do this to work around issue with updating list nested in array
        temp_arr = buckets[bucket_index].copy()
        temp_arr.append(arr[i])
        buckets[bucket_index] = temp_arr


        obj.stripState = []
        #obj.stripState = obj.stripState + buckets[0] + buckets[1] + buckets[2] + buckets[3] + buckets[4] + buckets[5] + buckets[6] + buckets[7] + buckets[8] + buckets[9]
        
        for n in range (0, num_buckets):
            obj.stripState = obj.stripState + buckets[n]

        obj.update()
        time.sleep(0.1)


    # now just need to sort buckets - can just do basic sort - e.g. insertion sort
    for i in range(0, num_buckets):
        arr_unsorted = buckets[i]
        sorted = 1
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
    time.sleep(2.5)