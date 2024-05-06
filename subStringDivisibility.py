from usefulFcns import *


def isDivisible(num, primes):
    for i in range(len(primes)):
        testPrime = primes[i]
        testNum = int(str(num)[i+1:i+4])
        if testNum / testPrime != testNum // testPrime:
            return False

    return True

from sympy.utilities.iterables import multiset_permutations

def subStringDivisibility():
    tot = 0
    primes = list(getPrimeLst(18))

    for perm in multiset_permutations("0123456789"):
        num = int("".join(perm))
        if isDivisible(num, primes):
            tot += num
    
    return tot

print(subStringDivisibility())