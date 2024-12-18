height, width = map(int, input().split())
base = []
for i in range(height):
    base.append(list(input()))


def paint(x, y):
    try:
        count = 0
        diff_color = ["W", "B"][board[step][y][x] == "W"]
        print(end=f"[{x},{y}]\t")
        if y >= 1 and board[step][y - 1][x] != diff_color:
            print(end="1")
            board[step][y - 1][x] = diff_color
            count += 1
        if y + 1 < height and board[step][y + 1][x] != diff_color:
            print(end="2")
            board[step][y + 1][x] = diff_color
            count += 1
        if x >= 1 and board[step][y][x - 1] != diff_color:
            print(end="3")
            board[step][y][x - 1] = diff_color
            count += 1
        if x + 1 < width and board[step][y][x + 1] != diff_color:
            print(end="4")
            board[step][y][x + 1] = diff_color
            count += 1
        print()
    except:
        print(step)
        print(board[step])
    return count


def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


board = []
board.append(base)
board.append(base)
for i in range(3):
    matrix = rotate_90(board[len(board) - 1])
    board.append(matrix)
    board.append(matrix)

m = 0
step = 0
while step < 8:
    count = 0
    for y in range(height):
        for x in range(width):
            count += paint(x, y)
    print(count)
    print("=======================")

    if m > count or step == 0:
        m = count

    step += 1

    count = 0
    print(board[step])
    for x in range(width):
        for y in range(height):
            count += paint(x, y)
    print(count)
    print("=======================")

    if m > count:
        m = count

    step += 1
    width, height = height, width
print(m)
