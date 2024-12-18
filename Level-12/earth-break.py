N = int(input())

step = 0
number = 666
while True:
    if str(number).find("666") != -1:
        step += 1
    if step==N:
        print(number)
        break
    number+=1