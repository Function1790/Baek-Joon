dial_pad = [
    "",
    "",
    "",  # 1
    "ABC",  # 2
    "DEF",  # 3
    "GHI",  # 4
    "JKL",  # 5
    "MNO",  # 6
    "PQRS",  # 7
    "TUV",  # 8
    "WXYZ",  # 9
    "OPERATOR",  # 0
]

word = input()
time = 0
for i in word:
    for j in range(len(dial_pad)):
        if i in dial_pad[j]:
            time += j
            break
print(time)