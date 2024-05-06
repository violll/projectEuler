from highlyDivisibleTriangularNum import getAllFactors
from largestPrimeFactor import getPrimeFactorLst

def A132740(n):
    lst = getPrimeFactorLst(n, [])
    factors = [num for num in lst if num != 2 and num !=5]
    res = 1
    for factor in factors:
        res *= factor
    return res

# def isCoprime(n1, n2):
#     f1 = getAllFactors(n1)
#     f2 = getAllFactors(n2)
#     intersection = [factor for factor in f1 if factor in f2]
#     if len(intersection) == 1:
#         return True
#     else: return False

def getTerminatingDecimalDenominators(max):
    res = []
    for i in range(max):
        for j in range(max):
            num = 2**i*5**j
            if num > max: break
            if num not in res: res.append(num)
    return sorted(res)

def getR(q):
    searching = True
    r = 1
    while searching:
        if 10**r % q == 1:
            return r
        r += 1

def getLongestRecipCycle(max):
    terminatingDecimals = getTerminatingDecimalDenominators(1000)
    maxLen = 0
    maxi = 0
    for i in range(1,max):
        if i not in terminatingDecimals: 
            q = A132740(i)
            r = getR(q)
            if r > maxLen: 
                maxLen = r
                maxi = i
    return maxi

print(getLongestRecipCycle(1000))
