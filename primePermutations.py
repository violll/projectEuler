import itertools

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def primePermutations():
    # set minN as this number because the first set of three numbers begins with 1487
    minN = 1488
    maxN = 9999
    n = minN

    while True:
        perms = sorted(list(set([int("".join(i)) for i in list(itertools.permutations(list(str(n))))])))
        validPerms = [perm for perm in perms if perm >= minN and perm <= maxN and isPrime(perm)]

        if len(validPerms) < 3:
            n += 1

        elif len(validPerms) == 3:
            if validPerms[1] - validPerms[0] == validPerms[2] - validPerms[0]:
                return "{}{}{}".format(n1,n2,n3)
            else: 
                n += 1

        else:
            allValidPerms = list(itertools.combinations(validPerms, 3))
            for validPerm in allValidPerms:
                n1, n2, n3 = validPerm
                if n1 < n2 and n2 < n3 and n2 - n1 == n3 - n2:
                    return "{}{}{}".format(n1,n2,n3)
            n += 1
        
print(primePermutations())