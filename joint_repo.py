def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

arr = [2, 1, 4, 4.5, 5, 6.2, 5, 6, 7, 17.8, 10, 15, 'cat', 'apple', 'ball', 'duck', 'frog', 'eagle', 'green', 25, 3.14, 17, 8]

# Split the list into numbers and strings and float and sort separately
numbers = [x for x in arr if isinstance(x, int)]
numbers_float = [x for x in arr if isinstance(x, float)]
strings = [x for x in arr if isinstance(x, str)]

heapSort(numbers)
heapSort(numbers_float)
strings.sort()  # Alphabetical sorting for strings

#Sort by number age
combined_sorted = numbers + numbers_float
combined_sorted.sort()
arr = combined_sorted + strings

print('Sorted array is')
for i in arr:
    print(i)
