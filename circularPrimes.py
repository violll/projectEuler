import time
import math

def isCircular(num, lst):
    sNum = str(num)
    if len(sNum) == 1: return True
    for i in range(1, len(sNum)):
        tsNum = sNum[i:] + sNum[:i]
        if int(tsNum) not in lst: return False

    
    return True

def getPrimeLst(max):
    num = 2
    res = set()
    while num < max:
        failed = False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num%i == 0: 
                failed = True
                break
        if not failed:
            res.add(num)
        num += 1
        
    return res

def getCircularPrimes(max):
    count = 0
    primeLst = getPrimeLst(max)
    for currPrime in primeLst:
        if isCircular(currPrime, primeLst):
            count += 1        
    return count

# sTime = time.time()

# print(getCircularPrimes(1000000))

# print(time.time() - sTime)
