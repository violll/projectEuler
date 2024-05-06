def getNumberSpiralSum(maxW):
    tot = 1
    res = 1

    for w in range(1,maxW,2):
        for _ in range(4):
            tot += w+1
            res += tot

    return res

print(getNumberSpiralSum(1001))