import math


# Partitioning based on position
def mergesort(array):
    # Call helper method to sort array recursively
    mergesorthelper(array, 0, len(array) - 1)


def mergesorthelper(arr, start, end):

    if start >= end:
        return

    mid = math.floor((start + end) / 2)

    mergesorthelper(arr, start, mid)
    mergesorthelper(arr, mid + 1, end)
    # Now merge the two sorted sub-arrays array[start...mid]
    # and array[mid+1...end]
    i = start
    j = mid + 1
    aux = []

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1

        else:  # arr[i] > arr[j]
            aux.append(arr[j])
            j += 1

    while i <= mid:
        aux.append(arr[i])
        i += 1

    while j <= end:
        aux.append(arr[j])
        j += 1

    arr[start:end + 1] = aux


array = [6, 4, 3, 8, 1, 5, 2, 7]
mergesort(array)
print(array)
