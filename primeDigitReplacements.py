import itertools

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def primeDigitReplacement2(nFamily):
    pow = 1
    possibleEndDigits = [1, 3, 7, 9]
    primes = set()
    

    while True:
        # need to get each unique possible number and then permutate the replacements
        # iterates through each possible number that a family could be based around
        powNums = []
        for endDigit in possibleEndDigits:
            for midDigit in range(10**(pow-1),10**(pow)):
                num = midDigit * 10 + endDigit
                if num in primes or isPrime(num):
                    primes.add(num)
                    powNums.append(num)
        
        for num in sorted(powNums):
            replacementInd = getReplacementInd(pow)
            res, primes = testReplacement(num, replacementInd, primes, nFamily)
            if type(res) == int: return res
                
        pow += 1
        
def getReplacementInd(pow):
    potentialDigitIndex = [str(i) for i in range(pow)]
    res = []

    for i in range(1, pow+1):
        perms = list(itertools.combinations(potentialDigitIndex, i))
        for item in perms: res.append(item)
    
    return res

def testReplacement(num, replacementInd, primes, nFamily):
    for idx in replacementInd:
        numList = list(map(int,list(str(num))))
        primeCount = 0
        family = []

        for i in range(10):
            for id in idx: numList[int(id)] = i
            familyMember = int("".join(map(str,numList)))

            if len(str(familyMember)) == len(str(num)) and (familyMember in primes or isPrime(familyMember)):
                primes.add(familyMember)
                family.append(familyMember)
                primeCount += 1

        if primeCount == nFamily: return min(family), primes

    return False, primes

print(primeDigitReplacement2(6))
print(primeDigitReplacement2(7))
print(primeDigitReplacement2(8))
