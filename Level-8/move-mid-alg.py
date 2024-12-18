result = 2
step = 1

for i in range(0, int(input())):
    step = 2**i
    result += step
    
print(result**2)
