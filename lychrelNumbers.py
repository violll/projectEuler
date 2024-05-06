def isPalindrome(n):
    lstN = list(str(n))
    if list(reversed(lstN)) == lstN and len(lstN) > 1: return True
    else: return False

def lychrelNumbers(maxN, maxPerm):
    res = 0

    for i in range(1, maxN):
        originalN = i
        for _ in range(maxPerm):
            i += int(str(i)[::-1])
            if isPalindrome(i): 
                print(originalN, i, sep="\t")
                res += 1
                break
    
    return maxN - 1 - res

print(lychrelNumbers(10000, 50))