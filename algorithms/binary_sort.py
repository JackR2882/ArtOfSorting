#basic implmentation of binary sort:
#essentially the same as insertion sort, however a binary search is used to find the correct index for insertion

def binary_search(val, obj, start_i, end_i, default_b):

    # highlight current section of arr
    obj.highlight(start_i, end_i, default_b)

    #import time
    #time.sleep(0.1)


    arr = obj.stripState

    i = start_i + int((end_i-start_i)/2)
    #print("start: " + str(start_i) + ", end: " + str(end_i) + ", i: " + str(i) + ", val: " + str(val) + ", into: " + str(arr[start_i:end_i])) 

    if (end_i == start_i) or (i == start_i):
        if arr[i] < val:
            i += 1
        if end_i > start_i and arr[end_i] < val:
            i += 1
    elif val > arr[i]:
        # recurse to right of val
        i = binary_search(val, obj, i+1, end_i, default_b)
    elif val < arr[i]:
        # recurse to left of val
        i = binary_search(val, obj, start_i, i-1, default_b)

    return(i)

#def insert(arr, insertion_index, val):
  
#    new_arr = [0]*(len(arr)+1)

    #print("inserting, " + str(val) + " @: " + str(insertion_index))

#    new_arr[0:insertion_index] = arr[0:insertion_index]
#    new_arr[insertion_index] = val
#    new_arr[insertion_index+1:len(new_arr)] = arr[insertion_index:len(arr)]

#    return(new_arr)


def sort(obj, audioBuff):

    sorted = 1
    sorted_arr = obj.stripState[0:sorted]

    default_b = obj.stripState[0][1]

    for i in range(1, len(obj.stripState)-1):

        val = obj.stripState[i].copy()
        audioBuff.append(val[0])

        # highlight pixel to be inserted
        obj.stripState[i][1] += 5
        obj.update()

        index = binary_search(val, obj, 0, sorted, default_b) # perform binary search to find where to insert item
        #sorted_arr = insert(sorted_arr, index, val) # insert item into sorted arr at given index (need to shift anything to the right of including the index, right by one)

        # possible way of inserting -> keeps execution time in line with other algorithms but doesn't look the best
        prev = obj.stripState[index]
        obj.stripState[index] = val
        for n in range(index+1, sorted+1):
            obj.stripState[n], prev = prev, obj.stripState[n]
            obj.update()

        #obj.stripState[0:len(sorted_arr)] = sorted_arr # update arr

        #obj.update()

        sorted += 1