def SelectionSort(arr):
    length = len(arr)
    for i in range(length - 1):
        min_value = arr[i]
        min_index = i
        for j in range(i + 1, length):
            if min_value < arr[j]:
                min_value = arr[j]
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


N, k = map(int, input().split())
arr = list(map(int, input().split()))
print(SelectionSort(arr)[k - 1])
