import os

# open the file and read the input
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = f.read()
f.close()

# a dictionary to get the coordinate increase depending on the sign
coordsDict = {'^' : (0, 1), '>' : (1, 0), 'v' : (0, -1), '<' : (-1, 0)}

# initialize the starting position and a set to keep all the visited coords in
currPos = (0, 0)
visitedPos = {currPos}

# loop over the input, update the current position, add to visited list if not visited before
for c in input:
    currPos = tuple([a + b for a, b in zip(currPos, coordsDict[c])])
    if currPos not in visitedPos:
        visitedPos.add(currPos)

# print star 1
print("The amount of houses santa vistied is: " + str(len(visitedPos)))

