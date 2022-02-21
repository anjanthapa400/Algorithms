# This code is used to perform interpolation search to find the elements if it is uniformly distributed


def interpolation_search(arr,x):

    low = 0
    high = len(arr) - 1


    while low <= high:

        pos = low + ((x - arr[low])/(arr[high] - arr[low])) * (high - low)


        if arr[int(pos)] == x:
            return int(pos) 

        if arr[int(pos)] > x:
            high = int(pos) - 1

        else:
            low = int(pos) + 1

    return -1


arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
print("The value of the element is at index",interpolation_search(arr,10))
