# This is the code implementation of exponential search by recursive approach

def binary_search(arr,low,high,x):

    mid = int((low + high)/2)

    if arr[mid] == x:
        return mid 

    if arr[mid] > x:
        binary_search(arr,low,mid-1,x)

    else:
        binary_search(arr,low+1,high,x)

    return -1



def exponential_search(arr,elem):
    expo_val = 0
    prev_val = 0
    x = 0
    while expo_val <=len(arr)-1:
        
        if arr[expo_val] == elem:
            return expo_val

        expo_val = 2**(x)
        if arr[expo_val] > elem:
            return binary_search(arr,prev_val,expo_val,elem)
        
        else:
            prev_val = expo_val

        x = x + 1



arr = [2, 3, 4, 10, 40]
print("The value of elem is at index",exponential_search(arr,2))
