from largestPalindromeProduct import checkPalindrome

def getDBPalindromes(max):
    nums = set()
    for n in range(max):
        bN = bin(n)[2:]
        if checkPalindrome(n) and checkPalindrome(int(bN)):
            nums.add(n)
    return sum(nums)

print(getDBPalindromes(1000000))