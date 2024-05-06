from num2words import num2words

def numberLetterCounts(min, max):
    sum = 0
    for i in range(min, max+1):
        sum += len(num2words(i)   \
            .replace("-", "")       \
            .replace(" ", ""))
    
    return sum

print(numberLetterCounts(1,1000))
