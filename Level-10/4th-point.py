p = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]

x = {}
y = {}
for i in p:
    try:
        x[str(i[0])] += 1
    except:
        x[str(i[0])] = 1
    try:
        y[str(i[1])] += 1
    except:
        y[str(i[1])] = 1
        
result = [0, 0]
for i in range(3):
    if x[str(p[i][0])]==1:
        result[0]=str(p[i][0])
    if y[str(p[i][1])]==1:
        result[1]=str(p[i][1])
print(" ".join(result))