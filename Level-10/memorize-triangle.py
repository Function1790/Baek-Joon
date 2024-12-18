angle = [int(input()), int(input()), int(input())]
total = sum(angle)

if angle[0]==60 and angle[1]==60 and angle[2]==60:
    print("Equilateral")
elif total == 180 and (angle[0]==angle[1] or angle[1]==angle[2] or angle[0]==angle[2]):
    print("Isosceles")
elif total == 180 and  (angle[0]!=angle[1] and angle[1]!=angle[2] and angle[0]!=angle[2]):
    print("Scalene")
else:
    print("Error")