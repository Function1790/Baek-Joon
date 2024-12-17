M = int(input())
index = 1
for i in range(8):
    data = int(input())
    if data > M:
        M = data
        index = i + 2
print(M)
print(index)
