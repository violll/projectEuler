from math import ceil
from highlyDivisibleTriangularNum import getAllFactors
from circularPrimes import getPrimeLst


def isPandigital(txt):
    for num in range(1, len(txt)+1):
        if txt.count(str(num)) != 1:
            return False
    
    return True

def checkPandigital(num, factors):
    for i in range(len(factors)//2):
        f1, f2 = factors[i], factors[len(factors)-i-1]
        strToCheck = str(f1) + str(f2) + str(num)
        if len(strToCheck) == 9 and isPandigital(strToCheck): 
            return True

    return False 

def hasUniqueDigits(num):
    res = set()
    while num >= 1:
        digit = num % 10
        if digit in res: return False
        else: res.add(digit)
        num = num//10
    return True

def getPandigitalProducts(max):
    numsList = set()
    primesLst = getPrimeLst(max)
    for num in [n for n in range(2, max) if n not in primesLst]:
        if hasUniqueDigits(num):
            factors = getAllFactors(num)
            if checkPandigital(num, factors[1:-1]):
                numsList.add(num)

    return sum(numsList)

def getMaxNum():
    i = 1
    while True:
        numDigitsRoot = len(str(int(ceil((i**0.5)))))
        i += 1
        if numDigitsRoot + len(str(i)) > 9: 
            return i

# print(getPandigitalProducts(getMaxNum()))
