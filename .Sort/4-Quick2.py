def QuickSort(arr):
    if len(arr) <= 1:
        return arr  # 배열 길이가 1 이하일 경우 그대로 반환
    
    pivot = arr[len(arr) // 2]  # 중간값을 pivot으로 선택
    left = [x for x in arr if x < pivot]  # pivot보다 작은 값
    middle = [x for x in arr if x == pivot]  # pivot과 같은 값
    right = [x for x in arr if x > pivot]  # pivot보다 큰 값

    return QuickSort(left) + middle + QuickSort(right)  # 재귀적으로 정렬 후 합치기

# 테스트
arr = [3, 1, 4, 2, 5, 5, 6, 7, 8]
print(QuickSort(arr))  # [1, 2, 3, 4, 5, 5, 6, 7, 8]