N = int(input())


def prime_factorization(N):
    factors = []

    while N % 2 == 0:
        factors.append(2)
        N //= 2

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i

    # N이 1보다 크면 N은 소수이므로 추가
    if N > 1:
        factors.append(N)

    return factors

[print(i) for i in prime_factorization(N)]