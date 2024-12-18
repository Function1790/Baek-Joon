A, B, V = map(int, input().split())

temp = A - B
day = int((V-B)/temp)
while True:
    temp2 = day * temp
    if V <= temp2 or V <= temp2 + B:
        print(day)
        break
    day += 1
