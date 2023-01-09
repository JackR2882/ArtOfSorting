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



# seems to work but is relatively slow
def heapify(arr_in, i):

	parent = math.floor(((i+1)/2)-1)

	if i >= 0:

		x = i
		# bubble up as far as possible
		while parent >= 0:			
			if (arr_in[parent] < arr_in[x]):

				# swap (bubble up)
				arr_in[x], arr_in[parent] = arr_in[parent], arr_in[x]

				arr_in = heapify(arr_in, x)

				x = parent

			parent = math.floor(((parent+1)/2)-1)

		# move to next item
		i -= 1
		arr_in = heapify(arr_in, i)
	
	return arr_in

def sort(obj):
	arr = obj.stripState

	obj.stripState = heapify(arr,len(arr)-1)
	obj.update()

	heaped_arr = obj.stripState
	sorted_arr = [[0,0,0,0,0]]*len(heaped_arr)

	i = 0

	while i <= len(heaped_arr)-1:

		sorted_arr[i] = heaped_arr[0]
		heaped_arr[0], heaped_arr[len(heaped_arr)-(1+i)] = heaped_arr[len(heaped_arr)-(1+i)], [0,0,0,0,0]
		heaped_arr = heapify(heaped_arr, len(heaped_arr)-1)

		obj.stripState = sorted_arr
		obj.update()

		i += 1

	return sorted_arr



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







