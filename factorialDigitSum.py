from powerDigitSum import digitSum

def getFactorial(num):
    if num == 1:
        return 1
    else: return num * getFactorial(num-1)

def factorialDigitSum(num):
    factorial = getFactorial(num)
    return digitSum(factorial)

print(factorialDigitSum(100))