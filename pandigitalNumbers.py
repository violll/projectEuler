def getPandigital(n):
    match = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    res = ""
    i = 1
    while True:
        res += str(n * i)
        i += 1
        if len(res) == 9:
            break
        if len(res) > 9: return False, res

    if set(int(n) for n in list(res)) == match: return True, res
    else: return False, res

def getMaxPandigitalMultiple():
    maxN = 0

    i = 1
    while i < 10000:
        check, res = getPandigital(i)
        if check and int(res) > maxN:
            maxN = int(res)
        i += 1
    
    return maxN


# print(getMaxPandigitalMultiple())