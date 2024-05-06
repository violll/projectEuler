def digitSum(n):
    res = 0
    while n >= 1:
        res += n % 10
        n //= 10
    return res

def powerfulDigitSum(maxA, maxB):
    maxDigitSum = 0
    for a in range(maxA-1, -1, -1):
        for b in range(maxB-1, -1, -1):
            n = a**b
            ds = digitSum(n)
            if ds > maxDigitSum: maxDigitSum = ds
    
    return maxDigitSum

print(powerfulDigitSum(100,100))