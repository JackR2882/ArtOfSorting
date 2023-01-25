# basic implmentation of radix sort:

# use counting sort to sort array based on current digit

# need to work out maximum item in array to inform radix sort, then if item is for example 144: sort
# items first by their hundreth digit value, e.g. 144 == 1 and 95 == 0
# then do the same for the 10th digit value, etc... all the way down to zero