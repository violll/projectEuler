# recursive solution
def sumFib(num1, num2, max, sum):
    if num1 >= max or num1+num2 >= max:
        return sum
    elif (num1+num2)%2==0:
        return sumFib(num2, num1+num2, max, sum+num1+num2)
    else:
        return sumFib(num2,num1+num2, max, sum)

print(sumFib(1,2,4000000,2))

# non-recursive solution
def fibLst(num1, num2, max):
    lst = []
    if num1%2==0: lst.append(num1)
    if num2%2==0: lst.append(num2)
    while num1 < max and num1+num2<max:
        newNum = num1+num2
        if newNum%2==0: lst.append(newNum)
        num1, num2 = num2, newNum
    return lst

print(sum(fibLst(1,2,4000000)))