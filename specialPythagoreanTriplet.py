def pythagoreanTriplet():
    for a in range(1,1001):
        for b in range(a+1,1000):
            c = 1000 - a - b
            if a < b < c and a**2 + b**2 == c**2:
                    return(a,b,c, a*b*c)
    
print(pythagoreanTriplet())