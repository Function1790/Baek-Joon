def QuickSort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    pL = 0
    pR = len(arr) - 1
    mid = (pL + pR) // 2
    if len(arr) % 2 == 0:
        mid += 1
    pivot = arr[mid]
    while pL <= pR:
        while arr[pL] < pivot:
            pL += 1
        while arr[pR] > pivot:
            pR -= 1
        arr[pL], arr[pR] = arr[pR], arr[pL]
        pR -= 1
        pL += 1
    return QuickSort(arr[:mid]) + QuickSort(arr[mid:])


arr = [3, 1, 4, 2, 5, 5, 6, 7, 8]
print(QuickSort(arr))
