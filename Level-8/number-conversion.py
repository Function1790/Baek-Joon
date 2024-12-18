num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
B = int(B)

total = 0
for i in range(len(N)):
    total += num.find(N[i]) * B ** (len(N) - i - 1)
print(total)