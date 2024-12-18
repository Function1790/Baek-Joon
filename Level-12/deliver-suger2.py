N = int(input())

counts = []
for i in range(N):
    for j in range(N):
        if 5 * i + 3 * j == N:
            counts.append(i + j)

if len(counts)==0:
    print(-1)
else:
    print(min(counts))
