croatian = ["c=", "c-", "d*", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in croatian:
    word = word.replace(i, "*")
print(len(word))