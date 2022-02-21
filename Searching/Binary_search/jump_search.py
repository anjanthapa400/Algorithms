def jump_search(arr,elem):

    jumper = 2

    high = 0
    low = 0
    for x in range(0,len(arr),jumper):
        if arr[x] == elem:
            return x

        if arr[x] > elem:

            high = x
            for x in range(low,high):
                if arr[x] == elem:
                    return x
        else:
            low = x

    return -1




    
print(jump_search([ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610],21))

