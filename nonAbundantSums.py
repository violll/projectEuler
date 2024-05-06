from amicableNumbers import getDivisors

def isPerfectNumber(num):
    divisors = getDivisors(num)
    s = sum(divisors)
    if s == num: return "Perfect"
    elif s < num: return "Deficient"
    else: return "Abundant"

def getAbundant(max):
    res = []
    num = 12

    while num < max:
        if isPerfectNumber(num) == "Abundant":
            res.append(num)
        num += 1
    
    return res

def getAbundantSums(max):
    abundantNums = getAbundant(max)
    res = set()
    
    for num1 in abundantNums:
        for num2 in abundantNums[abundantNums.index(num1):]:
            if num1+num2 < max:
                res.add(num1+num2)

    return sorted(list(res))

def getNonAbundant(max):
    abundantSums = getAbundantSums(max)
    testNums = [i for i in range(1,max)]
    res = [i for i in testNums if i not in abundantSums]
    return sum(res)


print(getNonAbundant(28124))
