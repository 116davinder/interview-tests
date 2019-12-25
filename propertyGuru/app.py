from itertools import permutations

a = [[0,0,0,0,0],
     [0,1,1,1,0],
     [0,0,0,0,0],
     [1,1,1,0,0],
     [0,1,0,0,0]]

activePointList = []

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == 1:
            activePointList.append([i,j])

# points are collinear if area of triangle is zero
def collinear(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    # print(f"area of triangle:\t{a}")
    if a == 0:
        return True
    else:
        return False

battleShipFoundList = []

if len(activePointList) >= 3:
    allLocations = list(permutations(activePointList, r=3))
    # print(allLocations)
    for i in allLocations:
        x1 = list(i)[0][0]
        y1 = list(i)[0][1]
        x2 = list(i)[1][0]
        y2 = list(i)[1][1]
        x3 = list(i)[2][0]
        y3 = list(i)[2][1]
        if collinear(x1, y1, x2, y2, x3, y3):
            battleShipFoundList.append(list(i))
            # print(f"BattleShip Location is: {list(i)}")
else:
    print("No Battle Ship Found")

# remove all duplicates from battleShipFoundList
for ship in battleShipFoundList:
    pList = list(permutations(ship, r=3))
    print(len(pList))
    for j in range(1,len(pList)):
        battleShipFoundList.remove(list(list(pList)[j]))

print(battleShipFoundList)
