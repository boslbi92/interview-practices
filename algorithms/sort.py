import copy

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) / 2
        lefthalf, righthalf = array[:mid], array[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0

        while(i < len(lefthalf) and j < len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while(i < len(lefthalf)):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while(j < len(righthalf)):
            array[k] = righthalf[j]
            j += 1
            k += 1
        return array

print mergeSort([54,26,93,17,77,31,44,55,20])