# recursive solution

import math


def getPrimeFactorLst(num, lst):
    if isPrime(num):
        lst.append(num)
        return lst
    else: 
        factor1, factor2 = getFactors(num)
        getPrimeFactorLst(factor1, lst)
        getPrimeFactorLst(factor2, lst)
        return lst

def getFactors(num):
    for i in range(2,num):
        if num%i == 0:
            return i, num//i

def isPrime(num):
    if num <= 1: return False
    else: 
        for i in range(2, int(math.sqrt(num)) + 1):
            if num%i == 0: return False
        return True

# print(getPrimeFactorLst(600851475143, []))