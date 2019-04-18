import os

# read and split the input
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = [s.split() for s in f.readlines()]
f.close()

# setup the grid
d = 1000
grid = [[0 for x in range(d)] for y in range(d)]

# converts coordinates to workable positions
def CoordToPos(coord1, coord2):
    pos1 = [int(n) for n in coord1.split(',')]
    pos2 = [int(n) for n in coord2.split(',')]
    return pos1, pos2

# switches light depending on mode m
# simply count for the corresponding mode
def Mode(coord1, coord2, m):
    pos1, pos2 = CoordToPos(coord1, coord2)
    for x in range(pos1[0], pos2[0] + 1):
        for y in range(pos1[1], pos2[1] + 1):
            grid[x][y] = max(grid[x][y] + m, 0)

# loop over all the input strings
for s in input:
    if "toggle" in s:
        Mode(s[1], s[3], 2)
    else:
        Mode(s[2], s[4], 1) if "on" in s else Mode(s[2], s[4], -1)

# update the brightness variable
brightness = 0
for x in range(d):
    for y in range(d):
        brightness += grid[x][y]

# print the total brightness
print(brightness)