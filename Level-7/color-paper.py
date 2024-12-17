def abs(x):
    if x < 0:
        return -x
    return x


size = 0
record = []
for i in range(int(input())):
    x, y = map(int, input().split())
    size += 100
    for j in record:
        xColliding = (x + 100 > j[0]) and (j[0] + 100 > x)
        yColliding = (y + 100 > j[1]) and (j[1] + 100 > y)
        if xColliding and yColliding:
            if (x < j[0] and y < j[1]):
                size -= abs((x+100-j[0])*1)
    record.append([x, y])
