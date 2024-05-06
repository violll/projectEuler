def digitCount(n):
    return len(str(n))

def squareRootConvergents(nIters):
    res = 0

    for i in range(nIters):
        s2num = 2
        s2den = 5

        if i == 0:
            snum = 3
            sden = 2

        else:
            snum = s2num
            sden = s2den
            for _ in range(i-1):
                snum, sden = sden, 2*sden+snum

            snum += sden

        if digitCount(snum) > digitCount(sden): res += 1

    return res
        
print(squareRootConvergents(1000))