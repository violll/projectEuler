from largestPrimeFactor import isPrime
import copy

def getPanDigitalNums(numD, curr, res, nums, i):
    if len(curr) == numD:
        res.append(curr) 
        return res
    else:
        remainingNums = [str(num) for num in nums if num not in curr]
        for num in remainingNums:
            tempCurr = copy.deepcopy(curr)
            tempCurr.append(num)
            tempNums = copy.deepcopy(remainingNums)
            tempNums.remove(num)
            res = getPanDigitalNums(numD, tempCurr, res, tempNums, i +1)

        return res

def pandigitalPrime(maxD):
    maxNum = 0

    for i in range(maxD, 0, -1):
        nums = getPanDigitalNums(i, [], [], [str(j) for j in range(1, i+1)], 0)
        
        for num in nums[::-1]:
            num = "".join(num)
            if isPrime(int(num)):
                return num
    
    return maxNum


# print(pandigitalPrime(9))