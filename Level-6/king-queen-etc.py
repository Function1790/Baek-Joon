base = [1, 1, 2, 2, 2, 8]
data = list(map(int, input().split()))
print(" ".join([str(base[i] - data[i]) for i in range(6)]))