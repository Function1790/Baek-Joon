N = int(input())
temp = N

big = N // 5
N = N % 5

small = N // 3
left = N % 3

if left != 0:
    N = temp
    small = N // 3
    left = N % 3
    if left != 0:
        print(-1)
    else:
        print(small)
else:
    print(big + small)
