import math
# import time

# need to convert to use min heap rather than max heap,
# in order to sort min-max rather than max-min

# sourced inspiration from:
# https://iq.opengenus.org/create-heap-from-array/
# and:
# https://www.geeksforgeeks.org/heap-sort/

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify2(arr, n, obj, default_b):
	
	#parent = int((n/2)-1)
	parent = n

	obj.highlight(0,0,225) # clear previous higlighting
    
	child_left = 2*parent+1
	child_right = 2*parent+2

	obj.highlight(parent, parent+1, default_b, stack=True, val=10)
	obj.highlight(child_left, child_right+1, default_b, stack=True, val=10)
	obj.highlight(child_right, child_right+1, default_b, stack=True, val=10)
    
	# compare with children
	if (child_left < len(arr)) and (arr[child_left] > arr[parent]):
		# swap left child and parent
		arr[child_left], arr[parent] = arr[parent], arr[child_left]
		arr = heapify2(arr, n, obj, default_b)
	if (child_right < len(arr)) and (arr[child_right] > arr[parent]):
	    # swap right child and parent
		arr[child_right], arr[parent] = arr[parent], arr[child_right]
		arr = heapify2(arr, n, obj, default_b)
	#else:
		#n-=1
		#if n > 0:
		#	arr = heapify2(arr, n, obj, default_b)
		#if parent > 0:
		#	arr = heapify2(arr, parent, obj, default_b)

	return(arr)


def heap(arr, obj, default_b):
	for n in range(math.floor(len(arr)/2), 0, -1):
		arr = heapify2(arr, n-1, obj, default_b)
	return(arr)


def sort(obj):

	default_b = obj.stripState[0][1]

	arr = obj.stripState


	#for n in range(math.floor(len(arr)/2), 0, -1):
	#	obj.stripState = heapify2(arr, n-1, obj, default_b)
	#	obj.update()
	obj.stripState = heap(arr, obj, default_b)


	import time
	print("heaped: " + str(obj.stripState[0][0]))
	#print("heaped: " + str(obj.stripState))
	#time.sleep(500)
	# could be issues with direction of sorting -> min/max heap ?


	heaped_arr = obj.stripState
	sorted_arr = [[0,0,0,0,0]]*len(heaped_arr)

	i = 0

	while i <= len(heaped_arr)-1:

		sorted_arr[i] = heaped_arr[0]
		heaped_arr[0], heaped_arr[len(heaped_arr)-(1+i)] = heaped_arr[len(heaped_arr)-(1+i)], [0,0,0,0,0] #what is this doing?
		

		heap(heaped_arr, obj, default_b)
		heaped_arr = obj.stripState
		#heaped_arr = heapify2(heaped_arr, len(heaped_arr)-1, obj, default_b)

		#obj.stripState = sorted_arr
		obj.update()

		print("heaped: " + str(obj.stripState[0][0]))

		i += 1

	obj.stripState = sorted_arr
	print(sorted_arr)



# seems to work, but as above not sure about optimality
#def heap_sort_test(arr_in):
#	heaped_arr = heapify(arr_in, len(arr_in)-1)
#	sorted_arr = [0]*len(heaped_arr)

#	i = 0
#
#	while i <= len(heaped_arr)-1:

		#print(i)
#		sorted_arr[i] = heaped_arr[0]
#		heaped_arr[0], heaped_arr[len(heaped_arr)-(1+i)] = heaped_arr[len(heaped_arr)-(1+i)], 0
#		heaped_arr = heapify(heaped_arr, len(heaped_arr)-1)

#		i += 1

#	return sorted_arr







