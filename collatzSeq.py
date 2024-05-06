def even(n):
    return n//2

def odd(n):
    return 3*n + 1

def longestCollatzSeq(maxNum):
    numTerms = 0
    num = 1

    for i in range(1, maxNum):
        tempNumTerms = len(getCollatzSeq(i, seq=[]))
        if tempNumTerms > numTerms: 
            numTerms = tempNumTerms
            num = i
    
    return num

def getCollatzSeq(num, seq=[]):
    seq.append(num)
    if num == 1: 
        return seq
    elif num%2 == 0:
        return getCollatzSeq(even(num), seq)
    else:
        return getCollatzSeq(odd(num), seq)

print(longestCollatzSeq(1000000))