_ = input()
arr = list(map(int, input().split()))


def isPrime(N):
    if N <= 1:
        return 0
    if N == 2 or N == 3:
        return 1
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return 0
    return 1


print(sum([isPrime(i) for i in arr]))
