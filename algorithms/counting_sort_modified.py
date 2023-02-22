# modified implmentation of counting sort - for use as a subroutine in radix sort, so includes the ability to specify a 
# 'granularity' with which to sort by
# the following resource was used in the writing of this function: https://www.javatpoint.com/counting-sort

import math


def sort(obj, off):


    arr = obj.stripState.copy()


    # count the number of occurences of a given item within an input array
    def count(arr, item):
        counter = 0
        for i in range(0, len(arr)):
            if int(math.floor(arr[i][0]/off)) == item:
                counter += 1
        return counter


    # find the maximum value item in array:
    max_i = 0
    for i in range(1, len(arr)):
        if math.floor(arr[max_i][0]/off) < math.floor(arr[i][0]/off): # (first item in ret arr is ID value)
            max_i = i
            

    # initialize arr of length max + 1
    new_arr = [0]*(int(arr[max_i][0]/off)+1)


    # work out frequencies (count items)
    # raw count:
    for i in range(0, len(new_arr)):
        new_arr[i] = count(arr, i)

    #print("raw count: " + str(new_arr))

    # work out cumulative frequencies
    # cumulative-count:
    acc = 0
    for i in range(0, len(new_arr)):
        acc += new_arr[i]
        new_arr[i] = acc

    #print("cum count: " + str(new_arr))
    
    # revert strip state back to initial state
    sorted_arr = obj.stripState

    # sort items:
    for i in range(0, len(arr)):
        offset = math.floor(arr[i][0]/off)
        index = new_arr[offset]-1 # get index of item as corresponding item from cumulative freq array
        new_arr[offset] -= 1

        sorted_arr[index] = arr[i]
        obj.update()
        obj.update()
        obj.update()


