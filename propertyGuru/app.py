from itertools import permutations

a = [[0,0,0,0,0],
     [0,1,1,1,0],
     [0,0,0,0,0],
     [1,0,0,0,0],
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

if len(activePointList) >= 3:
    allPossibleLocations = list(permutations(activePointList, 3))
    for i in allPossibleLocations:
        x1 = list(i)[0][0]
        y1 = list(i)[0][1]
        x2 = list(i)[1][0]
        y2 = list(i)[1][1]
        x3 = list(i)[2][0]
        y3 = list(i)[2][1]
        if collinear(x1, y1, x2, y2, x3, y3):
            print(f"BattleShip Location is: {list(i)}")
else:
    print("No Battle Ship Found")
