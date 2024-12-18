def main():
    N = int(input())

    for i in range(1, N+1):
        total = i + sum([int(j) for j in str(i)])
        if total == N:
            print(i)
            return
        if N==i:
            print(0)

main()