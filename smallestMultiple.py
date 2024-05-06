import numpy

from largestPrimeFactor import getPrimeFactorLst

# smart solution, much faster!
def getPrimeFactorizationOfRange(min, max):
    set = [i for i in range(min, max)]
    res = []

    for num in set[::-1]:
        factors = getPrimeFactorLst(num, [])
        factorsDict = {}
        for factor in factors:
            if factor not in factorsDict:
                factorsDict[factor] = factors.count(factor)
        for factor in factorsDict:
            if res.count(factor) < factorsDict[factor]:
                res.extend([factor for _ in range(factorsDict[factor] - res.count(factor))])
    return numpy.prod(res)

print(getPrimeFactorizationOfRange(1,20))

# slow solution
def smallestMultiple(min, max):
    set = [i for i in range(min, max+1)]
    checking = True
    testNum = max+1
    while checking:
        if checkDivisibility(testNum, set): 
            checking = False
            return testNum
        else: testNum += 1

def checkDivisibility(num, set):
    for factor in set[::-1]:
        if num%factor != 0: return False
    return True 

# print(smallestMultiple(1,20))