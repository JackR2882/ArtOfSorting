#basic implmentation of insertion sort:

def sort(obj, audioObj):

    default_b = obj.stripState[0][1]
    sorted = 1

    for i in range(0, len(obj.stripState)-1):

        audioObj.update(obj.stripState[i][0])

        for n in reversed(range(0,sorted)):

            audioObj.update(obj.stripState[n][0])
            obj.highlight(n, n+2, default_b)

            if not obj.compareAndSwapPixel(n+1, n):
                break

            obj.update()

        sorted += 1