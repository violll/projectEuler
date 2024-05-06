from largestPrimeFactor import isPrime

def eqn(n, a, b):
    return n**2 + a * n + b

def getPrimeChainLength(a, b):
    chainLen = 0
    n = 0

    while True:
        if isPrime(eqn(n, a, b)):
            chainLen += 1
        else: return chainLen

        n += 1

def getQuadraticPrimes(maxA,maxB):
    bestA = None
    bestB = None
    maxPrimes = 0
    for a in range(-maxA+1, maxA):
        for b in range(0, maxB+1):
            if isPrime(b):
                currMaxPrimes = getPrimeChainLength(a, b)
                if currMaxPrimes > maxPrimes:
                    maxPrimes = currMaxPrimes
                    bestA = a
                    bestB = b

    return bestA * bestB

print(getQuadraticPrimes(1000, 1000))