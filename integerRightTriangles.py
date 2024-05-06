def pythagoreanTriplet():
    p = 1000
    maxP = 0
    maxSols = 0

    for p in range(8,1001):
        numSols = 0
        print(p)
        for a in range(1,p//2+1):
            for b in range(a,(p-a)//2+1):
                c = p - a - b
                # if c <= b: break
                # print('\t',a,b,c)


                if a**2 + b**2 == c**2:
                    print('\t',a,b,c)
                    numSols += 1
        
        if numSols > maxSols:
            maxSols = numSols
            maxP = p

        p += 1
    
    return maxP

print(pythagoreanTriplet())