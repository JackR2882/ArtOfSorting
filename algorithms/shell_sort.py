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



# just a copy of insertion sort -> need to adapt
def sort(obj, audioBuff):

    default_b = obj.stripState[0][1]

    i = int(len(obj.stripState)/2)

    arr  = obj.stripState

    while i > 0:
        
        #print(i)

        for n in range(0, len(arr)-i):

            obj.highlight(n, n+1, default_b)
            obj.highlight(n+i, n+i+1, default_b, stack=True, val=5)

            if arr[n] > arr[n+i]:
                arr[n], arr[n+i] = arr[n+i], arr[n]
            obj.update()
        
        i -= 1