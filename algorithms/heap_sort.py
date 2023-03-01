import math

# need to convert to use min heap rather than max heap,
# in order to sort min-max rather than max-min

# sourced inspiration from:
# https://iq.opengenus.org/create-heap-from-array/
# and:
# https://www.geeksforgeeks.org/heap-sort/

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap



def heapify(arr, n, obj, default_b):
	
	parent = n

	obj.highlight(0,0,225) # clear previous higlighting
    
	child_left = 2*parent+1
	child_right = 2*parent+2

	obj.highlight(parent, parent+1, default_b, stack=True, val=10)
	obj.highlight(child_left, child_right+1, default_b, stack=True, val=10)

	# compare with children
	if (child_left < len(arr)) and (arr[child_left] < arr[parent]):
		# swap left child and parent
		arr[child_left], arr[parent] = arr[parent], arr[child_left]
		arr = heapify(arr, child_left, obj, default_b)
	if (child_right < len(arr)) and (arr[child_right] < arr[parent]):
	    # swap right child and parent
		arr[child_right], arr[parent] = arr[parent], arr[child_right]
		arr = heapify(arr, child_right, obj, default_b)

	return(arr)



def heap(arr, obj, default_b):
	for n in range(math.floor(len(arr)/2), 0, -1):
		arr = heapify(arr, n-1, obj, default_b)
	return(arr)



def sort(obj):

	default_b = obj.stripState[0][1]
	arr = obj.stripState

	# get arr into initial heap
	obj.stripState = heap(arr, obj, default_b)

	#print("heaped: " + str(obj.stripState[0][0]))

	# pull first item from heap, and append it to the end of the sorted arr:
	heaped_arr = obj.stripState
	sorted_arr = []
	i = 0

	#while False:
	while i <= len(obj.stripState)-1:

		sorted_arr.append(heaped_arr[0])
		heaped_arr.pop(0)

		# re-heap remaining unsorted arr
		heaped_arr = heap(heaped_arr, obj, default_b)

		# left side of strip is for heaped arr, and right side to build up sorted arr
		obj.stripState = heaped_arr + sorted_arr
		obj.update()

		i += 1



	obj.stripState = sorted_arr