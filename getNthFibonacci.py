def getNumDigits(num):
    digits = 0
    while num >= 1:
        digits += 1
        num //= 10
    return digits

def getFibIdx(n1, n2, idx, digitNum):
    while getNumDigits(n1) != digitNum:
        n1, n2 = n2, n1+n2
        idx += 1
    
    return idx

# print(getFibIdx(1, 1, 1, 1000))