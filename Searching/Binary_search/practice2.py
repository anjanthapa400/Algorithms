# This is the code for optimized binary search 

def binary_search(arr,low,high,x):

  #  mid = low + int((high -low)/2)


    while low <= high:


        
        mid = low + int((high -low)/2)


        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            high = mid -1

        else:
            low = mid + 1

        
    return -1


arr = [2,3,4,10,40]

print("The element is at index",binary_search(arr,0,len(arr)-1,40))

