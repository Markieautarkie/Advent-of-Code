import os
import re # regular expressions, used for star 2

# open and read the input
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = f.readlines()
f.close()

# lists that are used for applying rules for star 1
vowels = ['a', 'e', 'i', 'o', 'u']
notStrings = ["ab", "cd", "pq", "xy"]

# rules for nice strings of star 1, returns true if all the rules hold
def StringRulesOne(s):
    rule1 = sum([vowels.count(c) for c in s]) >= 3
    rule2 = len([i + j for i, j in zip(s, s[1:]) if i == j]) >= 1
    rule3 = not any(nono in s for nono in notStrings)
    return rule1 and rule2 and rule3

# rules for the nices strings of star 2, returns true if all the rules hold
def StringRulesTwo(s):
    rule1 = re.search(r'(..).*\1', s) # huuray for regex
    rule2 = len([i + j for i, j in zip(s, s[2:]) if i == j]) >= 1
    return rule1 and rule2

# count the amount of nice strings for star one and two
niceStringsOne = len([s.rstrip() for s in input if StringRulesOne(s.rstrip())])
niceStringsTwo = len([s.rstrip() for s in input if StringRulesTwo(s.rstrip())])

# print the amount of nice strings for both stars
print("Star 1 nice strings: " + str(niceStringsOne))
print("Star 2 nice strings: " + str(niceStringsTwo))