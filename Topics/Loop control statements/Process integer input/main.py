while True:
    value = int(input())
    if value > 100:
        break
    if value < 10:
        continue
    else:
        print(value)
