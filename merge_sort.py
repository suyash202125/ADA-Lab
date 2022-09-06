# Merge Sort algorithm

def merge_sort(arr) :
    if len(arr) > 1 :
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursive call
        merge_sort(left_arr) #sorting left half
        merge_sort(right_arr) #sorting right half

        #merge
        i = 0 #left_arr index
        j = 0 #right_arr index
        k = 0 #merged array index

        #merging data in the sorted order
        while i < len(left_arr) and j < len(right_arr) :
            if left_arr[i] < right_arr[j] :
                arr[k] = left_arr[i]
                i += 1
            else :
                arr[k] = right_arr[j]
                j += 1
            k += 1

        #checking if any element left in the left half
        while i < len(left_arr) :
            arr[k] = left_arr[i]
            i += 1
            k += 1

        #checking if any element left in the right half
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


#driver code
arr_test = [2, 3, 5, 1, 7, 11, 9, 4, 4]
print('before sorting:',arr_test)
merge_sort(arr_test)
print('after sorting:',arr_test)