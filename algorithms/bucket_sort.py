# basic implementation of bucket sort

import math
import time

def sort(obj):

    #compareSD = obj.compareSD

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

    # divide the array into 5 buckets:
    bucket_1, bucket_2, bucket_3, bucket_4, bucket_5 = [], [], [], [], []

    for i in range(0, len(arr)):

        if arr[i][0] < bucket_range*1:
            # insert into bucket_1
            bucket_1.append(arr[i])
            bucket_1[-1][1] += 10
        elif arr[i][0] < bucket_range*2:
            # insert into bucket 2
            bucket_2.append(arr[i])
            bucket_2[-1][1] += 2
        elif arr[i][0] < bucket_range*3:
            # insert into bucket 3
            bucket_3.append(arr[i])
            bucket_3[-1][1] += 10
        elif arr[i][0] < bucket_range*4:
            # insert into bucket 2
            bucket_4.append(arr[i])
            bucket_4[-1][1] += 2
        else:
            # insert into bucket 2
            bucket_5.append(arr[i])
            bucket_5[-1][1] += 10
        
        time.sleep(obj.compareSD + obj.swapSD) # appending so modifying arr

        obj.stripState[0:i+1], obj.stripState[i:]= bucket_1 + bucket_2 + bucket_3 + bucket_4 + bucket_5, arr[i:]
        
        obj.update()
        obj.update()
        obj.update()

        buckets = [bucket_1, bucket_2, bucket_3, bucket_4, bucket_5]



    # now just need to sort buckets - can just do any basic sort e.g. insertion sort
    for i in range(0, num_buckets):

        arr_unsorted = buckets[i]

        sorted = i*bucket_range+1
        for x in range(i*bucket_range, i*bucket_range+len(arr_unsorted)-1):
        
            for n in reversed(range(i*bucket_range,sorted)):
                
                obj.stripState[n+1][1] += 10
                obj.stripState[n][1] += 10

                if not obj.compareAndSwapPixel(n+1, n):
                    obj.stripState[n+1][1] -= 10
                    obj.stripState[n][1] -= 10
                    break

                obj.update()
                obj.update()
                obj.update()

                obj.stripState[n+1][1] -= 10
                obj.stripState[n][1] -= 10
                

            # revert to default brightness:
            for n in range(0, (i)*bucket_range):
                obj.stripState[n][1] = default_b
            obj.update()
            obj.update() 
            obj.update()
            sorted += 1

    # remove any highlighting
    obj.highlight(0,0,default_b)