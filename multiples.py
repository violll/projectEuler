# non-recursive solution
def getSum(maxNum):
    sum = 0
    for i in range(1, maxNum):
        if isMultiple(3,i) or isMultiple(5,i):
            sum += i
    return sum

def isMultiple(multiple, num):
    return (num%multiple==0)

print(getSum(1000))

# list comprehension
print(sum([i for i in range(1000) if i%3==0 or i%5==0]))