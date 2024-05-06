import copy
def triNum(n):
    return n * (n + 1) / 2

def squareNum(n):
    return n ** 2

def pentNum(n):
    return n * (3 * n - 1) / 2

def hexNum(n):
    return n * (2 * n - 1)

def heptNum(n):
    return n * (5 * n - 3) / 2

def octNum(n):
    return n * (3 * n - 2)

def cyclicalFigurateNumbers():
    triNums = [triNum(n) for n in range(1,9999) if triNum(n) >= 1000 and triNum(n) < 10000]
    squareNums = [squareNum(n) for n in range(1,9999) if squareNum(n) >= 1000 and squareNum(n) < 10000]
    pentNums = [pentNum(n) for n in range(1,9999) if pentNum(n) >= 1000 and pentNum(n) < 10000]
    hexNums = [hexNum(n) for n in range(1,9999) if hexNum(n) >= 1000 and hexNum(n) < 10000]
    heptNums = [heptNum(n) for n in range(1,9999) if heptNum(n) >= 1000 and heptNum(n) < 10000]
    octNums = [octNum(n) for n in range(1,9999) if octNum(n) >= 1000 and octNum(n) < 10000]

    for n1 in range(1000, 10000):
        properties = [0 for _ in range(6)]

        # this sets the first number
        nCheck = isFigurate(n1, triNums, squareNums, pentNums, hexNums, heptNums, octNums)
        if nCheck != False:
            properties = [properties[i] + nCheck[i] for i in range(len(properties))]
            nums = [n1]
            print(n1)

            while len(nums) != 6:
                startDigits = str(nums[-1])[2:]
                n2 = int(startDigits) * 100
                if startDigits[0] != "0":
                    while True:
                        print(" " * len(nums), n2)

                        if str(n2)[:2] == startDigits:
                            res = isFigurate(n2, triNums, squareNums, pentNums, hexNums, heptNums, octNums)
                            if res != False and str(n2)[2] != "0":
                                tempProp = [properties[i] + res[i] for i in range(len(properties))]
                                if 2 not in tempProp:
                                    print(n2, res)
                                    nums.append(n2)
                                    properties = copy.deepcopy(tempProp)
                                    break
                        else: 
                            n2 += 1
                            break
                        n2 += 1      
                else: break  

        # # change this into recursive statement
        # nCheck = isFigurate(n1, triNums, squareNums, pentNums, hexNums, heptNums, octNums)
        # if nCheck != False:
        #     properties = [properties[i] + nCheck[i] for i in range(len(properties))]

# def cycFigNums(properties, nums, triNums, squareNums, pentNums, hexNums, heptNums, octNums):
#     if 0 not in properties: return nums
#     elif 2 in properties: return nums
#     else:
#         pass
#     pass

def isFigurate(n, triNums, squareNums, pentNums, hexNums, heptNums, octNums):
    res = [0 for _ in range(6)]
    if n in triNums: res[0] += 1
    if n in squareNums: res[1] += 1
    if n in pentNums: res[2] += 1
    if n in hexNums: res[3] += 1
    if n in heptNums: res[4] += 1
    if n in octNums: res[5] += 1

    if sum(res) != 1: return False
    else: return res

# print(cyclicalFigurateNumbers())

# triNums = [triNum(n) for n in range(1,9999) if triNum(n) >= 1000 and triNum(n) < 10000]
# squareNums = [squareNum(n) for n in range(1,9999) if squareNum(n) >= 1000 and squareNum(n) < 10000]
# pentNums = [pentNum(n) for n in range(1,9999) if pentNum(n) >= 1000 and pentNum(n) < 10000]
# hexNums = [hexNum(n) for n in range(1,9999) if hexNum(n) >= 1000 and hexNum(n) < 10000]
# heptNums = [heptNum(n) for n in range(1,9999) if heptNum(n) >= 1000 and heptNum(n) < 10000]
# octNums = [octNum(n) for n in range(1,9999) if octNum(n) >= 1000 and octNum(n) < 10000]
# nums = [5500]
# n = 5500
# while True:
#     if str(n)[2] != "0" and int(str(n)[:2]) == int(str(nums[-1])[:2]):
#         res = isFigurate(n, triNums, squareNums, pentNums, hexNums, heptNums, octNums)
#         if res != False:
#             print(n, res)
#             break
#     n += 1