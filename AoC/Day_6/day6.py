def task_one(filename):
    with open(filename) as f:
        file = f.readlines()
    task = [line.strip() for line in file]

    seq = ''
    res = 0

    for i in range(len(task) - 3):
        for num in range(i, i + 4):
            seq += task[num]
        if not i in seq:
            res = task[]


def task_two(filename):
    with open(filename) as f:
        file = f.readlines()
    pass

print(task_one('test.txt'))
#print(task_one('input.txt'))

#print(task_two('test.txt'))
#print(task_two('input.txt'))