# from usefulFcns import 

def getTriangleLst(xth):
    res = set()
    for i in range(1,xth+1):
        res.add((i * (i+1))//2)
    return res

def getWordScore(word):
    res = 0

    for letter in word:
        res += ord(letter) - 64

    return res

def getCodedTriangleNumber(f):
    tNums = 0
    tLst = getTriangleLst(26*10)
    f = open(f, "r")
    text = f.read().replace('"', "").split(",")
    for word in text:
        testScore = getWordScore(word)
        if testScore in tLst:
            tNums += 1
    
    return tNums

# print(getCodedTriangleNumber("p042_words.txt"))