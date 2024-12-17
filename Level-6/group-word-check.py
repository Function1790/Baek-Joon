def check():
    word = list(input())
    memory = {}
    for i in range(len(word)):
        try:
            if i - memory[word[i]] != 1:
                return 0
            else:
                memory[word[i]] = i
        except:
            memory[word[i]] = i
    return 1


n = int(input())
count = 0
for _ in range(n):
    count += check()
print(count)
