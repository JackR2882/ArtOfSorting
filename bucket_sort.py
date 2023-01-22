import math
#import numpy as np

# basic implmentation of bucket sort -> it recurses on itself, that is, it splits the array into two buckets,
# then two more buckets, then two more buckets, until it cannot anymore

arr = [10,9,7,8,4,6,5,2,3,1,0]
bucket_arr = arr.copy()

#print(bucket_arr)

bucket_1 = [] # numbers less than equal to 2
bucket_2 = [] # numbers between 3 and 5 (inclusive)
bucket_3 = [] # numbers between 6 and 8 (inclusive)
bucket_4 = [] # numbers between 9 and 10 (inclusive)

def bucket_sort(arr_in):
    if len(arr_in) > 1:

        # split arr_in into two buckets and recurse:
        maximum = max(arr_in)
        minimum = min(arr_in)

        pivot = round(math.ceil(minimum + ((maximum - minimum)/2)))

        bucket_1 = [] # items upto  pivot
        bucket_2 = [] # items from pivot to the max value

        for i in range(0, len(arr_in)):
            if arr_in[i] < pivot:
                bucket_1.append(arr_in[i])
            else:
                bucket_2.append(arr_in[i])


        bs_1 = bucket_sort(bucket_1)
        bs_2 = bucket_sort(bucket_2)

        print(bs_1)
        print(bs_2)

        arr_out = bs_1
        for i in range(0, len(bs_1)):
            arr_out.append(bs_2[i])

        return(arr_out)
    
    else:
        return arr_in
        #print(arr_in)

#sorted = bucket_sort(arr)
#print(sorted)

#print("---------------------------------------------")
#print(round(0.6))

arr =  [62, 129, 43, 172, 76, 123, 121, 120, 82, 52, 18, 85, 80, 25, 118, 106, 9, 109, 137,
        81, 113, 72, 161, 151, 12, 31, 145, 110, 139, 166, 144, 177, 19, 95, 59, 186, 180,
        182, 14, 176, 138, 178, 94, 188, 74, 122, 132, 197, 154, 100, 158, 184, 174, 66, 36,
        79, 96, 63, 53, 35, 17, 65, 146, 90, 127, 6, 187, 102, 148, 173, 149, 93, 125, 30, 169,
        64, 155, 140, 135, 196, 185, 73, 112, 190, 54, 21, 141, 195, 164, 167, 171, 179, 142,
        24, 159, 133, 71, 77, 117, 20, 156, 37, 101, 75, 61, 47, 165, 143, 183, 98, 7, 5, 8,
        170, 28, 11, 58, 84, 67, 29, 39, 48, 22, 34, 189, 26, 33, 86, 131, 105, 13, 124, 114,
        152, 181, 116, 153, 46, 51, 32, 16, 10, 49, 136, 128, 107, 27, 68, 103, 115, 97, 56, 134,
        92, 175, 45, 119, 162, 41, 40, 2, 130, 126, 50, 194, 60, 89, 57, 147, 44, 111, 38, 200,
        99, 55, 23, 104, 157, 83, 70, 160, 150, 168, 198, 91, 78, 108, 4, 192, 193, 199, 1, 191,
        87, 42, 163, 3, 15, 88, 69]




