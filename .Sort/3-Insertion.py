def InsertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= 0:
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = temp
    return arr


arr = [2, 3, 5, 1, 4]
print(InsertionSort(arr))
