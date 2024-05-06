def getNameScores(f):
    f = open(f, "r")
    text = sorted(f.read().replace('"', "").split(","))
    score = 0
    for i in range(len(text)):
        name = text[i]
        tempScore = 0
        for letter in name:
            tempScore += ord(letter) - 64
        tempScore *= i+1
        score += tempScore
    return score

print(getNameScores("p022_names.txt"))