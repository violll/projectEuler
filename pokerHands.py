from functools import cmp_to_key
from collections import Counter

def sortCards(card1, card2):
    val1, _ = card1[0], card1[1]
    val2, _ = card2[0], card2[1]

    cardDict = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
    if val1 in cardDict: val1 = cardDict[val1]
    if val2 in cardDict: val2 = cardDict[val2]

    val1 = int(val1)
    val2 = int(val2)

    if val1 < val2: return -1
    elif val1 > val2: return 1
    else: return 0

def pokerHands(file):
    f = open(file, "r")
    lines = f.readlines()
    p1Score = 0
    for line in lines:
        handsLst = line.split(" ")
        p1 = sorted(handsLst[:5], key=cmp_to_key(sortCards))
        p2 = sorted(handsLst[5:], key=cmp_to_key(sortCards))

        p1Hand, p1Value = getHand(p1)
        p2Hand, p2Value = getHand(p2)

        if p1Hand > p2Hand: 
            p1Score += 1
        
        elif p1Hand == p2Hand:
            # no comparison necessary for a royal flush, two of them would make a tie
            # straight flush: compare the highest card from each (only one comp is necessary since they're consecutive)
            if p1Hand == 8 and p1Value[-1] > p2Value[-1]:
                p1Score += 1                
            
            # four of a kind & full house
            elif p1Hand == 7 or p1Hand == 6:
                if Counter(p1Value).most_common()[0][0] > Counter(p2Value).most_common()[0][0]:
                    p1Score += 1
                elif Counter(p1Value).most_common()[0][0] == Counter(p2Value).most_common()[0][0] and Counter(p1Value).most_common()[1][0] > Counter(p2Value).most_common()[1][0]:
                        p1Score += 1

            # flush & high card: comp highest card etc
            elif p1Hand == 5 or p1Hand == 0:
                i = len(p1Value) - 1
                while True:
                    if p1Value[i] > p2Value[i]:
                        p1Score += 1
                        break
                    elif p1Value[i] < p2Value[i]:
                        break

                    i -= 1

            # straight: comp highest card
            elif p1Hand == 4 and p1Value[-1] > p2Value[-1]:
                p1Score += 1

            # 3 pairs & 1 pair: comp trio first, then highest card etc
            elif p1Hand == 3 or p1Hand == 1:
                if Counter(p1Value).most_common()[0][0] > Counter(p2Value).most_common()[0][0]:
                    p1Score += 1
                elif Counter(p1Value).most_common()[0][0] < Counter(p2Value).most_common()[0][0]:
                    continue
                else:
                    i = len(p1Value) - 1
                    while True:
                        if p1Value[i] != Counter(p1Value).most_common()[0][0] and p1Value[i] > p2Value[i]:
                            p1Score += 1
                            break
                        elif p1Value[i] < p2Value[i]:
                            break
                            
                        i -= 1

            # 2: there shouldn't be a comparison here b/c the two pairs are ambiguous? or would it be the highest of the two pairs
            elif p1Hand == 2:
                maxPair1 = sorted([Counter(p1Value).most_common()[0][0], Counter(p1Value).most_common()[1][0]])
                maxPair2 = sorted([Counter(p2Value).most_common()[0][0], Counter(p2Value).most_common()[1][0]])
                
                if maxPair1[0] > maxPair2[0]: 
                    p1Score += 1
                elif maxPair1[0] == maxPair2[0]:
                    if maxPair1[1] > maxPair2[1]: 
                        p1Score += 1
                    elif maxPair1[1] == maxPair2[1]:
                        i = len(p1Value) - 1
                        while True:
                            if p1Value[i] not in maxPair1 and p2Value[i] not in maxPair2 and p1Value[i] > p2Value[i]:
                                p1Score += 1
                                break
                            elif p1Value[i] < p2Value[i]:
                                break
                                
                            i -= 1
            
        else:
            continue

    return p1Score
        
def getHand(cards):
    hands = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
    cardDict = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
    
    value = [int(cards[i][0]) if cards[i][0].isnumeric() else int(cardDict[cards[i][0]]) for i in range(len(cards))]
    suit = [cards[i][1] for i in range(len(cards))]

    # Royal Flush
    if set(value) == set(["T", "J", "Q", "K", "A"]) and suit.count(suit[0]) == 5:
        return hands.index("Royal Flush"), value

    # Straight Flush
    elif value == [value[0] + i for i in range(len(value))] and suit.count(suit[0]) == 5:
        return hands.index("Straight Flush"), value
    
    # Four of a Kind
    elif Counter(value).most_common()[0][1] >= 4:
        return hands.index("Four of a Kind"), value

    # Full House
    elif Counter(value).most_common()[0][1] == 3 and Counter(value).most_common()[1][1] == 2:
        return hands.index("Full House"), value
    
    # Flush 
    elif suit.count(suit[0]) == 5:
        return hands.index("Flush"), value
    
    # Straight
    elif value == [value[0] + i for i in range(len(value))]:
        return hands.index("Straight"), value
    
    # Three of a Kind 
    elif Counter(value).most_common()[0][1] >= 3:
        return hands.index("Three of a Kind"), value
    
    # Two Pairs
    elif Counter(value).most_common()[0][1] >= 2 and Counter(value).most_common()[1][1] >= 2:
        return hands.index("Two Pairs"), value

    # One Pair
    elif Counter(value).most_common()[0][1] >= 2 and Counter(value).most_common()[1][1] == 1:
        return hands.index("One Pair"), value

    # High Card
    else:
        return hands.index("High Card"), value

print(pokerHands("0054_poker.txt"))

