

def distinctPowers(aRange, bRange):
    res = set()
    for a in aRange:
        for b in bRange:
            if a**b not in res: res.add(a**b)
    return len(res)

print(distinctPowers(range(2,101), range(2,101)))