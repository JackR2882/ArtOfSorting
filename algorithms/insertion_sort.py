import audio_controller_temp

#basic implmentation of insertion sort:
def sort(obj):

    audio = audio_controller_temp.AudioOut()

    sorted = 1
    for i in range(0, len(obj.stripState)-1):
        audio.out(obj.stripState[i][0])
        for n in reversed(range(0,sorted)):
            if obj.stripState[n] > obj.stripState[n+1]:
                audio.out(obj.stripState[n][0])
                mem = obj.stripState[n+1]
                obj.stripState[n+1] = [0,255,255,255,255]
                obj.update()
                obj.stripState[n+1] = obj.stripState[n]
                obj.stripState[n] = mem
                obj.update()
            else:
                break
        sorted += 1
        obj.update()

#arr = [3,2,5,9,6,1,8]
#sorted = 1

#for i in range(0,len(arr)-1):
#    for n in reversed(range(0,sorted)):
#        if arr[n] > arr[n+1]:
#            mem = arr[n]
#            arr[n] = arr[n+1]
#            arr[n+1] = mem
#        else:
#            break    
#    sorted+=1 #new item added to sorted arr

#print(arr)