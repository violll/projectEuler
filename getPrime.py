from largestPrimeFactor import isPrime


def getPrime(xth):
    start = 1
    count = 0
    while count < xth:
        if isPrime(start):
            count += 1
        if xth == count: return start
        else: start += 1
    return start

# print(getPrime(10001))