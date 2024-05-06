def getDiff(min, max):
    sumSquares = sum([i**2 for i in range(min, max+1)])
    squaredSum = sum([i for i in range(min, max+1)])**2
    return abs(sumSquares-squaredSum)

print(getDiff(1,100))