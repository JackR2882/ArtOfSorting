# modified implmentation of insertion sort:
# for use in tim-sort
# only operates on a slice of the whole array, starting at start and ending at end

def sort(obj, audioBuff, start, end):

    default_b = obj.stripState[0][1]

    sorted = start+1
    for i in range(start, end):
        audioBuff.append(obj.stripState[i][0])
        for n in reversed(range(start,sorted)):
            #obj.highlight(n, n+2, default_b)
            
            if not obj.compareAndSwapPixel(n+1, n):
                break

            obj.update()
            #if obj.stripState[n] > obj.stripState[n+1]:
            #    audioBuff.append(obj.stripState[i][0])

            #    mem = obj.stripState[n+1]
            #    obj.stripState[n+1] = [mem[0],255,mem[2],mem[3],mem[4]]                
                #obj.stripState[n+1] = [0,255,255,255,255]
            #    obj.update()
            #    obj.stripState[n+1] = obj.stripState[n]
            #    obj.stripState[n] = mem
                #obj.update()
            #else:
            #    break
            #obj.update()
        sorted += 1
        #obj.update()