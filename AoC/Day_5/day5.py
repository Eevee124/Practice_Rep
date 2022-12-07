test = [
['Z', 'N'],
['M', 'C', 'D'],  
['P']]

input = [
    ['B', 'W', 'N'],
    ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
    ['Q', 'H', 'Z', 'W', 'R'],
    ['W', 'D', 'V', 'J', 'Z', 'R'],
    ['S', 'H', 'M', 'B'],
    ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
    ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
    ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
    ['Z', 'W', 'M', 'S', 'C', 'D', 'J']]


def task_one(filename):
    with open(filename) as f:
        file = f.readlines()
        instructions = [line.strip() for line in file]
    
    instr = []
    
    for line in instructions:
        x = line.replace('move', '')
        x = x.replace('from', '')
        x = x.replace('to', '')
        instr.append(x.split())

    #move 1 from 2 to 1
    print(instr)

    for instruction in instr:
        from_ = int(instruction[1]) - 1
        to_ = int(instruction[2]) - 1

        print(from_, to_, instruction)

        for i in range(int(instruction[0])):
            moved = input[from_].pop()
            #print(moved)
            input[to_].append(moved)
            #print(test)
    res = ''
    for line in input:
       res += line[-1]
    return res

def task_two(filename):
    with open(filename) as f:
        file = f.readlines()
    pass

#print(task_one('test.txt'))
print(task_one('input.txt'))

#print(task_two('test.txt'))
#print(task_two('input.txt'))