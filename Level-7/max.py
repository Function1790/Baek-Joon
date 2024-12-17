M = 0
pos = [0, 0]
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] > M:
            M = arr[j]
            pos = [i, j]
print(M)
print(pos[0] + 1, pos[1] + 1)
