# semi working
# see below for exmplanation (can't handle arrays with repeated elements)

# inspiration sourced from: https://www.javatpoint.com/counting-sort

arr = [9,8,7,6,5,4,3,2,1]

arr = [80, 97, 60, 24, 38, 10, 57, 13, 69, 84, 64, 89, 32, 90,
       19, 36, 27, 44, 43, 2, 56, 67, 83, 51, 25, 95, 45, 8, 14,
       96, 46, 91, 63, 82, 59, 4, 54, 26, 70, 76, 37, 20, 55, 74,
       77, 88, 3, 9, 28, 94, 48, 62, 40, 79, 85, 35, 81, 23, 98,
       6, 29, 52, 41, 50, 87, 99, 78, 22, 93, 21, 72, 58, 42, 33,
       49, 73, 75, 5, 86, 66, 47, 11, 16, 12, 30, 17, 7, 68, 92, 71,
       15, 53, 18, 34, 65, 61, 31, 1, 100]

# can't handle arrays with repeated elements
#arr = [1,4,1,2,7,5,2]

#print(arr)



def count(arr, item):
    counter = 0
    for i in range(0, len(arr)):
        if arr[i] == item:
            counter += 1

    return counter



# find max item in array:
max_i = 0
for i in range(1, len(arr)):
    if arr[max_i] < arr[i]:
        max_i = i




# init arr of length max + 1
#print(arr[max_i])
new_arr = [0]*(arr[max_i]+1)


for i in range(0, len(new_arr)):
    new_arr[i] = count(arr, i)

print(new_arr)

# cumulative-count:
acc = 0
for i in range(0, len(new_arr)):
    acc += new_arr[i]
    new_arr[i] = acc


print(new_arr)

sorted_arr = arr.copy()

for i in range(0, len(arr)):
    index = new_arr[arr[i]]-1
    print(index)
    sorted_arr[index] = arr[i]

print(arr)
print(sorted_arr)

#print(len(arr))
#print(len(new_arr))


