n, m = map(int, input().split())
arr = ["0" for i in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        arr[x] = str(k)
print(" ".join(arr))