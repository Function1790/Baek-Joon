def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    step = 0
    start = 1
    while True:
        step += 1
        end = start + 6 * step
        start += 1
        if start <= n <= end:
            print(step + 1)
            return
        start = end


main()
