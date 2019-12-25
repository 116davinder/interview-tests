from itertools import permutations

a = [[1,0,0,0,0],
     [0,1,1,1,0],
     [0,0,1,0,1],
     [1,1,0,0,1],
     [1,0,0,0,0]]

activePointList = []
battleShipFoundList = []
toBeRemovedShipAfterAdjacentPointTest = []
overLappingPointShipList = []
diagonalPointShipList = []

def printBattleShiplocation(locationList):
    for ship in locationList:
        print(f"BattleShip Location is: {ship}")

# find all active points on map
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == 1:
            activePointList.append([i,j])

# points are collinear if area of triangle is zero
def collinearTest(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    # print(f"area of triangle:\t{a}")
    if a == 0:
        return True
    else:
        return False

# if 2d points are less than 3 means no ship is there.
if len(activePointList) >= 3:
    allLocations = list(permutations(activePointList, r=3))
    for i in allLocations:
        x1 = list(i)[0][0]
        y1 = list(i)[0][1]
        x2 = list(i)[1][0]
        y2 = list(i)[1][1]
        x3 = list(i)[2][0]
        y3 = list(i)[2][1]
        if collinearTest(x1, y1, x2, y2, x3, y3):
            battleShipFoundList.append(list(i))
else:
    print("No Battle Ship Found")
    exit

# remove all duplicates from battleShipFoundList
for ship in battleShipFoundList:
    pList = list(permutations(ship, r=3))
    for j in range(1,len(pList)):
        # print(list(list(pList)[j]))
        battleShipFoundList.remove(list(list(pList)[j]))

# remove ships points where points are collinear but not adjacent
def adjacentTest(x1, y1, x2, y2, x3, y3):
    return (abs(x1 - x2) == abs(x2 - x3) and 
            abs(y1 - y2) == abs(y2 - y3) and
            abs(x1 - x2) in (0,1) and
            abs(x2 - x3) in (0,1) and
            abs(y1 - y2) in (0,1) and
            abs(y2 - y3) in (0,1)
    )

# add battleship location to toBeRemovedShipAfterAdjacentPointTest
# list if adjacentTest test fails
for ship in battleShipFoundList:
    x1,y1,x2,y2,x3,y3 = ship[0][0], ship[0][1], ship[1][0], ship[1][1], ship[2][0], ship[2][1]
    if not adjacentTest(x1, y1, x2, y2, x3, y3):
        # print(f"removed ship: {ship}")
        toBeRemovedShipAfterAdjacentPointTest.append(ship)

# remove all ships from main ship list which failed adjacentTest
for ship in toBeRemovedShipAfterAdjacentPointTest:
    battleShipFoundList.remove(ship)

# diagonal ship edge case removal
def diagonalShipTest(x1, y1, x2, y2, x3, y3):
    return (
        abs(x1 - x2) == abs(x2 - x3) == 1 and
        abs(y1 - y2) == abs(y2 - y3) == 1
    )

# add battleship location to diagonalPointShipList
# list if diagonalShipTest test fails
for ship in battleShipFoundList:
    x1,y1,x2,y2,x3,y3 = ship[0][0], ship[0][1], ship[1][0], ship[1][1], ship[2][0], ship[2][1]
    if diagonalShipTest(x1, y1, x2, y2, x3, y3):
        # print(f"removed ship: {ship}")
        diagonalPointShipList.append(ship)

# remove all ships from main ship list which failed diagonalShipTest
for ship in diagonalPointShipList:
    battleShipFoundList.remove(ship)

# Print ships location
printBattleShiplocation(battleShipFoundList)
