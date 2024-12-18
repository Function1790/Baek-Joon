def isPrime(N):
    if N <= 1:
        return 0
    if N == 2 or N == 3:
        return 1
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return 0
    return 1

M = int(input())
N = int(input())

result = [i for i in range(M, N+1) if isPrime(i)]
if len(result)!=0:
    print(sum(result))
    print(result[0])
else:
    print(-1)