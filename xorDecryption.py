import collections
import operator
import string

def decryptedTxt(txt):
    for c1 in string.ascii_lowercase:
        for c2 in string.ascii_lowercase:
            for c3 in string.ascii_lowercase:
                testStr = ""
                for i in range(0, len(txt)-2, 3):
                    testStr += chr(int(txt[i]) ^ ord(c1)) + chr(int(txt[i+1]) ^ ord(c2)) + chr(int(txt[i+2]) ^ ord(c3))
                if " and " in testStr and " the " in testStr and " be " in testStr and " to " in testStr and " of " in testStr: 
                    print([c1, c2, c3], "\t", testStr)
                    return testStr


def getASCIIsum(file):
    f = open(file, "r")
    txt = f.readline().split(",")
    txt = decryptedTxt(txt)

    res = 0

    for letter in txt:
        res += ord(letter)

    return res
    

print(getASCIIsum("0059_cipher.txt"))
