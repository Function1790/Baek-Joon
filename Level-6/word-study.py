word = input().upper()
count = {}
for i in word:
    try:
        count[i] += 1
    except:
        count[i] = 1
M = "?"
c = 0
for i in count:
    if count[i] > c:
        M = i
        c = count[i]
    elif count[i] == c:
        M = "?"
print(M)
