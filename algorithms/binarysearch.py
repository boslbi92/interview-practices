

def main(array, k):
    if len(array) == 0:
        return False
    return binary_search(array, k, 0, len(array)-1)

def binary_search(array, k, start, end):
    while(start <= end):
        mid = (start + end) / 2
        if array[mid] == k:
            return True
        else:
            if array[mid] < k:
                return binary_search(array, k, mid+1, end)
            else:
                return binary_search(array, k, start, mid-1)
    return False

array = range(1000)
print array
print main(array, -28)