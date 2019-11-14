import os

# open the file and read the input
root = os.path.dirname(__file__)
f = open(os.path.join(root, "input.txt"))
input = f.readlines()
f.close()

# two dictionaries, one for the comands and one for results
commands = {}
results = {}

# fill the commands dictionary
for line in input:
    cmd, res = line.split('->')
    commands[res.strip()] = cmd.strip().split(' ')

# recursively walk the circuit for a given wire
def walk_circuit(wire):
    # if the current wire is a value, return it
    try:
        return int(wire)
    except ValueError:
        pass

    # if the wire is not in the results, calculate it
    if wire not in results:
        # get the command for the wire
        cmd = commands[wire]
        # if it is a value assignment, do so
        if len(cmd) == 1:
            res = walk_circuit(cmd[0])
        
        # else, get the correct operation and calculate the result
        else:
            op = cmd[-2]
            if op == 'AND':
                res = walk_circuit(cmd[0]) & walk_circuit(cmd[2])
            elif op == 'OR':
                res = walk_circuit(cmd[0]) | walk_circuit(cmd[2])
            elif op == 'NOT':
                res = ~walk_circuit(cmd[1]) & 0xffff # mask the output to ensure 16-bit encoding
            elif op == 'LSHIFT':
                res = walk_circuit(cmd[0]) << walk_circuit(cmd[2])
            elif op == 'RSHIFT':
                res = walk_circuit(cmd[0]) >> walk_circuit(cmd[2])

        # add the result to the wire
        results[wire] = res
    
    # return the wanted wire result
    return results[wire]

results['b'] = 46065 # comment for star 1
print(walk_circuit('a'))