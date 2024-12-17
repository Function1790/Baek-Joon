background = [[0 for i in range(100)] for j in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        if y+i>=100:
            break
        for j in range(10):
            if x+j>=100:
                break
            background[y+i][x+j]=1
            
print(sum([sum(background[i]) for i in range(100)]))