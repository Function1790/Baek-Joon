matrix = []
for i in range(5):
    matrix.append(input())
    matrix[i] += "●" * (15-len(matrix[i]))

result = ""
for i in range(15):
    for j in range(5):
        if matrix[j][i] == "●":
            continue
        result += matrix[j][i]

print(result)