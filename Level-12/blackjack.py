N, M = map(int, input().split())
cards = list(map(int, input().split()))
length = len(cards)

cards.sort()

best = 0
for i in range(length - 2):
    for j in range(i+1, length - 1):
        for k in range(j+1,length):
            total = cards[i] + cards[j] + cards[k]
            if best < total <= M:
                best = total
print(best)