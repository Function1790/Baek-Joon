text = input()
def check(text):
    l = len(text) - 1
    for i in range(int(l/2)+1):
        if text[i]!=text[l-i]:
            return 0
    return 1

print(check(text))