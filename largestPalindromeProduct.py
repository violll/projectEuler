def getLargestPalindrome(min, max):
    maxPal = 0
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            testNum = i*j
            if checkPalindrome(testNum) and testNum>maxPal: 
                maxPal = testNum
    return maxPal

def checkPalindrome(num):
    strNum = str(num)
    reversed = strNum[::-1]
    
    if strNum == reversed: return True
    else: return False 

# print(getLargestPalindrome(99, 999))

