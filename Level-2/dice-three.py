a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or c == a:
    add = b
    if c == a:
        add = c
    print(1000 + add * 100)
else:
    add = max([a, b, c])
    print(add * 100)
