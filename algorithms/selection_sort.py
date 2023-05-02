# basic implementation of selection sort:

def sort(obj, audioObj):

    default_b = obj.stripState[0][1]

    for i in range(0, len(obj.stripState)-1):

        audioObj.update(obj.stripState[i][0])

        # track curr min
        min_index = i

        for n in range(i+1, len(obj.stripState)):

            audioObj.update(obj.stripState[n][0])
            
            obj.stripState[n][1] += 10

            obj.update()

            min_index, old_min = obj.comparePixel(min_index, n)

            obj.stripState[old_min][1] = default_b

        obj.stripState[min_index][1] = default_b
        obj.swapPixel(i, min_index)

        obj.update()