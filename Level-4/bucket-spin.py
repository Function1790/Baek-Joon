n, m = map(int, input().split())
arr = [str(i+1) for i in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(x, int((x+y)/2)+1):
        arr[i], arr[y-(i-x)] = arr[y-(i-x)], arr[i]
print(" ".join(arr))