class HeapSort:
    array = [6, 4, 3, 8, 1, 5, 2, 7]

    def heapifyDown(self, arr, n, i):
        largest = i  # Initialize with root
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than parent
        if left < n and arr[i] < arr[left]:
            largest = left

        # Check if right child exits and is greater than largest
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Change parent, if needed
        if largest != i:
            # Swap the parent with largest child
            (arr[i], arr[largest]) = (arr[largest], arr[i])
            # Heapify because of swap
            self.heapifyDown(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)

        # Build the MaxHeap
        # Since last parent will be at ((n//2)-1) we can start at that location
        for i in range(n // 2 - 1, -1, -1):
            self.heapifyDown(arr, n, i)

        # One by one extract parent element
        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            heapifyDown(arr, i, 0)

        return arr

    if __name__ == "__main__":
        print(heapSort(array))
