def getChampernowneConst():
    i = 1
    frac = ""
    res = 1

    while len(frac) < 1000000:
        frac += str(i)
        i += 1
    
    for j in [10**i for i in range(7)]:
        res *= int(frac[j-1])

    return res

print(getChampernowneConst())