import random

array = [6, 4, 3, 8, 1, 5, 2, 7]


def quicksortlomuto(arr, start, end):
    # Base case
    if start >= end:
        return

    # Pickup a random element as pivot
    # randindex = random.randint(start, end)
    # (arr[randindex], arr[start]) = \
    #     (arr[start], arr[randindex])

    pivot = arr[start]
    smaller = start

    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= pivot:
            smaller += 1
            (arr[smaller], arr[bigger]) = \
                (arr[bigger], arr[smaller])

    # Place pivot on its right place
    (arr[start], arr[smaller]) = (arr[smaller], arr[start])

    quicksortlomuto(arr, start, smaller - 1)
    quicksortlomuto(arr, smaller + 1, end)


def quicksorthoare(array, start, end):
    # Base case
    if start >= end:
        return

    pivot = array[start]
    left = start
    right = end


def quicksort(array):
    start = 0
    end = len(array) - 1
    quicksortlomuto(array, start, end)
    quicksorthoare(array, start, end)
    return array


if __name__ == "__main__":
    print(quicksort(array))
