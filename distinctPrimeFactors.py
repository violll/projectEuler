def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def primeFactorization(n, primes):
    factors = set()
    i = 0
    
    while n > 1:
        f = primes[i]
        if n % f == 0:
            n /= f
            factors.add(f)
        else:
            i += 1
    
    return factors

def nConsecDistinctPrimeFactors(nConsec):
    startN = 2
    n = startN
    primes = []

    while True:
        while n < startN + nConsec:
            if isPrime(n): 
                primes.append(n)
                startN = n + 1
                n = startN
                break

            # get prime factorization
            pFactors = primeFactorization(n, primes)
            # check if it has 4 distinct factors
            if len(pFactors) == nConsec:
                # if true, continue
                n += 1
            # if not, break and make startN and n = n+1
            else:
                startN = n + 1
                n = startN
                break
        if n == startN + nConsec:
            return startN
        

print(nConsecDistinctPrimeFactors(4))
