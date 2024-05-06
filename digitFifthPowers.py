def getFifthPowerSum(num):
    res = 0
    while num >= 1:
        res += int(num%10)**5
        num /= 10
    return res

def digitFifthPowers(max):
    res = 0

    for i in range(2, max):
        temp = getFifthPowerSum(i)
        if i == temp: res += i
        if temp > max: break
    
    return res

print(digitFifthPowers(1000000))