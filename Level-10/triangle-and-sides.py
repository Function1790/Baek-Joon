while True:
    sides = list(map(int, input().split()))
    total = sum(sides)
    if total==0:
        break
    if max(sides) >= total - max(sides):
        print("Invalid")
    elif sides[0]==sides[1] and sides[1]==sides[2] and sides[0]==sides[2]:
        print("Equilateral")
    elif sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]:
        print("Isosceles")
    elif sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2]:
        print("Scalene")