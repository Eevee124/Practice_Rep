#make sure you're in the right directory!!!!

def task_one(filename):
    with open(filename) as f:
        file = f.readlines()

    opp = []
    you = []

    for line in file:
        opp.append(line[0])
        you.append(line[2])
    
    score = 0
    
    for i in range(len(opp)):

        win = False

        if (opp[i] == 'A' and you[i] == 'Y') or (opp[i] == 'B' and you[i] == 'Z') or (opp[i] == 'C' and you[i] == 'X'):
            win = True
        
        if you[i] == 'X':
            score += 1
        elif you[i] == 'Y':
            score += 2
        elif you[i] == 'Z':
            score += 3

        if win == True:
            score += 6
        elif (opp[i] == 'A' and you[i] == 'X') or (opp[i] == 'B' and you[i] == 'Y') or (opp[i] == 'C' and you[i] == 'Z'):
            score += 3
    
    return score



def task_two(filename):
    with open(filename) as f:
        file = f.readlines()

    opp = []
    end = []

    for line in file:
        opp.append(line[0])
        end.append(line[2])
    
    score = 0
    
    for i in range(len(opp)):

        if end[i] == 'Z':
            score += 6
            if opp[i] == 'A':
                score += 2
            elif opp[i] == 'B':
                score += 3
            else: score += 1
        
        elif end[i] == 'Y':
            score += 3
            if opp[i] == 'A':
                score += 1
            elif opp[i] == 'B':
                score += 2
            else:
                score += 3
        
        else:
            if opp[i] == 'A': score += 3
            elif opp[i] == 'B': score += 1
            else: score += 2
    
    return score



print(task_one('test.txt'))
print(task_two('test.txt'))

print(task_one('input.txt'))
print(task_two('input.txt'))