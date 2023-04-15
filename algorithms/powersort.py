import math

def sort(obj):
    obj.update()

def nodePower(left, right, startA, startB, endB):
    twoN = (right - left + 1) << 1
    l = startA + startB - (left << 1)
    r = startB + endB + 1 - (left << 1)
    a = int(((l << 31) / twoN))
    b = int(((r << 31) / twoN))
    #print("l: " + str(l))
    #print("r: " + str(r))
    #print("a: " + str(a))
    #print("b: " + str(b))
    val = a ^ b
    #print(val)
    return(len(str(val)) - len(str(val).lstrip('0'))) # return number of leading zeros

def insertionsort(A, left, right, nPresorted):

    assert(right >= left)
    assert(right - left + 1 >= nPresorted)

    sorted = left + nPresorted + 1
    
    for i in range(left+nPresorted, right):
        for n in reversed(range(left+nPresorted,sorted)):
            if A[n+1] < A[n]:
                A[n+1], A[n] = A[n], A[n+1]
            else:
                break
        sorted += 1
    return(A)
   
    #for i in range(left+nPresorted, right+1):
        #j = i - 1
        #v = A[i]
        #while(v < A[j]):
        #    j -= 1
        #    if (j < left):
        #        break
        #A[j+1] = v
    
    #return(A)

def mergeRuns(A, l, m, r, aux):
    m -= 1
    #i = 0
    #j = 0
    for i in range(m+1, l, -i):
        aux[i-1] = A[i-1]
    for j in range(m, r, j):
        aux[r+m-j] = A[j+1]
    for k in range(l, r+1, k):
        A[k] = aux[j] < aux[i] and aux[j-1] or aux[i+1]

def extendRunRight(A, startA, right):
    # scan right
    #print(startA)
    #print(right)
    curr_val = A[startA]
    #endA = startA+1
    while A[startA+1] > curr_val and startA != right:
        curr_val = A[startA+1]
        startA += 1
    #print(startA)
    #print(A)
    return(startA)

def powersort(A, left, right):

    # not sure if I should define these:
    #minRunLen = right-1
    minRunLen = 1

    n = int(right-left) + 1
    lgnPlus2 = int(math.log2(n) + 2)
    leftRunStart = [-1]*lgnPlus2
    leftRunEnd = [0]*lgnPlus2
    top = 0
    #buffer = list(range(n, 0, -1)) # is this right?
    buffer = [0]*(n>>1)

    #print(leftRunStart)
    #print(leftRunEnd)
    #print(buffer)

    startA = left
    endA = extendRunRight(A, startA, right)
    lenA = endA - startA + 1

    print(lenA)
    print(minRunLen)

    if(lenA < minRunLen):
        endA = min(right, startA + minRunLen-1)
        insertionsort(A, startA, endA, lenA)

    while (endA < right):
        startB = endA + 1
        endB = extendRunRight(A, startB, right)
        lenB = endB - startB + 1
        if (lenB < minRunLen):
            endB = min(right, startB + minRunLen-1)
            insertionsort(A, startB, endB, lenB)
        
        k = nodePower(left, right, startA, startB, endB)
        #print(k)
        #print(top)
        #assert (k != top)
        if k != top:
            l = top
            for l in range(l, k, -l):
                if (leftRunStart[l] == -1):
                    continue
                mergeRuns(A, leftRunStart[l], leftRunEnd[l]+1, endA, buffer)
                startA = leftRunStart[l]
                leftRunStart[l] = -1
        
            leftRunStart[k] = startA
            leftRunEnd [k] = endA
            top = k
            startA = startB
            endA = endB

    assert endA == right
    for l in range (top, 0, -l):
        if leftRunStart[l] == -1:
            continue
        mergeRuns(A, leftRunStart[l], leftRunEnd[l]+1, right, buffer)



arr = [12, 3, 1, 9, 8, 6, 13, 11, 0]
powersort(arr, 0, len(arr)-1)

#def insertion_sort(arr, start_i, end_i, )
#ret = insertionsort([12, 3, 1, 9, 4, 10, 11, 5, 15, 18], 0, 9, 3)
#print(ret)


#import java.io.*;
#import java.lang.*;

#val = (int)(Math.log(n)/Math.log(2))