from largestPrimeFactor import isPrime

def sumPrimes(maxPrime):
    sum = 0
    testPrime = 1

    while testPrime < maxPrime:
        if isPrime(testPrime):
            sum += testPrime
        testPrime += 1

    return sum

print(sumPrimes(2000000))
