import os

# reads the file and store it in a variable
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = f.read()
f.close()

# first star - count the symbols and subtract them
endFloor = input.count('(') - input.count(')')
print("Santa ends up at floor: " + str(endFloor))

# second star - update floor number and watch when floor < 0
floor = 0
currChar = 0
for c in input:
    floor += 1 if c == '(' else -1
    currChar += 1
    if floor < 0:
        print("The first time santa enters the basement is: " + str(currChar))
        break