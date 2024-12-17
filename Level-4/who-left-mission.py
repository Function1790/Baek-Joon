arr = [i+1 for i in range(30)]
for i in range(28):
    n = int(input())
    for j in range(len(arr)):
        if arr[j]==n:
            break
    arr.pop(j)
print(arr[0])
print(arr[1])