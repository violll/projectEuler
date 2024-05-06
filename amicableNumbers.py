from highlyDivisibleTriangularNum import getAllFactors

# solution 1
def getDivisors(n):
    res = getAllFactors(n)
    res = [factor for factor in res if factor != n]
    if n**0.5 in res: res.remove(n**0.5)
    return res

def isAmicablePair(a, b):
    if sum(getDivisors(a)) == b and sum(getDivisors(b)) == a:
        return True
    else: 
        return False

def getAmicableNumbers(maxNum):
    res = []
    for i in range(1, maxNum):
        for j in range(i+1, maxNum):
            if isAmicablePair(i, j):
                print(res)
                print(i, j)
                if i not in res: res.append(i)
                if j not in res: res.append(j)
    return res

def getAmicableNumberSum(maxNum):
    return sum(getAmicableNumbers(maxNum))

# print(getAmicableNumberSum(10000))