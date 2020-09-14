# Decrease-and-conquer: insertion sort


# Function to sort Array recursively
def insertionSortRecursive(array, n):
    if n <= 1:
        return
    # Sort first n-1 elements
    insertionSortRecursive(array, n - 1)

    # Insert last element into its correct
    # place in sorted array
    current_value = array[n - 1]
    j = n - 2
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and array[j] > current_value:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = current_value


# Iterative version (bottom-up)
def insertionSortIteration(array, n):
    # Traverse through 1 to len(arr)
    for i in range(1, n):

        current_value = array[i]
        j = i-1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and array[j] > current_value:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current_value


arr = [1, 2, 4, 5, 6, 7, 8, 3]
size = len(arr)
insertionSortIteration(arr, size)
print(arr)

# insertionSortRecursive(arr, size)
# print(arr)
