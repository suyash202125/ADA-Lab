# Python program for BINARY SEARCH

# binary search funtion
def Binary_Search(sequence, target_num):
    start_index = 0
    end_index = len(sequence) - 1

    # loop to search the index of the target_num
    while start_index <= end_index :
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = sequence[mid_index]

        # if mid_value matches the target_num return the index of the mid_value i.e., mid_index
        if mid_value == target_num :
            return mid_index
        elif mid_value < target_num :
            # shifting the start index to the right of the mid index
            start_index = mid_index + 1 
        elif mid_value > target_num :
            # shifting the end index to the left of the mid index
            end_index = mid_index - 1

    # if number is not in the list return none
    return None


# numbers list
sequence_a = [2, 3, 5, 6, 8, 9, 11, 14, 15, 16, 22, 34, 37, 43, 47, 50]
# taking input for the number to find
num_find = int(input("Enter the number for the search: "))


# output
if Binary_Search(sequence_a, num_find) :
    print("The number is at the index:", Binary_Search(sequence_a, num_find))
elif Binary_Search(sequence_a, num_find) is None :
    print("The number is not in the list.")