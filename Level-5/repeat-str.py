n = int(input())
for i in range(n):
    data = input().split()
    r, s = int(data[0]), data[1]
    print("".join([i*r for i in s]))