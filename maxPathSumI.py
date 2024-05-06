triangle = "75\n95 64\n17 47 82\n18 35 87 10\n20 04 82 47 65\n19 01 23 75 03 34\n88 02 77 73 07 63 67\n99 65 04 28 06 16 70 92\n41 41 26 56 83 40 80 70 33\n41 48 72 33 47 32 37 16 94 29\n53 71 44 65 25 43 91 52 97 51 14\n70 11 33 28 77 73 17 78 39 68 17 57\n91 71 52 38 17 14 91 43 58 50 27 29 48\n63 66 04 68 89 53 67 30 73 16 69 87 40 31\n04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
lstTriangle = [row.split(" ") for row in triangle.split("\n")]
lstTriangle = [[int(num) for num in subLst] for subLst in lstTriangle]

triangle2 = [[3],
             [7, 4],
             [2, 4, 6],
             [8, 5, 9, 3],
            ]

def getTree(tree, loc, cost, costs):
    x, y = loc
    cost += tree[x][y]
    if x == len(tree) - 1: 
        costs.append(cost)
        return cost
    else:
        getTree(tree, [x+1, y], cost, costs)
        getTree(tree, [x+1, y+1], cost, costs)
        return max(costs)

print(getTree(lstTriangle, [0,0], 0, []))

# irrelevant algorithm
# def getNodes(triangle):
#     nodes = []
#     for i in range(len(triangle)):
#         for j in range(len(triangle[i])):
#             nodes.append([i,j])
#     return nodes

# def getPath(triangle):
#     nodes = getNodes(triangle)
#     currNode = nodes[0]
#     nodes.remove(currNode)

#     cost = triangle[currNode[0]][currNode[0]]
#     path = [currNode]

#     for _ in range(len(triangle)-1):
#         candidate1 = [currNode[0]+1, currNode[1]]
#         candidate2 = [currNode[0]+1, currNode[1]+1]
#         cost1 = triangle[candidate1[0]][candidate1[1]]
#         cost2 = triangle[candidate2[0]][candidate2[1]]
#         if cost1 > cost2:
#             cost += cost1
#             path.append(candidate1)
#             currNode = candidate1
#         else:
#             cost += cost2
#             path.append(candidate2)
#             currNode = candidate2
    
#     return cost