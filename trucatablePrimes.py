from circularPrimes import getPrimeLst
from largestPrimeFactor import isPrime

def isTruncatablePrimeRTL(n):
    while n >= 1:
        if not isPrime(n): return False
        n = n//10

    return True

def isTruncatablePrimeLTR(n):
    while n >= 1:
        if not isPrime(n): return False

        if len(str(n)) != 1: n = int(str(n)[1:])
        else: break
    
    return True

def getTruncatablePrimes():
    res = set()

    lst = sorted(list(getPrimeLst(1000000)))[4:]

    i = 0
    n = lst[i]
    while len(res) != 11:
        if isPrime(n) and isTruncatablePrimeRTL(n//10) and isTruncatablePrimeLTR(n):
            res.add(n)
        i += 1
        n = lst[i]
    
    return sum(res)

# print(getTruncatablePrimes())