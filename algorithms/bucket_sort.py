#  https://www.cs.usfca.edu/~galles/visualization/BucketSort.html <- should it be looking more like this?

# basic implementation of bucket sort

import math
import time

def sort(obj):

    default_b = obj.stripState[0][1]

    num_buckets = 5
    
    arr = obj.stripState.copy()
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
        if bucket_index%2 == 0:
            temp_arr.append([arr[i][0],arr[i][1]+10,arr[i][2],arr[i][3],arr[i][4]])
        else:
            temp_arr.append([arr[i][0],arr[i][1]+2,arr[i][2],arr[i][3],arr[i][4]])
        buckets[bucket_index] = temp_arr

    obj.stripState = [] 
    for n in range (0, num_buckets):
        obj.stripState = obj.stripState + buckets[n]
    obj.update()


    # now just need to sort buckets - can just do any basic sort e.g. insertion sort
    for i in range(0, num_buckets):

        arr_unsorted = buckets[i]

        sorted = 1
        for x in range(0, len(arr_unsorted)-1):
        #audioBuff.append(obj.stripState[i][0])
            for n in reversed(range(0,sorted)):
                if arr_unsorted[n] > arr_unsorted[n+1]:
                    #audioBuff.append(obj.stripState[i][0])

                    mem = arr_unsorted[n+1].copy()
                    #arr_unsorted[n+1] = [mem[0],255,mem[2],mem[3],mem[4]] 
                    arr_unsorted[n+1][1] += 10

                    obj.stripState[i*bucket_range:(i+1)*bucket_range] = arr_unsorted
                    obj.update()

                    arr_unsorted[n+1] = arr_unsorted[n]
                    arr_unsorted[n] = mem

                    obj.stripState[i*bucket_range:(i+1)*bucket_range] = arr_unsorted
                    obj.update()
                else:
                    break

            # revert to default brightness:
            for n in range(0, (i)*bucket_range):
                obj.stripState[n][1] = default_b
            obj.update() 
                #obj.update()
            sorted += 1

    # remove any highlighting
    obj.highlight(0,0,default_b)