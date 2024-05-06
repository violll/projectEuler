from largestPrimeFactor import isPrime

def spiralPrimes(minRatio):
    sideLength = 1
    nDiag = 1
    primeDiag = 0
    n = 1
    ratio = 1

    while ratio > minRatio:
        sideLength += 2
        for _ in range(4):
            n += sideLength-1
            nDiag += 1
            if isPrime(n): primeDiag += 1
        ratio = primeDiag/nDiag
        if ratio < minRatio: return sideLength


print(spiralPrimes(0.1))