croatian = ["c=", "c-", "d*", "d-", "lj", "nj", "s=", "z="]
word = input()
for _ in range(2):
    word = list(word)
    for i in range(len(word) - 1):
        if word[i] + word[i + 1] in croatian:
            word[i] = "*"
            word[i + 1] = ""
    word = "".join(word)
    print(word)
print(len(word))
