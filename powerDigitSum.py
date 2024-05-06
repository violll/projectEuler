def powerDigitSum(power):
    res = 2**power
    return digitSum(res)

def digitSum(num):
    digitSum = 0
    while num >= 1:
        digitSum += int(num%10)
        num = num // 10
    return digitSum

# print(powerDigitSum(1000))