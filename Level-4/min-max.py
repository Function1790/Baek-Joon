_ = int(input())
arr = list(map(int, input().split()))
m = arr[0]
M = arr[0]
for i in arr:
    if i < m:
        m = i
    if i > M:
        M = i
        
print(m, M)