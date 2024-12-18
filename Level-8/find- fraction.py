def main():
    X = int(input())

    count = 0
    step = 0
    while True:
        step += 1
        if X > count + step:
            count += step
            continue
        else:
            for i in range(step):
                count += 1
                if X == count:
                    print(f"{i+1}/{step-i}")
                    return


main()