def bucket_s(arr_in):

    # divide arr into 10 buckets:
    maximum = max(arr_in)
    step = round(maximum/10)

    t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9, t_10 = step*1, step*2, step*3, step*4, step*5, step*6, step*7, step*8, step*9, step*10 # declare threshold values for buckets
    b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_10 = [], [], [], [], [], [], [], [], [], [] # declare buckets

    # split into threshold values:
    for i in range(0, len(arr_in)):
    
        # could insert into the correct position here, to save having to do it later

        if arr_in[i] <= t_1:

            b_1.append(arr_in[i])
            for i in range(len(b_1)-1, -1, -1):
                if i != 0 and b_1[i] < b_1[i-1]:
                    b_1[i], b_1[i-1] = b_1[i-1], b_1[i]
                else:
                    break

        elif arr_in[i] <= t_2:

            b_2.append(arr_in[i])
            for i in range(len(b_2)-1, -1, -1):
                if i != 0 and b_2[i] < b_2[i-1]:
                    b_2[i], b_2[i-1] = b_2[i-1], b_2[i]
                else:
                    break

        elif arr_in[i] <= t_3:

            b_3.append(arr_in[i])
            for i in range(len(b_3)-1, -1, -1):
                if i != 0 and b_3[i] < b_3[i-1]:
                    b_3[i], b_3[i-1] = b_3[i-1], b_3[i]
                else:
                    break

        elif arr_in[i] <= t_4:

            b_4.append(arr_in[i])
            for i in range(len(b_4)-1, -1, -1):
                if i != 0 and b_4[i] < b_4[i-1]:
                    b_4[i], b_4[i-1] = b_4[i-1], b_4[i]
                else:
                    break

        elif arr_in[i] <= t_5:

            b_5.append(arr_in[i])
            for i in range(len(b_5)-1, -1, -1):
                if i != 0 and b_5[i] < b_5[i-1]:
                    b_5[i], b_5[i-1] = b_5[i-1], b_5[i]
                else:
                    break

        elif arr_in[i] <= t_6:

            b_6.append(arr_in[i])
            for i in range(len(b_6)-1, -1, -1):
                if i != 0 and b_6[i] < b_6[i-1]:
                    b_6[i], b_6[i-1] = b_6[i-1], b_6[i]
                else:
                    break

        elif arr_in[i] <= t_7:

            b_7.append(arr_in[i])
            for i in range(len(b_7)-1, -1, -1):
                if i != 0 and b_7[i] < b_7[i-1]:
                    b_7[i], b_7[i-1] = b_7[i-1], b_7[i]
                else:
                    break

        elif arr_in[i] <= t_8:

            b_8.append(arr_in[i])
            for i in range(len(b_8)-1, -1, -1):
                if i != 0 and b_8[i] < b_8[i-1]:
                    b_8[i], b_8[i-1] = b_8[i-1], b_8[i]
                else:
                    break

        elif arr_in[i] <= t_9:

            b_9.append(arr_in[i])
            for i in range(len(b_9)-1, -1, -1):
                if i != 0 and b_9[i] < b_9[i-1]:
                    b_9[i], b_9[i-1] = b_9[i-1], b_9[i]
                else:
                    break

        elif arr_in[i] <= t_10:

            b_10.append(arr_in[i])
            for i in range(len(b_10)-1, -1, -1):
                if i != 0 and b_10[i] < b_10[i-1]:
                    b_10[i], b_10[i-1] = b_10[i-1], b_10[i]
                else:
                    break

    #print(b_10)

    
    #ret_arr = b_1.append(b_2.append(b_3.append(b_4.append(b_5.append(b_6.append(b_7.append(b_8.append(b_9.append(b_10)))))))))
    #return_arr = b_1
    #b_9.append(b_10)
    #b_8.append(b_9)
    #b_7.append(b_8)
    #b_6.append(b_7)
    #b_5.append(b_6)
    #b_4.append(b_5)
    #b_3.append(b_4)
    #b_2.append(b_3)
    #b_1.append(b_2)

    #o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8, o_9 = len(b_1)-1, len(b_2)-1, len(b_3)-1, len(b_4)-1, len(b_5)-1, len(b_6)-1, len(b_7)-1, len(b_8)-1, len(b_9)-1 # define offsets

    return_arr = arr_in


    # move buckets back into main array, readhy to be returned
    for i in range(0,20):
        return_arr[i] = b_1[i]
        return_arr[i+(1*step)] = b_2[i]
        return_arr[i+(2*step)] = b_3[i]
        return_arr[i+(3*step)] = b_4[i]
        return_arr[i+(4*step)] = b_5[i]
        return_arr[i+(5*step)] = b_6[i]
        return_arr[i+(6*step)] = b_7[i]
        return_arr[i+(7*step)] = b_8[i]
        return_arr[i+(8*step)] = b_9[i]
        return_arr[i+(9*step)] = b_10[i]


        

    #return_arr = b_1
    #return_arr.flatten()
    

    #dreturn_arr.append(b_2.append(b_3.append(b_4.append(b_5.append(b_6.append(b_7.append(b_8.append(b_9.append(b_10)))))))))
    #ret_arr = np.concatenate(b_1, b_2)
    return return_arr


    #print(step)

    #print(arr_in)

print(bucket_s(arr))

