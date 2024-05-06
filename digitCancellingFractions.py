from highlyDivisibleTriangularNum import getAllFactors
import numpy as np

def getTestNums(sN, sD, intersection):
    if sN[0] == intersection: testN = sN[1]
    else: testN = sN[0]

    if sD[0] == intersection: testD = sD[1]
    else: testD = sD[0]

    return int(testN), int(testD)


def isDigitCancelling(num, den):
    sN = list(str(num))
    sD = list(str(den))

    intersection = np.intersect1d(sN, sD)
    if len(intersection) > 0:
        intersection = intersection[0]

        testN, testD = getTestNums(sN, sD, intersection)

        if testD == 0: return False

        if num / den == testN / testD:
            return True
        
        else: return False


def getDigitCancellingFraction():
    num = 10
    den = 11

    res = []

    while len(res) != 4:
        if (num % 10 == 0 and den % 10 == 0):
            pass
        elif isDigitCancelling(num, den):
            res.append((num, den))
        
        num += 1
        if num == den: 
            den += 1
            num = 10

    return res


def simplifyFraction(num, den):
    while True:
        fN = getAllFactors(num)
        fD = getAllFactors(den)
        intersection = np.intersect1d(fN, fD)
        if len(intersection) == 1 or num == 1: break
        gcd = np.max(intersection)
        num /= gcd
        den /= gcd

    return num, den


def getDenominator():
    fractions = getDigitCancellingFraction()
    num, den = 1, 1
    for n, d in fractions:
        num *= n
        den *= d

    return simplifyFraction(num, den)[1]
    

print(getDenominator())