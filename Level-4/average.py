n = int(input())
arr = list(map(int, input().split()))
arr = [i / max(arr) * 100 for i in arr]
print(sum(arr)/len(arr))