import math

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


def consecPrimeSum(max):
    primes = getPrimeLst(max)
    sortedPrimes = sorted(list(primes))
    maxP = None
    maxConsec = 0
    
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            s = sum(sortedPrimes[i:j+1])

            if s > max:
                break

            if s in primes and j-i+1 > maxConsec:
                maxP = s
                maxConsec = j-i+1
    
    return "The longest sum of consecutive primes below 1m that adds to a prime, containes {} terms, and is equal to {}".format(maxConsec, maxP)


print(consecPrimeSum(1000000))
