import math

def choose(n, k):
    return (math.factorial(n)) / (math.factorial(k)*math.factorial(n-k))

def combinatoricSelections(minN, maxN, minVal):
    res = 0
    for n in range(minN, maxN+1):
        for k in range(1,n):
            # the commented out line does the same thing, just an alternate method of solving that uses a prewritten function in the math package
            # if math.comb(n, k) > minVal: res += 1
            if choose(n, k) > minVal: res += 1
    
    return res

print(combinatoricSelections(1, 100, 1000000))