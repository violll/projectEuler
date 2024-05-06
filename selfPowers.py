def selfPowersSum(maxN):
    s = 0
    n = 1
    while n <= maxN:
        square = str(n**n)
        
        if len(square) < 10: 
            truncSquare = square
        else:
            truncSquare = square[-10:]

        s += int(truncSquare)
        n += 1
    return int(str(s)[-10:])

print(selfPowersSum(1000))
