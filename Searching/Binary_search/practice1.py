# This code implements finding of the elements in a sorted array (using binary search)

def binary_search(elems,low,high,x):

    if len(elems) is None:
        print("No element is given")


    mid = low + int((high - low)/2)

    while low <= high:

        print("Entered")
        if elems[mid] == x:
            return mid 

        if elems[mid] > x:
            low = 0
            high = mid
            mid = low + int((high -low)/2)
            continue
        else:
            low = mid 
            mid = low + int((high - low)/2)
            continue

    return -1

arr = [2,3,4,10,40]
print("The element is at index",binary_search(arr,0,len(arr)-1,2))

    

        

    