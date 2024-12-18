num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())

result = ""
left = N
for i in range(100, -1, -1):
    Bexp = B**i
    result += num[int(left / Bexp)]
    left = left % Bexp
print(result.lstrip('0'))