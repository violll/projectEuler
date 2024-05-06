import numpy as np
import math

def roundHalfUp(n):
    return math.floor(n + 0.5)

def T(n):
    return n * (n + 1) // 2

def P(n):
    return n * (3*n - 1) // 2

def H(n):
    return n * (2*n - 1)

def solvePoly(rootsLst):
    roots = np.roots(rootsLst)
    for r in roots:
        if r > 0 and math.isclose(roundHalfUp(r), r, rel_tol=1e-9):
            return roundHalfUp(r)
    return None

def isAllThree():
    n = 1
    while True:
        num = H(n)
        isPent = solvePoly([3, -1, -2*num])
        if isPent and num != 1 and num != 40755: return num

        n += 1
        
print(isAllThree())