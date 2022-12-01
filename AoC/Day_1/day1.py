
def task_one(filename):
    with open(filename) as f:
        file = f.readlines()
        max = 0
        current = 0
        temp = 0

        for line in file:
            if max < current:
                max = current

            if not line == '\n' or line == file[-1]:
                temp += int(line.strip())
            else:
                current = temp
                temp = 0
    return max

def task_two(filename):
    with open(filename) as f:
        file = f.readlines()
        max = 0
        second_two = 0
        last = 0
        current = 0
        temp = 0

        for line in file:
            
            if not line == '\n' or line == file[-1]:
                temp += int(line.strip())
            else:
                current = temp
                temp = 0

            if line == file[-1]: current = temp

            if max < current:
                last = second_two
                second_two = max
                max = current
            elif second_two < current and not current == max:
                last = second_two
                second_two = current
            elif last < current and not current == second_two and not current == max:
                last = current


    return max + second_two + last

print(task_one('input.txt'))

print(task_two('input.txt'))