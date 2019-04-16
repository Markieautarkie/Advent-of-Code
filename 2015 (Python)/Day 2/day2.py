import os

# read, strip and split the input
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = [s.rstrip().split('x') for s in f.readlines()]
f.close()

# calculates the amount of wrapping paper needed
def WrappingPaper(l, w, h):
    l, w, h = int(l), int(w), int(h)
    area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    slack = l * w * h // max(l, max(w, h))
    return area + slack

# use list comprehension to elegantly sum all the calculations (thanks Python!)
totalWrappingPaper = sum([WrappingPaper(l, w, h) for l, w, h in input])
print("The total amount of wrapping paper needed is: " + str(totalWrappingPaper))

# calculates the amount of ribbon needed
def Ribbon(l, w, h):
    l, w, h = int(l), int(w), int(h)
    wrap = (2 * l + 2 * w + 2 * h) - 2 * max(l, max(w, h))
    bow = l * w * h
    return wrap + bow

# one trick pony ;)
totalRibbon = sum([Ribbon(l, w, h) for l, w, h in input])
print("The total amount of ribbon needed is: " + str(totalRibbon))