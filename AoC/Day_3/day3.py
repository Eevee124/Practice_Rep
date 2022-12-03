
def task_one(filename):
    with open(filename) as f:
        file = f.readlines()
    
    first = []
    second = []

    for line in file:
        line = line.strip()
        half = len(line)//2
        first.append(line[:half])
        second.append(line[half:])

    inside = False
    shared = []

    for j in range(len(first)):
        inside = False
        for i in range(len(first[j])):
            for n in range(len(first[j])):

                if first[j][i] == second[j][n] and not inside:
                    shared.append(first[j][i])
                    inside = True
    priority = 0
    temp = 0

    for letter in shared:

        if ord(letter) > 90:
            temp = ord(letter) - 96
            if temp % 26 == 0:
                priority += 26
            else: priority += temp % 26
        
        else:
            temp = ord(letter) - 38
            if temp % 26 == 0: 
                priority += 52
            else: priority += temp

    return priority


def task_two(filename):
    with open(filename) as f:
        file = f.readlines()

    first = []
    second = []
    third = []
    count = 0

    for line in file:
        line = line.strip()
        if count % 3 == 0: first.append(line)
        elif count % 3 == 1: second.append(line)
        else: third.append(line)
        count += 1
    
    print(first, second, third)

    shared = []
    inside = False

    for i, line in enumerate(first):
        inside = False
        for letter in line:
            if letter in second[i] and letter in third[i] and not inside:
                shared.append(letter)
                inside = True

    priority = 0
    temp = 0

    for letter in shared:

        if ord(letter) > 90:
            temp = ord(letter) - 96
            if temp % 26 == 0:
                priority += 26
            else: priority += temp % 26
        
        else:
            temp = ord(letter) - 38
            if temp % 26 == 0: 
                priority += 52
            else: priority += temp

    return priority


#print(task_one('test.txt'))
#print(task_one('input.txt'))

print(task_two('test.txt'))
print(task_two('input.txt'))
