def first_task(filename):
    with open(filename) as f:
        file = f.readlines()
    print(type(file))
    #file.replace('-', ',')
    add = ''
    zones = []

    contained = 0

    for line in file:
        #line = line.replace('-', ',')
        for num in line:
            if not num.isdigit():
                zones.append(int(add))
                add = ''
                if num == line[-1]:
                    if (zones[0] <= zones[2] and zones[1] >= zones[3]) or (zones[2] <= zones[0] and zones[1] >= zones[1]):
                        contained += 1
                    zones = []
            else:
                add += num
    zones.append(int(add))
    if (zones[0] <= zones[2] and zones[1] >= zones[3]) or (zones[2] <= zones[0] and zones[1] >= zones[1]):
                        contained += 1

    return contained


def second_task(filename):
    pass

print(first_task('test.txt'))
print(first_task('input.txt'))

#print(second_task('test.txt'))
#print(second_task('input.txt'))