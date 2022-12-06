def first_task(filename):
    with open(filename) as f:
        file = f.readlines()
        assignement_pairs = [entry.strip() for entry in file]
    #print(assignement_pairs)
    #file.replace('-', ',')

    def contains(range_one, range_two):
        start_first, end_first = map(int, range_one.split('-'))
        start_second, end_second = map(int, range_two.split('-'))
       # print(start_first, end_first, ":", start_second, end_second)
        
        return start_first <= start_second and end_first >= end_second

    
    contained = 0
    for pair in assignement_pairs:
        first, second = pair.split(',')
        #print(first, second)

        if contains(first, second) or contains(second, first): contained += 1

    return contained


def second_task(filename):
    with open(filename) as f:
        file = f.readlines()
        assignement_pairs = [entry.strip() for entry in file]
    
    overlap = 0

    for pair in assignement_pairs:
        first, second = pair.split(',')
        start_first, end_first = map(int, first.split('-'))
        start_second, end_second = map(int, second.split('-'))

        if start_first in range(start_second, end_second + 1) or end_first in range(start_second, end_second + 1) or start_second in range(start_first, end_first + 1) or end_second in range(start_first, end_first + 1): overlap += 1

    return overlap

print(first_task('test.txt'))
print(first_task('input.txt'))

print(second_task('test.txt'))
print(second_task('input.txt'))