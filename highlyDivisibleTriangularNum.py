import math


def getXthTriangleNum(xth):
    sum = 0
    for i in range(1,xth+1):
        sum += i
    return sum

def getAllFactors(num):
    res = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num%i == 0:
            res.add(i)
            if num//i not in res: res.add(num//i)
    
    return sorted(list(res))

def highlyDivisibleTriangleNum(minFactors):
    i = 1
    triangleNum = getXthTriangleNum(i)
    factors = len(getAllFactors(triangleNum))

    while factors < minFactors:
        i += 1
        tempNum = getXthTriangleNum(i)
        tempFactors = len(getAllFactors(tempNum))
        if tempFactors > factors: 
            factors = tempFactors
            triangleNum = tempNum
        
    return triangleNum

# print(highlyDivisibleTriangleNum(500))