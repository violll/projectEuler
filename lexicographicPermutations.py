from math import factorial

nums = [i for i in range(0, 10)]

def reducePerms(nums, max):
    possiblePerms = [factorial(len(nums)-num) for num in nums]

    # the permutation of each number can be divided equally
    totalPerms = 0
    startPerms = 0
    newNums = [None for _ in range(len(nums))]
    for i in range(len(nums)):
        perms = possiblePerms[i]
        unknownDigits = len(nums) - i
        permsPerNum = perms / unknownDigits
        for j in [k for k in nums if k not in newNums]:
            totalPerms += permsPerNum

            if totalPerms >= max: 
                newNums[i] = j
                startPerms = totalPerms - permsPerNum
                break

        totalPerms = startPerms

        if startPerms == max: break

    return newNums


print(reducePerms(nums, 1000000))