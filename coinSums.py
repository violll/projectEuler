import copy

def baseCase(perms, permDict, permLst):
    permLst.append(permDict)
    perms += 1
    return perms

def getCoinSums(target, perms, currency, i, permDict, permLst):
    if target == 0:
        perms = baseCase(perms, permDict, permLst)

    else: 
        remainingCurrency = [c for c in currency if c <= target]
        coin = remainingCurrency[0]
        if i == 0: permDict = {}
        tempPermDict = copy.deepcopy(permDict)
        currTarget = target

        tempCurrency = copy.deepcopy(remainingCurrency)

        if coin != 1: 
            tempCurrency.remove(coin)
            perms = getCoinSums(currTarget, perms, tempCurrency, i+1, tempPermDict, permLst)

        while currTarget - coin >= 0:
            if coin == 1:
                tempPermDict[coin] = target
                perms = baseCase(perms, tempPermDict, permLst)
                break

            else:
                if coin in tempCurrency: 
                    tempCurrency.remove(coin)
                
                if coin in tempPermDict: tempPermDict[coin] += 1
                else: tempPermDict[coin] = 1

                perms = getCoinSums(currTarget-coin, perms, tempCurrency, i+1, tempPermDict, permLst)
                currTarget -= coin

    return perms


print(getCoinSums(200, 0, [200, 100, 50, 20, 10, 5, 2, 1], 0, {}, []))