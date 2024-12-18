def main():
    sticks = list(map(int, input().split()))
    for i in range(sticks[0], 0, -1):
        for j in range(sticks[1], 0, -1):
            for k in range(sticks[2], 0, -1):
                sides = [i, j, k]
                total = sum(sides)
                M = max(sides)
                if M >= total - M:
                    continue
                print(total)
                return

main()