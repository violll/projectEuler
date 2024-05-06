def digitCount(num):
    res = {i:0 for i in range(10)}
    while num >= 1:
        digit = num%10
        res[digit] += 1
        num //= 10
    return(res)

def permutatedMultiples():
    multiples = [2, 3, 4, 5, 6]
    n = 1
    while True:
        valid = True
        ns = [i * n if len(str(2 * n)) == len(str(i*n)) else False for i in multiples]
        if False not in ns:
            for nx in ns[1:]:
                reqDigits = digitCount(ns[0])
                if digitCount(nx) != reqDigits:
                    valid = False
                    break
            if valid: return n
        n += 1

print(permutatedMultiples())