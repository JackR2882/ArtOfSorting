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


# seems to be working
def quicksort(arr_in):

    if len(arr_in) > 1:

        pivot = math.floor(len(arr_in)/2)
        pivot = random.randint(0, len(arr_in)-1)

        l = []      # items less than pivot
        g = []      # items greater than pivot
        e = []      # items equal to pivot

        #print(pivot)
        #print(len(arr_in))

        for i in range (0, len(arr_in)): # split array into items, less than, greater than, and equal to the pivot

            if arr_in[i] < arr_in[pivot]:
                l.append(arr_in[i])
                print("less than")
            
            if arr_in[i] >= arr_in[pivot]:
                g.append(arr_in[i])
                print("greater than")

        #if len(l) > 0 and len(g) > 0:
        l = quicksort(l)
        g = quicksort(g)
        #else:
        #    if len(l) > 0:
        #        l = quicksort(l)
        #    else:
        #        g = quicksort(g)

        if len(e) > 0:
            l.append(e[0])
        for x in range(0, len(g)):
            l.append(g[x])

        return l

        #return (ret_l.extend(ret_g))
    
    else:
        return arr_in





        #print(pivot)
        #print(arr_in[:pivot])
        #print(arr_in[pivot:])
        #quicksort(arr_in[:pivot])
        #quicksort(arr_in[pivot:])

#print(len([]))

print(quicksort(arr))

