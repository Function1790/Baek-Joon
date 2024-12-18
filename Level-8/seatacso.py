change = [25, 10, 5, 1]

T = int(input())
for _ in range(T):
    left = int(input())
    result = []
    for i in change:
        result.append(str(int(left / i)))
        left = left % i
    print(" ".join(result))