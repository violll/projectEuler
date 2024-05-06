import numpy as np

def P(n):
    return n * (3*n - 1) / 2

def D(j, k):
    return abs(k-j)

def solvePoly(n):
    roots = np.roots([3, -1, -n*2])
    for r in roots:
        if int(r) == r and r > 0:
            return int(r)

def optimizePairSum():
    pentagonalNums = []
    diff = 10**10
    i = 0
    while True:
        i += 1
        s = P(i)
        pentagonalNums.append(int(s))

        for n1 in pentagonalNums:
            if n1 < s//2:
                n2 = int(s - n1)
                if int(n2) != 0 and n1 != n2 and (n2 in pentagonalNums or solvePoly(n2) != None):
                    d = D(n1, n2)
                    if d in pentagonalNums or solvePoly(d) != None:
                        if d < diff: diff = d
                        return diff

# print(optimizePairSum())