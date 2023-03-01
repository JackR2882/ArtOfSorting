# basic implementation of shell sort:



# variation on insertion sort / bubble sort
# define i as interval pair off with distance as interval, e.g...

# x1, x2, x3, x4, x5, x6, x7, x8

# x1              x5
#     x2              x6
#         x3              x7
#             x4              x8

# then swap pairs into order, e.g...
# swap x5 and x1 if x5 < x1, etc...

# repeat and reduce interval

# prevents items from having to be inserted to distant position


# inspired by the following implemntation: https://www.tutorialspoint.com/data_structures_algorithms/shell_sort_algorithm.htm


def sort(obj, audioBuff):

    default_b = obj.stripState[0][1]

    #i = int(len(obj.stripState)/2)
    #i = 1

    arr  = obj.stripState
        
    #while i < len(arr):

        #print(i)

    #    for n in range(0, len(arr)-i):

    #        obj.highlight(n, n+1, default_b)
    #        obj.highlight(n+i, n+i+1, default_b, stack=True, val=5)

    #        if arr[n] > arr[n+i]:
    #            arr[n], arr[n+i] = arr[n+i], arr[n]
    #        obj.update()
        
    #    i = int(i/2)
    #    i = (3*i) + 1

    #def shell(arr):
    
    interval = int(len(arr)/2)

    while interval > 0:

        for i in range(interval, len(arr)):

            obj.highlight(i, i+1, default_b) # highlight current item

            temp = arr[i] # store current item

            n = i # value to look back by

            # insertion sort backwards from current item in steps of size = interval
            while n >= interval and arr[n - interval] > temp:
                obj.highlight(n, n+1, default_b)
                obj.highlight(n-interval, n-interval+1, default_b, stack=True, val=5)
                arr[n] = arr[n - interval]
                n = n - interval
                obj.update()
            
            arr[n] = temp # insert current item into correct place

        interval = int(interval/2) # update interval
    
    # reset brightness:
    obj.highlight(0,0, default_b)