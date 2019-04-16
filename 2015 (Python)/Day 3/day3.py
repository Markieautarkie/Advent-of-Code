import os

# open the file and read the input
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = f.read()
f.close()

# Set this to true for the first star
star = False

# updates the given position
def UpdatePos(pos, sign):
    return tuple([a + b for a, b in zip(pos, coordsDict[sign])])

# a dictionary to get the coordinate increase depending on the sign
coordsDict = {'^' : (0, 1), '>' : (1, 0), 'v' : (0, -1), '<' : (-1, 0)}

# initialize the starting position and a set to keep all the visited coords in
currSantaPos, currRobotPos = (0, 0), (0, 0)
visitedPos = {currSantaPos}

# loop over the input, update the current position, add to visited list if not visited before
for index, c in enumerate(input):
    if index % 2 == 0 and not star:
        currSantaPos = UpdatePos(currSantaPos, c)
        if currSantaPos not in visitedPos:
            visitedPos.add(currSantaPos)
    else:
        currRobotPos = UpdatePos(currRobotPos, c)
        if currRobotPos not in visitedPos:
            visitedPos.add(currRobotPos)

# print star 
print("The amount of houses santa vistied is: " + str(len(visitedPos)))