alphabet = {i:-1 for i in "abcdefghijklmnopqrstuvwxyz"}
word = input()
for i in range(len(word)):
    if alphabet[word[i]]==-1:
        alphabet[word[i]]=i
print(" ".join([str(alphabet[i]) for i in alphabet]))