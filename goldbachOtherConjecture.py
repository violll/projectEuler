def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True


def otherConjecture():
    n = 2
    while True:
        if not isPrime(n) and n % 2 != 0:
            s = 1
            while True:
                if 2 * s**2 >= n: 
                    return n

                testN = n - 2 * s**2
                if isPrime(testN): break
                s += 1
        n += 1

print(otherConjecture())