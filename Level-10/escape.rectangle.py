x, y, w, h = map(int, input().split())


def abs(n):
    if n < 0:
        return -n
    return n

print(min([x, y, abs(x-w), abs(x+w), abs(y-h), abs(y+h)]))