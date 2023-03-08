#basic implmentation of insertion sort:

def sort(obj, audioBuff):

    default_b = obj.stripState[0][1]

    sorted = 1
    for i in range(0, len(obj.stripState)-1):
        audioBuff.append(obj.stripState[i][0])
        for n in reversed(range(0,sorted)):

            obj.highlight(n, n+2, default_b)

            if not obj.compareAndSwapPixel(n, n+1):
                break

            obj.update()
#            if obj.stripState[n] > obj.stripState[n+1]:
#                audioBuff.append(obj.stripState[i][0])

#                mem = obj.stripState[n+1]
#                obj.stripState[n+1] = [mem[0],255,mem[2],mem[3],mem[4]]                
                #obj.stripState[n+1] = [0,255,255,255,255]
#                obj.update()
#                obj.stripState[n+1] = obj.stripState[n]
#                obj.stripState[n] = mem
                #obj.update()
#            else:
#                break
            #obj.update()
        sorted += 1
        #obj.update()