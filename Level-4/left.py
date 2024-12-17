count = {str(i): 0 for i in range(42)}
for i in range(10):
    count[str(int(input())%42)] += 1

print(sum([1 for i in count if count[i]!=0]))
