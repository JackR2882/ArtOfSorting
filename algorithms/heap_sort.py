# inspired by the following resources:
#  - https://iq.opengenus.org/create-heap-from-array/
#  - https://www.geeksforgeeks.org/heap-sort/

# basic implmentation of heap sort

import math
import time

def heapify(arr, n, obj, audioObj, default_b):
	
	parent = n
	audioObj.update(obj.stripState[n][0])
    
	child_left = 2*parent+1
	child_right = 2*parent+2

	obj.highlight(parent, parent+1, default_b)

	# only highlight children if they exist
	if (child_right < len(arr)):
		#obj.highlight(parent, parent+1, default_b, stack=True, val=10)
		obj.highlight(child_left, child_right+1, default_b, stack=True, val=10)
		audioObj.update(obj.stripState[child_right][0])
	elif (child_left < len(arr)):
		obj.highlight(child_left, child_left+1, default_b, stack=True, val=10)
		audioObj.update(obj.stripState[child_left][0])

	# compare with children
	if (child_left < len(arr)) and (arr[child_left] < arr[parent]):
		# swap left child and parent
		arr[child_left], arr[parent] = arr[parent], arr[child_left]
		arr = heapify(arr, child_left, obj, audioObj, default_b)
		time.sleep(obj.swapSD+obj.recursionSD)
	if (child_right < len(arr)) and (arr[child_right] < arr[parent]):
	    # swap right child and parent
		arr[child_right], arr[parent] = arr[parent], arr[child_right]
		arr = heapify(arr, child_right, obj, audioObj, default_b)
		time.sleep(obj.swapSD+obj.recursionSD)

	time.sleep(obj.compareSD*3) # to make up for previous comparions

	return(arr)



def heap(arr, obj, audioObj, default_b):
	for n in range(math.floor(len(arr)/2), 0, -1):
		arr = heapify(arr, n-1, obj, audioObj, default_b)
	return(arr)



def sort(obj, audioObj):

	default_b = obj.stripState[0][1]
	arr = obj.stripState

	# get arr into initial heap
	obj.stripState = heap(arr, obj, audioObj, default_b)

	# pull first item from heap, and append it to the end of the sorted arr:
	heaped_arr = obj.stripState
	sorted_arr = []
	i = 0

	#while False:
	while i <= len(obj.stripState)-1:

		sorted_arr.append(heaped_arr[0])
		audioObj.update(heaped_arr.pop(0)[0])

		# re-heap remaining unsorted arr
		heaped_arr = heap(heaped_arr, obj, audioObj, default_b)

		# left side of strip is for heaped arr, and right side to build up sorted arr
		obj.stripState = heaped_arr + sorted_arr
		obj.update()

		i += 1



	obj.stripState = sorted_arr