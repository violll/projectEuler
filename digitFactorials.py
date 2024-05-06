def factorial(num):
    if num == 0: return 1
    elif num == 1: return num
    else:
        return num * factorial(num-1)

def digitFactorials():
    res = []
    n = 3
    while True:
        if n == sum([factorial(int(digit)) for digit in list(str(n))]):
            res.append(n)
        n += 1

        if n == 1000000: break

    return sum(res)

print(digitFactorials())