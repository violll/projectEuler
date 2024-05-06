from collections import Counter


def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: 
            return False
    return True

def getNextPrime(n=0):
    n += 1
    while not isPrime(n): n += 1
    return n

def primePairSets(numPrimes):
    testedPrimes = {}
    currPrimes = set()

    n1 = getNextPrime(2)
    currPrimes.add(n1)
    testedPrimes[n1] = 0
    n2 = getNextPrime(n1)

    while len(currPrimes) < numPrimes:
        testSuccess, testedPrimes = testPairs(currPrimes, n2, testedPrimes)
        if testSuccess:
            currPrimes.add(n2)
            testedPrimes[n2] = 0
            n1 = n2
        
        elif Counter(testedPrimes).most_common()[0][1] > 10**4:
            primeToRemove = Counter(testedPrimes).most_common()[0][0]
            print(currPrimes)
            currPrimes.remove(primeToRemove)
            testedPrimes.pop(primeToRemove)
            print("Removed {}".format(primeToRemove))
            n2 = primeToRemove

        n2 = getNextPrime(n2)
    
    print(testedPrimes)
    return currPrimes

def testPairs(currPrimes, n, testedPrimes):
    if n in currPrimes: return False, testedPrimes
    for n1 in currPrimes:
        print(n1, testedPrimes)
        if not isPrimePair(n1, n): 
            if n > max(currPrimes): testedPrimes[n1] += 1
            return False, testedPrimes
    return True, testedPrimes

def isPrimePair(n1, n2):
    if isPrime(int(str(n1) + str(n2))) and isPrime(int(str(n2) + str(n1))):
        return True
    else: 
        return False

# prime pairs are connected such that the numbers in the list of potential pairs is always smaller than the prime pair they all share 
def getPotentialPrimePairs(maxN):
    primePairs = {}
    
    n = getNextPrime(2)
    while n < maxN:
        n2 = getNextPrime(n)
        primePairs[n] = []
        while n2 < maxN:
            # print(n, n2)
            if isPrimePair(n, n2):
                primePairs[n].append(n2)
            n2 = getNextPrime(n2)
        n = getNextPrime(n)
    
    return primePairs

def primePairSets2(nPrimes, maxP):
    primePairs = getPotentialPrimePairs(maxP)

    currPrimes = set()

    currPrimes = []

    for n in primePairs.keys():
        print(n)
        currPrimes.append(n)
        res = primePairSetsRecursive(currPrimes, primePairs, nPrimes, {n+1: 0 for n in range(nPrimes)})[0]
        if len(res) == nPrimes: return res
        currPrimes.remove(n)

def primePairSetsRecursive(currPrimes, primePairs, nPrimes, counter):
    if len(currPrimes) == nPrimes:
        return currPrimes, primePairs, nPrimes, counter
    elif len(currPrimes) == 0:
        return currPrimes, primePairs, nPrimes, counter

    potentialPairs = primePairs[currPrimes[0]]
    for n in currPrimes[1:]:
        potentialPairs = list(set(potentialPairs) & set(primePairs[n]))
    
    for n in sorted(potentialPairs)[counter[len(currPrimes)]:]:
        print(len(currPrimes) * "\t", n)
        return primePairSetsRecursive(currPrimes + [n], primePairs, nPrimes, counter)
    
    if len(currPrimes) == 1: 
        counter[1] += 1

    else: 
        counter = {n+1: 0 if n+1 > len(currPrimes)-1 else counter[n+1] if n+1 < len(currPrimes)-1 else counter[n+1] + 1 for n in range(nPrimes)}

    return primePairSetsRecursive(currPrimes[:-1], primePairs, nPrimes, counter)


print(primePairSets2(5, 10**4))