from math import factorial

def getPaths(gridSize, possibleDirs):
    moves = gridSize[0] * 2
    return factorial(moves)//(factorial(moves//len(possibleDirs))**2)

print(getPaths([2,2], [[1,0], [0,1]]))