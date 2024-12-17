def rev(word):
    word = list(word)
    last = len(word) - 1
    for i in range(int(last / 2) + 1):
        word[i], word[last - i] = word[last - i], word[i]
    return "".join(word)


a, b = map(int, rev(input()).split())
print([a, b][b > a])
