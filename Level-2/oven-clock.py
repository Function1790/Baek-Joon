h, m = map(int, input().split())
add = int(input())
m += add
h = (h + int(m / 60)) % 24
m = m % 60
print(h, m)
