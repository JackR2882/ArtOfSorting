# modified version of merge sort -> works on a copy of array, and keeps track of current
# section (run) of array being worked on; meaning that as runs are merged, the values in
# array object can also be updated, thus LED strip mirrors sorting algorithm

import time

def sort(obj, audioObj):

    swapSD = obj.swapSD = 0.001 # JUST USING RAW TIME AT THE MOMENT, WILL EXPERIMENT WITH LOOPING LATER
    compareSD = obj.compareSD = 0.001
    recursionSD = obj.recursionSD = 0.001

    # get starting brightness to act as anchor - so brightness can always be reset to orignial value
    default_b = obj.stripState[0][1]

    # get copy of array object to run merge sort on
    arr = obj.stripState.copy()

    # pointers for current slice of array
    start = 0
    end = len(arr)-1

    # merge sort modified to take 3 arguments:
    #   -> arr = array to be sorted
    #   -> start = pointer for start of current slice of array
    #   -> end = pointer for end of current slice of array
    def mergeSort(arr, start, end):

        time.sleep(recursionSD)

        # split array into two 
        mid = (int) (len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        # more than two elements in array so need to recurse on each sub array
        if len(arr)>2:

            # recurse
            l = mergeSort(left,start,start+mid-1)
            r = mergeSort(right,start+mid,end)

            #highlight after recurison to show merge
            obj.highlight(start, end+1, default_b)

            # pointers for merging
            lcount = 0
            rcount = 0

            # merge:
            for i in range(0,len(arr)):
                if lcount >= mid:
                    arr[i] = r[rcount]            
                    obj.stripState[start+i] = r[rcount] # also need to update LED strip
                    obj.update()
                    rcount += 1
                elif rcount >= len(arr)-mid:
                    arr[i] = l[lcount]
                    obj.stripState[start+i] = l[lcount] # also need to update LED strip
                    obj.update()
                    lcount += 1
                elif l[lcount] < r[rcount]:
                    arr[i] = l[lcount]
                    obj.stripState[start+i] = l[lcount] # also need to update LED strip
                    obj.update()
                    lcount += 1
                else:
                    arr[i] = r[rcount]
                    obj.stripState[start+i] = r[rcount] # also need to update LED strip
                    obj.update()
                    rcount += 1
                
                audioObj.update(obj.stripState[start+i][0])

                
                time.sleep(compareSD + swapSD)

            # remove highlight after merge
            obj.highlight(0,0,default_b)

            # pass merged array up a level                    
            return(arr)

        # only two elements in array so can simply order them and return
        elif len(arr) == 2:
            time.sleep(compareSD)
            if left[0] < right[0]:
                audioObj.update(left[0][0])
                audioObj.update(right[0][0])
                return([left[0], right[0]])
            else:
                audioObj.update(right[0][0])
                audioObj.update(left[0][0])
                return([right[0], left[0]])
        # only one element in array so just return (reached base layer of recursion)
        else:
            return(arr)
    

    # perform merge sort:
    mergeSort(arr, start, end)