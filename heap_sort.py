import math


# sourced inspiration from:
# https://iq.opengenus.org/create-heap-from-array/
# and:
# https://www.geeksforgeeks.org/heap-sort/

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

#arr = [4,3,7,2,8,9,1]
#arr = [42,29,18,14,11,13,18,7,12,100]


#def insert_heap(temp_heap, item, i):

#	heap_update = temp_heap

	# parent = i/2
	# left_child = (2*index) + 1
	# right_child = (2*index) + 2

#	parent_i = math.floor(i/2)

#	if i/2 >= 1:
#		while i/2 >= 1:
#			parent_i = math.floor(i/2)-1
#			if item > heap_update[parent_i]:
#				heap_update[i] = heap_update[parent_i]
#				heap_update[parent_i] = item
#			i = parent_i
#	else:
#		heap_update[i] = item
#
#	print(heap_update)
#	return(heap_update)
#
#def heap(arr_in):
#
#	length = len(arr_in)
#	temp_heap = [0]*length
#	for i in range(0,length):
#		temp_heap = insert_heap(temp_heap, arr_in[i], i)
#
#	return temp_heap

arr = [4,3,7,2,8,9,1]
arr = [42,29,18,14,11,13,18,7,12,100]





# seems to work but is relatively slow
def heapify(arr_in, i):

	parent = math.floor(((i+1)/2)-1)

	#print("index: " + str(i), "parent: " + str(parent), "     arr_in[parent]: " + str(arr_in[parent]), "     arr_in[i]: " + str(arr_in[i]))
	if i >= 0:

		x = i
		# bubble up as far as possible
		while parent >= 0:
							
			if (arr_in[parent] < arr_in[x]):
				#print("x: " + str(x), "parent: " + str(parent), "     arr_in[parent]: " + str(arr_in[parent]), "     arr_in[x]: " + str(arr_in[x]))

				# swap (bubble up)
				arr_in[x], arr_in[parent] = arr_in[parent], arr_in[x]
				#arr_in = heapify(arr_in, i)

				arr_in = heapify(arr_in, x)

				x = parent

			parent = math.floor(((parent+1)/2)-1)

		# move to next item
		i -= 1
		arr_in = heapify(arr_in, i)
	
	return arr_in

print(heapify(arr, len(arr)-1))



# seems to work, but as above not sure about optimality
def heap_sort(arr_in):
	heaped_arr = heapify(arr_in, len(arr_in)-1)
	sorted_arr = [0]*len(heaped_arr)

	i = 0

	while i <= len(heaped_arr)-1:

		#print(i)
		sorted_arr[i] = heaped_arr[0]
		heaped_arr[0], heaped_arr[len(heaped_arr)-(1+i)] = heaped_arr[len(heaped_arr)-(1+i)], 0
		heaped_arr = heapify(heaped_arr, len(heaped_arr)-1)

		i += 1	
		#print(heaped_arr)

	return sorted_arr

print(heap_sort(arr))






