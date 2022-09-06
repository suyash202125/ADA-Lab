#QUICKSORT ALGORITHM

#quick_sort function uses partition_position index
#returned by the partition function to recursively
#quick sort the left and right values to the partition_position index
def quick_sort(arr, left, right) :
    if left < right :
        #recieving the partition_position index
        partition_pos = partition(arr, left, right)
        #recursively sorting the left array
        quick_sort(arr, left, partition_pos - 1)
        #recursively sorting the right array
        quick_sort(arr, partition_pos + 1, right)

#partition function returns the index of the partition position
def partition(arr, left, right) :
    i = left
    j = right - 1
    pivot = arr[right] #pivot is the right most element

    #moving i and j pointers 
    while i < j :
        while i < right and arr[i] < pivot :
            i += 1

        while j > left and arr[j] >= pivot :
            j -= 1

        #check if i and j hasn't crossed yet
        #if not, swap the i and j elements
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    #if i and j crossed, we swap the pivot and i element
    if arr[i] > pivot :
        arr[i], arr[right] = arr[right], arr[i]

    #returning the partition index
    return i


#driver code
arr = [77, 55, 66, 11, 33, 22, 99, 88, 44]
print('before applying quicksort:', arr)
quick_sort(arr, 0, len(arr) - 1)
print('after applying quick_sort:', arr)