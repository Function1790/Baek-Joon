n, m = map(int, input().split())
arr = [str(i + 1) for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a-=1
    b-=1
    arr[a],arr[b] = arr[b], arr[a]
print(" ".join(arr))