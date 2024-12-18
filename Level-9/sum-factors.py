while True:    
    N = int(input())
    if N==-1:
        break
    arr = [1]
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            arr.append(i)
            if i != N // i:
                arr.append(N // i)
    total = sum(arr)
    if total == N:
        arr.sort()
        print(N,"="," + ".join(str(i) for i in arr))
        
    else:
        print(f"{N} is NOT perfect.")